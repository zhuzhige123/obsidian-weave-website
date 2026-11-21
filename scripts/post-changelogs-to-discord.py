# -*- coding: utf-8 -*-
"""
把官网 CHANGELOGS 发到 Discord（按插件 + 语言分频道）。

格式对齐 GitHub Release / weave-changelog-style：
  # Weave Review 1.1.12
  ## Added
  - Added: ...

用法:
  python scripts/post-changelogs-to-discord.py --plugin weave --lang en --since-site-gap
  python scripts/post-changelogs-to-discord.py --plugin weave --lang en --latest
  python scripts/post-changelogs-to-discord.py --dry-run --plugin weave --lang en --latest

Webhook 本机私密文件（勿提交）:
  .local/discord-changelog-webhook-weave-en.txt
  .local/discord-changelog-webhook-reader-en.txt
  .local/discord-changelog-webhook-ir-en.txt
  .local/discord-changelog-webhook-weave-zh.txt
  ...
  或环境变量 DISCORD_CHANGELOG_WEBHOOK_WEAVE_EN 等
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
LOCAL = ROOT / ".local"

PLUGIN_META = {
    "weave": {
        "name": "Weave Review",
        "color": 0x6C8CFF,
        "gap_after": "1.0.0",
    },
    "reader": {
        "name": "Weave Reader",
        "color": 0x5BB8D4,
        "gap_after": "0.8.0",
    },
    "ir": {
        "name": "Incremental Reading",
        "color": 0x4CB87A,
        "gap_after": "0.5.37",
    },
}

GROUP_LABELS = {
    "added": ("新增", "Added"),
    "improved": ("优化", "Improved"),
    "changed": ("调整", "Changed"),
    "fixed": ("修复", "Fixed"),
}
GROUP_ORDER = ["added", "improved", "changed", "fixed"]
PLUGIN_ORDER = ["weave", "reader", "ir"]

DISCORD_CONTENT_LIMIT = 2000
DISCORD_EMBED_DESC_LIMIT = 4096
USER_AGENT = "WeaveChangelogBot/1.0 (+https://obsidian-weave.xyz)"


def ver_key(tag: str) -> tuple:
    return tuple(int(p) for p in re.split(r"[^\d]+", tag) if p.isdigit())


def webhook_path(plugin: str, lang: str) -> Path:
    return LOCAL / f"discord-changelog-webhook-{plugin}-{lang}.txt"


def webhook_env(plugin: str, lang: str) -> str:
    return f"DISCORD_CHANGELOG_WEBHOOK_{plugin.upper()}_{lang.upper()}"


def read_webhook(plugin: str, lang: str) -> str:
    env_key = webhook_env(plugin, lang)
    env = (os.environ.get(env_key) or "").strip()
    if env:
        return env
    path = webhook_path(plugin, lang)
    if path.exists():
        line = path.read_text(encoding="utf-8").strip().splitlines()[0].strip()
        if line:
            return line
    raise SystemExit(
        f"未找到 Webhook：请设置 {env_key}，或写入 {path}"
    )


def load_entries_via_node() -> dict:
    js = r"""
