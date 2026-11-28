# -*- coding: utf-8 -*-
"""
把官网 CHANGELOGS 发到腾讯频道「更新日志」版块（与 Discord 同源）。

依赖本机已安装 tencent-channel-cli，并用 QQ 互联 Token 登录：
  - 环境变量 QQ_AI_CONNECT_TOKEN
  - 或 ~/.qqcli/.env 中 QQ_AI_CONNECT_TOKEN=...
  - 或本仓 .local/qq-ai-connect-token.txt（脚本会自动注入环境变量）

凭据 / 目标（勿提交，已在 .gitignore 的 .local/）：
  .local/qq-ai-connect-token.txt
  .local/qq-changelog-guild-id.txt
  .local/qq-changelog-channel-id.txt          # 默认版块（更新日志）
  .local/qq-changelog-channel-{plugin}.txt    # 可选：按插件覆盖版块

用法:
  python scripts/post-changelogs-to-qq.py --plugin reader --latest
  python scripts/post-changelogs-to-qq.py --plugin weave --lang zh --latest
  python scripts/post-changelogs-to-qq.py --dry-run --plugin all --latest
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "website-embeds" / "changelog-embed.html"
LOCAL = ROOT / ".local"

PLUGIN_META = {
    "weave": {
        "name": "Weave Review",
        "gap_after": "1.0.0",
    },
    "reader": {
        "name": "Weave Reader",
        "gap_after": "0.8.0",
    },
    "ir": {
        "name": "Incremental Reading",
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

# 腾讯频道长贴上限约 10000 加权字；脚本按字符保守截断
QQ_MARKDOWN_SOFT_LIMIT = 9000


def ver_key(tag: str) -> tuple:
    return tuple(int(p) for p in re.split(r"[^\d]+", tag) if p.isdigit())


def read_local_line(name: str, *, required: bool = True) -> str:
    path = LOCAL / name
    if path.exists():
        line = path.read_text(encoding="utf-8").strip().splitlines()
        if line and line[0].strip():
            return line[0].strip()
    if required:
        raise SystemExit(f"未找到 {path}，请写入对应值（一行）")
    return ""


def ensure_token_env() -> None:
    if (os.environ.get("QQ_AI_CONNECT_TOKEN") or "").strip():
        return
    token = read_local_line("qq-ai-connect-token.txt", required=False)
    if token:
        os.environ["QQ_AI_CONNECT_TOKEN"] = token
        return
    dotenv = Path.home() / ".qqcli" / ".env"
    if dotenv.exists():
        for raw in dotenv.read_text(encoding="utf-8", errors="replace").splitlines():
            line = raw.strip()
            if line.startswith("QQ_AI_CONNECT_TOKEN="):
                val = line.split("=", 1)[1].strip().strip('"').strip("'")
                if val:
                    os.environ["QQ_AI_CONNECT_TOKEN"] = val
                    return
    raise SystemExit(
        "未找到 QQ Token：请设置 QQ_AI_CONNECT_TOKEN，"
        "或写入 .local/qq-ai-connect-token.txt / ~/.qqcli/.env"
    )


def find_cli() -> str:
    cmd = shutil.which("tencent-channel-cli") or shutil.which("tencent-channel-cli.cmd")
    if cmd:
        return cmd
    raise SystemExit(
        "未找到 tencent-channel-cli。请先执行: npm install -g tencent-channel-cli"
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


def resolve_channel_id(plugin: str) -> str:
    override = read_local_line(f"qq-changelog-channel-{plugin}.txt", required=False)
    if override:
        return override
    return read_local_line("qq-changelog-channel-id.txt")


def select_entries(all_data: dict, plugin: str, mode: str) -> list[dict]:
    entries = list(all_data.get(plugin) or [])
    if mode == "latest":
        return entries[:1]
    if mode == "since-site-gap":
        after = PLUGIN_META[plugin]["gap_after"]
        return [e for e in entries if ver_key(e["version"]) > ver_key(after)]
    return entries


def run_cli(cli: str, args: list[str], *, timeout: int = 120) -> dict:
    proc = subprocess.run(
        [cli, *args, "--json"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        env=os.environ.copy(),
    )
    out = (proc.stdout or "").strip()
    err = (proc.stderr or "").strip()
    payload: dict | None = None
    if out:
        try:
            payload = json.loads(out)
        except json.JSONDecodeError:
            # 有时 CLI 会在 JSON 前后混入日志行，取最后一段对象
            start = out.rfind("{")
            end = out.rfind("}")
            if start >= 0 and end > start:
                try:
                    payload = json.loads(out[start : end + 1])
                except json.JSONDecodeError:
                    payload = None
    if proc.returncode != 0:
        detail = err or out or f"exit {proc.returncode}"
        if payload and payload.get("error"):
            detail = json.dumps(payload["error"], ensure_ascii=False)
        raise SystemExit(f"tencent-channel-cli failed: {detail}")
    if not payload:
        raise SystemExit(f"tencent-channel-cli 无 JSON 输出: {out or err}")
    if payload.get("success") is False:
        raise SystemExit(
            f"tencent-channel-cli error: {json.dumps(payload.get('error') or payload, ensure_ascii=False)}"
        )
    return payload


def publish_feed(
    *,
    cli: str,
    guild_id: str,
    channel_id: str,
    title: str,
    markdown: str,
    dry_run: bool,
    label: str,
) -> None:
    body = markdown
    if len(body) > QQ_MARKDOWN_SOFT_LIMIT:
        body = body[: QQ_MARKDOWN_SOFT_LIMIT - 1] + "…"

    if dry_run:
        print(f"[dry-run][{label}] title={title!r} chars={len(body)}")
        print(body)
        print("---")
        return

    # Windows 命令行对多行/Markdown 不友好：写临时文件后用 content-file 风格不可用于 markdown
    # 官方支持 markdown_content via stdin JSON
    with tempfile.TemporaryDirectory(prefix="weave-qq-changelog-") as tmp:
        md_path = Path(tmp) / "body.md"
        md_path.write_text(body, encoding="utf-8")
        # content-file 走纯文本；Markdown 长贴用 stdin JSON 的 markdown_content
        payload = {
            "guild_id": guild_id,
            "channel_id": channel_id,
            "title": title,
            "feed_type": 2,
            "markdown_content": body,
        }
        raw = json.dumps(payload, ensure_ascii=False)
        proc = subprocess.run(
            [cli, "feed", "publish-feed", "--json"],
            input=raw,
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
            env=os.environ.copy(),
        )
        out = (proc.stdout or "").strip()
        err = (proc.stderr or "").strip()
        parsed: dict | None = None
        if out:
            try:
                parsed = json.loads(out)
            except json.JSONDecodeError:
                start = out.rfind("{")
                end = out.rfind("}")
                if start >= 0 and end > start:
                    try:
                        parsed = json.loads(out[start : end + 1])
                    except json.JSONDecodeError:
                        parsed = None
        if proc.returncode != 0 or (parsed and parsed.get("success") is False):
            detail = err or out
            err_obj = (parsed or {}).get("error") if parsed else None
            if parsed:
                detail = json.dumps(err_obj or parsed, ensure_ascii=False)
            detail_text = detail if isinstance(detail, str) else json.dumps(detail, ensure_ascii=False)
            # 官方限流：sleep 后由外层重试
            if "153" in detail_text or "频率" in detail_text or "rate" in detail_text.lower():
                raise RuntimeError(f"RATE_LIMITED:{detail_text}")
            raise SystemExit(f"发帖失败 [{label}] {title}: {detail}")
        share = ""
        data = (parsed or {}).get("data") if parsed else None
        if isinstance(data, dict):
            share = (
                data.get("share_url")
                or data.get("url")
                or (data.get("share") or {}).get("url")
                or ""
            )
        print(f"OK [{label}] {title}" + (f" {share}" if share else ""))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plugin", choices=["weave", "reader", "ir", "all"], default="all")
    ap.add_argument("--lang", choices=["zh", "en"], default="zh", help="QQ 默认中文")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--latest", action="store_true")
    g.add_argument("--since-site-gap", action="store_true")
    g.add_argument("--all-versions", dest="all_versions", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--delay", type=float, default=2.0)
    ap.add_argument(
        "--skip",
        action="append",
        default=[],
        help="跳过 plugin:version，可重复，例如 --skip reader:1.0.4",
    )
    args = ap.parse_args()

    mode = "latest" if args.latest else ("since-site-gap" if args.since_site_gap else "all")
    plugins = PLUGIN_ORDER if args.plugin == "all" else [args.plugin]
    lang = args.lang
    skip_set: set[tuple[str, str]] = set()
    for raw in args.skip or []:
        if ":" not in raw:
            raise SystemExit(f"--skip 格式应为 plugin:version，收到: {raw}")
        p, v = raw.split(":", 1)
        p, v = p.strip(), v.strip()
        if p not in PLUGIN_META:
            raise SystemExit(f"--skip 未知 plugin: {p}")
        skip_set.add((p, v))

    ensure_token_env()
    cli = find_cli()
    guild_id = read_local_line("qq-changelog-guild-id.txt")

    if not args.dry_run:
        status = run_cli(cli, ["login", "status"])
        data = status.get("data") or {}
        if not data.get("valid"):
            raise SystemExit(f"QQ 登录无效: {json.dumps(status, ensure_ascii=False)}")

    data = load_entries_via_node()
    jobs: list[tuple[str, dict, str]] = []
    for plugin in plugins:
        channel_id = resolve_channel_id(plugin)
        for entry in select_entries(data, plugin, mode):
            if (plugin, entry["version"]) in skip_set:
                print(f"skip [{plugin}/{lang}] {entry['version']} (--skip)")
                continue
            has_items = any((g.get(lang) or []) for g in entry.get("groups") or [])
            if not has_items:
                print(f"skip [{plugin}/{lang}] {entry['version']} (no items)")
                continue
            jobs.append((plugin, entry, channel_id))

    # 旧→新，最新留在版块时间线底部
    jobs.sort(key=lambda j: (PLUGIN_ORDER.index(j[0]), ver_key(j[1]["version"])))

    print(
        f"将发送 {len(jobs)} 条到 QQ 频道"
        f"（plugins={plugins}, lang={lang}, mode={mode}, dry_run={args.dry_run}）"
    )

    for i, (plugin, entry, channel_id) in enumerate(jobs):
        title = f'{PLUGIN_META[plugin]["name"]} {entry["version"]}'
        md = format_release_markdown(plugin, entry, lang)
        # 长贴正文不必重复标题行（标题已在 title）
        lines = md.splitlines()
        if lines and lines[0].startswith("# "):
            md_body = "\n".join(lines[1:]).strip()
        else:
            md_body = md
        label = f"{plugin}/{lang}"
        if args.dry_run:
            publish_feed(
                cli=cli,
                guild_id=guild_id,
                channel_id=channel_id,
                title=title,
                markdown=md_body,
                dry_run=True,
                label=label,
            )
        else:
            attempts = 0
            while True:
                attempts += 1
                try:
                    publish_feed(
                        cli=cli,
                        guild_id=guild_id,
                        channel_id=channel_id,
                        title=title,
                        markdown=md_body,
                        dry_run=False,
                        label=label,
                    )
                    break
                except RuntimeError as e:
                    msg = str(e)
                    if msg.startswith("RATE_LIMITED:") and attempts < 4:
                        print(f"rate-limited [{label}] {title}; sleep 70s then retry ({attempts}/3)")
                        time.sleep(70)
                        continue
                    raise SystemExit(msg)
        if not args.dry_run and i < len(jobs) - 1:
            time.sleep(args.delay)

    print(f"完成，实际发送 {len(jobs)} 条")
    return 0


if __name__ == "__main__":
    sys.exit(main())