const fs = require('fs');
const html = fs.readFileSync(process.argv[1], 'utf8');
const start = html.indexOf('var CHANGELOGS = {');
const end = html.indexOf('function pack()', start);
if (start < 0 || end < 0) { console.error('parse fail'); process.exit(1); }
eval(html.slice(start, end));
const out = {};
for (const [k, v] of Object.entries(CHANGELOGS)) {
  out[k] = (v.entries || []).map(e => ({
    version: e.version,
    date: e.date,
    latest: !!e.latest,
    groups: (e.groups || []).map(g => ({
      type: g.type,
      zh: (g.items && g.items.zh) || [],
      en: (g.items && g.items.en) || [],
    })),
  }));
}
process.stdout.write(JSON.stringify(out));
"""
    raw = subprocess.check_output(
        ["node", "-e", js, str(INDEX)],
        cwd=str(ROOT),
        encoding="utf-8",
        errors="replace",
    )
    return json.loads(raw)


def strip_existing_prefix(text: str, lang: str) -> str:
    if lang == "zh":
        return re.sub(r"^(新增|优化|调整|修复|移除)\s*[:：]\s*", "", text.strip())
    return re.sub(
        r"^(Added|Improved|Changed|Fixed|Removed)\s*:\s*",
        "",
        text.strip(),
        flags=re.I,
    )


def format_release_markdown(plugin: str, entry: dict, lang: str) -> str:
    meta = PLUGIN_META[plugin]
    lines: list[str] = [f'# {meta["name"]} {entry["version"]}', ""]
    for gtype in GROUP_ORDER:
        group = next((g for g in entry.get("groups") or [] if g.get("type") == gtype), None)
        if not group:
            continue
        items = group.get(lang) or []
        if not items:
            continue
        zh_label, en_label = GROUP_LABELS[gtype]
        if lang == "zh":
            heading, prefix, colon = zh_label, zh_label, "："
        else:
            heading, prefix, colon = en_label, en_label, ": "
        lines.append(f"## {heading}")
        for item in items:
            body = strip_existing_prefix(item, lang)
            if not body:
                continue
            lines.append(f"- {prefix}{colon}{body}")
        lines.append("")
    return "\n".join(lines).strip()


def build_payload(plugin: str, entry: dict, lang: str) -> dict:
    body = format_release_markdown(plugin, entry, lang)
    username = "Weave Changelog" if lang == "en" else "Weave 更新日志"
    # flags=4 → SUPPRESS_EMBEDS（正文里若偶有链接也不展开预览）
    if len(body) <= DISCORD_CONTENT_LIMIT:
        return {"username": username, "content": body, "flags": 4}

    desc = body
    desc_lines = desc.splitlines()
    if desc_lines and desc_lines[0].startswith("# "):
        desc = "\n".join(desc_lines[1:]).strip()
    if len(desc) > DISCORD_EMBED_DESC_LIMIT:
        desc = desc[: DISCORD_EMBED_DESC_LIMIT - 1] + "…"
    return {
        "username": username,
        "flags": 4,
        "embeds": [
            {
                "title": f'{PLUGIN_META[plugin]["name"]} {entry["version"]}',
                "color": PLUGIN_META[plugin]["color"],
                "description": desc,
            }
        ],
    }


def post_webhook(url: str, payload: dict, *, dry_run: bool, label: str, retries: int = 5) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    title = ""
    if payload.get("content"):
        title = payload["content"].splitlines()[0]
    elif payload.get("embeds"):
        title = payload["embeds"][0].get("title", "")
    if dry_run:
        print(f"[dry-run][{label}] {title} ({len(body)} bytes)")
        return
    last_err: Exception | None = None
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(
            url + "?wait=true",
            data=body,
            headers={
                "Content-Type": "application/json",
                "User-Agent": USER_AGENT,
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                resp.read()
                print(f"OK {resp.status} [{label}] {title}")
                return
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")
            if e.code == 429:
                wait = 3.0 * attempt
                print(f"rate-limited [{label}] wait {wait:.0f}s…")
                time.sleep(wait)
                last_err = e
                continue
            raise SystemExit(f"Discord HTTP {e.code} [{label}]: {detail}") from e
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last_err = e
            wait = 2.0 * attempt
            print(f"retry {attempt}/{retries} [{label}] {title}: {e}; sleep {wait:.0f}s")
            time.sleep(wait)
    raise SystemExit(f"Discord post failed after retries [{label}] {title}: {last_err}")


def select_entries(all_data: dict, plugin: str, mode: str) -> list[dict]:
    entries = list(all_data.get(plugin) or [])
    if mode == "latest":
        return entries[:1]
    if mode == "since-site-gap":
        after = PLUGIN_META[plugin]["gap_after"]
        return [e for e in entries if ver_key(e["version"]) > ver_key(after)]
    return entries


def parse_start_at(raw: str | None) -> tuple[str, str] | None:
    if not raw:
        return None
    if ":" not in raw:
        raise SystemExit("--start-at 格式应为 plugin:version，例如 weave:1.1.0")
    plugin, version = raw.split(":", 1)
    plugin, version = plugin.strip(), version.strip()
    if plugin not in PLUGIN_META:
        raise SystemExit(f"未知 plugin: {plugin}")
    return plugin, version


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plugin", choices=["weave", "reader", "ir", "all"], default="all")
    ap.add_argument("--lang", choices=["zh", "en", "all"], default="en")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--latest", action="store_true")
    g.add_argument("--since-site-gap", action="store_true")
    g.add_argument("--all-versions", dest="all_versions", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--delay", type=float, default=1.4)
    ap.add_argument("--start-at", default=None, help="断点续发，例如 weave:1.1.8")
    args = ap.parse_args()

    mode = "latest" if args.latest else ("since-site-gap" if args.since_site_gap else "all")
    plugins = PLUGIN_ORDER if args.plugin == "all" else [args.plugin]
    langs = ["zh", "en"] if args.lang == "all" else [args.lang]
    start = parse_start_at(args.start_at)
    data = load_entries_via_node()

    jobs: list[tuple[str, str, dict]] = []
    for plugin in plugins:
        for entry in select_entries(data, plugin, mode):
            if start:
                sp, sv = start
                if PLUGIN_ORDER.index(plugin) < PLUGIN_ORDER.index(sp):
                    continue
                if plugin == sp and ver_key(entry["version"]) < ver_key(sv):
                    continue
            for lang in langs:
                has_items = any((g.get(lang) or []) for g in entry.get("groups") or [])
                if not has_items:
                    print(f"skip [{plugin}/{lang}] {entry['version']} (no items)")
                    continue
                jobs.append((plugin, lang, entry))

    # Discord 时间线：先发旧版，最新留在频道底部
    jobs.sort(
        key=lambda j: (PLUGIN_ORDER.index(j[0]), j[1], ver_key(j[2]["version"]))
    )

    print(
        f"将发送 {len(jobs)} 条"
        f"（plugins={plugins}, langs={langs}, mode={mode}, dry_run={args.dry_run}）"
    )

    # Preload webhooks only for needed pairs
    hooks: dict[tuple[str, str], str] = {}
    if not args.dry_run:
        for plugin, lang, _ in jobs:
            key = (plugin, lang)
            if key not in hooks:
                hooks[key] = read_webhook(plugin, lang)

    for i, (plugin, lang, entry) in enumerate(jobs):
        payload = build_payload(plugin, entry, lang)
        label = f"{plugin}/{lang}"
        url = "DRY" if args.dry_run else hooks[(plugin, lang)]
        post_webhook(url, payload, dry_run=args.dry_run, label=label)
        if not args.dry_run and i < len(jobs) - 1:
            time.sleep(args.delay)

    print(f"完成，实际发送 {len(jobs)} 条")
    return 0


if __name__ == "__main__":
    sys.exit(main())
