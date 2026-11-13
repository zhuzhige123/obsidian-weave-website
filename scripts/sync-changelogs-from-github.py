# -*- coding: utf-8 -*-
"""
从三款插件的 GitHub Release 同步官网更新日志到 index.html。

用法（在官网仓库根目录）:
  python scripts/sync-changelogs-from-github.py

依赖: 已登录的 gh CLI。
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
CACHE = ROOT / "scripts" / ".changelog-cache"
CACHE.mkdir(parents=True, exist_ok=True)

REPOS = {
    "weave": "zhuzhige123/obsidian---Weave",
    "reader": "zhuzhige123/obsidian-weave-reader",
    "ir": "zhuzhige123/Obsidian-Weave-incremental-reading",
}

# 官网已有、且本脚本不再从 Release 覆盖的底栏版本
KEEP_FROM = {
    "weave": "1.0.0",
    "reader": "0.8.0",
    "ir": "0.5.37",
}

META = {
    "weave": {
        "titleKey": "changelog.plugin.weave",
        "github": "https://github.com/zhuzhige123/obsidian---Weave/releases",
    },
    "reader": {
        "titleKey": "changelog.plugin.reader",
        "github": "https://github.com/zhuzhige123/obsidian-weave-reader/releases",
    },
    "ir": {
        "titleKey": "changelog.plugin.ir",
        "github": "https://github.com/zhuzhige123/Obsidian-Weave-incremental-reading/releases",
    },
}

TYPE_MAP = {
    "新增": "added",
    "优化": "improved",
    "调整": "changed",
    "修复": "fixed",
    "移除": "changed",
    "Added": "added",
    "Improved": "improved",
    "Changed": "changed",
    "Fixed": "fixed",
    "Removed": "changed",
}
PREFIX_RE = re.compile(
    r"^(新增|优化|调整|修复|移除|Added|Improved|Changed|Fixed|Removed)\s*[:：]\s*"
)
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")
HR_RE = re.compile(r"^---+\s*$")
H1_RE = re.compile(r"^#\s+")
ORDER = ["added", "improved", "changed", "fixed"]

WEAVE_110_ZH = {
    "added": [
        "AI 助手对话：可跟随当前笔记提问、分析与学习",
        "明确要求制卡后，结果先进入「预览卡片」再导入",
        "预览卡片可显示对话摘要，并可自动打开预览",
        "制卡可写入已有牌组或按名称新建；默认走预览导入",
        "输入 @ 可提及笔记或技能（内置与库内技能）",
        "助手可列出牌组与卡片、扫描低质量卡、展示相关卡并生成学习报告",
        "对话内确认后可删卡、移卡、删牌组，并创建 Markdown 笔记",
        "可将当前 EPUB 章节与高亮作为对话与制卡材料",
        "可发现并调用暴露官方 API 的已启用插件（Weave、阅读器、增量阅读）；写操作仅在你明确要求时使用",
        "支持多会话：新建、删除，并导出为 Markdown",
        "可编辑对话系统提示词，或恢复为插件默认",
    ],
    "changed": [
        "侧栏「AI 制卡」更名为「AI 助手」",
        "原独立制卡与摘录编辑任务改到对话中完成",
        "AI 助手页保留对话与解析预览",
        "编辑器选区命令改为把选区送入 AI 助手对话",
        "移除独立 AI 制卡页与摘录编辑制卡界面",
    ],
}


def ver_key(tag: str) -> tuple:
    parts = []
    for p in re.split(r"[^\d]+", tag):
        if p.isdigit():
            parts.append(int(p))
    return tuple(parts)


def strip_prefix(text: str) -> str:
    return PREFIX_RE.sub("", text).strip()


def split_lang(body: str) -> tuple[str, str]:
    text = (body or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    if not text:
        return "", ""
    parts = re.split(r"\n---+\n", text, maxsplit=1)
    if len(parts) == 2:
        left, right = parts[0].strip(), parts[1].strip()
        left_zh = bool(re.search(r"[\u4e00-\u9fff]", left))
        right_zh = bool(re.search(r"[\u4e00-\u9fff]", right))
        if not left_zh and right_zh:
            return right, left
        return left, right
    if re.search(r"[\u4e00-\u9fff]", text):
        return text, ""
    return "", text


def parse_sections(block: str) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    current: str | None = None
    for raw in (block or "").split("\n"):
        line = raw.strip()
        if not line or H1_RE.match(line) or HR_RE.match(line):
            continue
        hm = HEADING_RE.match(line)
        if hm:
            title = hm.group(1).strip()
            key = title.split()[0] if title else ""
            current = TYPE_MAP.get(key) or TYPE_MAP.get(title)
            if current and current not in groups:
                groups[current] = []
            continue
        if line.startswith("- ") or line.startswith("* "):
            item = strip_prefix(line[2:].strip())
            if not item:
                continue
            if not current:
                current = "improved"
                groups.setdefault(current, [])
            groups[current].append(item)
    return {k: v for k, v in groups.items() if v}


def groups_to_site(zh_groups: dict[str, list[str]], en_groups: dict[str, list[str]]) -> list[dict]:
    keys = [k for k in ORDER if zh_groups.get(k) or en_groups.get(k)]
    return [
        {"type": k, "items": {"zh": list(zh_groups.get(k) or []), "en": list(en_groups.get(k) or [])}}
        for k in keys
    ]


def fetch_releases(repo: str) -> list[dict]:
    raw = subprocess.check_output(
        ["gh", "api", f"repos/{repo}/releases", "--paginate"],
        text=True,
        encoding="utf-8",
        errors="replace",
    ).strip()
    if "][" in raw:
        raw = "[" + raw.replace("][", ",")[1:]
    return json.loads(raw) if raw.startswith("[") else []


def js_string(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def emit_entry(entry: dict, *, latest: bool, indent: int = 14) -> str:
    sp = " " * indent
    sp2 = " " * (indent + 2)
    sp3 = " " * (indent + 4)
    sp4 = " " * (indent + 6)
    sp5 = " " * (indent + 8)
    lines = [f"{sp}{{", f'{sp2}version: {js_string(entry["version"])},', f'{sp2}date: {js_string(entry["date"])},']
    if latest:
        lines.append(f"{sp2}latest: true,")
    lines.append(f"{sp2}groups: [")
    for gi, group in enumerate(entry["groups"]):
        lines.append(f"{sp3}{{")
        lines.append(f'{sp4}type: {js_string(group["type"])},')
        lines.append(f"{sp4}items: {{")
        for lang in ("zh", "en"):
            lines.append(f"{sp5}{lang}: [")
            for item in group["items"][lang]:
                lines.append(f"{sp5}  {js_string(item)},")
            lines.append(f"{sp5}],")
        lines.append(f"{sp4}}}")
        lines.append(f"{sp3}" + ("}," if gi < len(entry["groups"]) - 1 else "}"))
    lines.append(f"{sp2}]")
    lines.append(f"{sp}}}")
    return "\n".join(lines)


def extract_existing_entries(html: str, plugin: str) -> list[dict]:
    """Keep older website entries at/below KEEP_FROM by re-parsing current CHANGELOGS via node-less regex fallback.

    Simpler approach: slice the existing plugin block and eval with a tiny transform is fragile.
    Instead we keep a minimal frozen tail embedded below for the three baseline versions.
    """
    raise NotImplementedError


# Frozen tails (content already published on the site before this sync era)
FROZEN_TAILS: dict[str, list[dict]] = {
    "weave": [
        {
            "version": "1.0.0",
            "date": "2026-10-05",
            "groups": [
                {
                    "type": "added",
                    "items": {
                        "zh": [
                            "重要日程视图，在牌组学习界面用圆点切换，集中查看当天与近期安排",
                            "牌组树状图，按父牌组 / 子牌组层级展示记忆牌组与学习进度",
                            "记忆牌组支持设为子牌组、改挂父级，或升为一级牌组",
                            "从考试题组一键生成考试安排，写入日历",
                            "笔记任务（#weave-task），可在日程中勾选、改时间、跳回原笔记",
                            "重要日程支持关联日记，并识别阅读器阅读计划与增量阅读点",
                            "牌组独立记忆配置；标签树可显示今日可学数量",
                            "牌组学习界面可手动切换网格 / 看板视图",
                            "离线激活与许可证 Cloudflare 国际中转",
                            "界面可见性设置，可分别隐藏记忆牌组、考试题组、重要日程等入口",
                        ],
                        "en": [
                            "Important Schedule view on the deck study screen",
                            "Deck tree with parent / child hierarchy and progress",
                            "Memory decks can become child decks, reparent, or promote",
                            "One-click exam schedules from quiz banks",
                            "Note tasks (#weave-task) with check-off, reschedule, and jump-back",
                            "Schedule links daily notes, reader plans, and IR points",
                            "Per-deck memory settings; tag tree due counts",
                            "Manual grid / kanban switch on deck study",
                            "Offline activation and Cloudflare license relay",
                            "UI visibility settings for decks, quiz banks, and schedule",
                        ],
                    },
                },
                {
                    "type": "improved",
                    "items": {
                        "zh": [
                            "重要日程月历支持单行 / 双行 / 完整日历，以及日间过渡图",
                            "重要日程支持来源筛选、搜索、仅看重要项、隐藏已完成",
                            "考试安排支持单场 / 整批改期与删除",
                        ],
                        "en": [
                            "Month calendar modes and day-transition art",
                            "Filters for source, search, important-only, hide completed",
                            "Reschedule or delete one exam session or a whole batch",
                        ],
                    },
                },
                {
                    "type": "changed",
                    "items": {
                        "zh": [
                            "卡片管理顶栏视图顺序改为表格 → 网格 → 看板 → 时间线",
                            "全局学习设置与单牌组记忆配置职责分开",
                            "仅作分组用的父牌组在日程中按文件夹占位",
                        ],
                        "en": [
                            "Card toolbar order is table → grid → kanban → timeline",
                            "Global Study Settings vs per-deck Memory Config separated",
                            "Grouping-only parent decks appear as folders in the schedule",
                        ],
                    },
                },
                {
                    "type": "fixed",
                    "items": {
                        "zh": [
                            "关闭学习结算弹窗后不再强制跳回插件主界面",
                            "插件重启后重要日程仍能正确读取已保存的考试安排",
                            "调整父 / 子牌组归属时的约束提示，避免层级错乱",
                        ],
                        "en": [
                            "Closing the study summary no longer forces a jump to the main UI",
                            "Important Schedule keeps exam plans across restarts",
                            "Clearer parent / child deck constraints",
                        ],
                    },
                },
            ],
        },
        {
            "version": "0.9.26",
            "date": "2026-09-26",
            "groups": [
                {
                    "type": "added",
                    "items": {
                        "zh": ["表格视图支持多种分组方式", "新增排序功能键"],
                        "en": ["Table view supports multiple grouping modes", "Added sort controls"],
                    },
                },
                {
                    "type": "improved",
                    "items": {
                        "zh": [
                            "批量操作功能键底部显示名称，移动端长按可滚动查看更多",
                            "重新设计看板列属性与表格标签列",
                        ],
                        "en": [
                            "Batch action labels under icons; long-press scroll on mobile",
                            "Redesigned kanban column properties and table tag column",
                        ],
                    },
                },
            ],
        },
        {
            "version": "0.9.24",
            "date": "2026-09-14",
            "groups": [
                {
                    "type": "fixed",
                    "items": {
                        "zh": [
                            "在牌组学习界面或新建卡片列表切换记忆牌组时，因空路径被误当成库根路径导致无法写入默认牌组目录的问题"
                        ],
                        "en": [
                            "Fixed empty-path normalize treating vault root as the deck folder, which blocked writing the default deck path"
                        ],
                    },
                }
            ],
        },
    ],
    "reader": [
        {
            "version": "0.8.0",
            "date": "2026-10-05",
            "groups": [
                {
                    "type": "added",
                    "items": {
                        "zh": [
                            "激活与云端校验新增国际中转节点；支持离线激活",
                            "书籍目录右键「加入阅读计划」「从本章起生成阅读计划」，可预览后写入本书数据页",
                            "选中文本工具条「复制」支持多种格式，可在基础设置中选择默认项",
                        ],
                        "en": [
                            "International license relay and offline activation",
                            "TOC context menu: add / generate reading plans into the book data page",
                            "Selection toolbar copy supports multiple formats with a default in settings",
                        ],
                    },
                },
                {
                    "type": "improved",
                    "items": {
                        "zh": ["后台阅读标签约 15 秒后自动挂起，切回后自动恢复进度"],
                        "en": ["Background reader tabs suspend after about 15s and resume on return"],
                    },
                },
                {
                    "type": "changed",
                    "items": {
                        "zh": ["番茄专注计时改为高级功能，未激活时需开启高级预览才可见"],
                        "en": ["Pomodoro focus timer is premium; preview mode required before activation"],
                    },
                },
                {
                    "type": "fixed",
                    "items": {
                        "zh": ["部分 TXT 书籍目录解析不全", "部分 TXT 书籍中文正文缩进异常"],
                        "en": [
                            "Fixed incomplete TOC parsing for some TXT books",
                            "Fixed Chinese body indentation issues in some TXT books",
                        ],
                    },
                },
            ],
        }
    ],
    "ir": [
        {
            "version": "0.5.37",
            "date": "2026-10-05",
            "groups": [
                {
                    "type": "added",
                    "items": {
                        "zh": [
                            "激活与云端校验新增国际中转节点：海外优先中转，国内可走直连备用",
                            "支持离线激活（适用部分单位内网环境）",
                        ],
                        "en": [
                            "International license relay with domestic direct fallback",
                            "Offline activation for restricted intranet environments",
                        ],
                    },
                }
            ],
        }
    ],
}


def build_entries(plugin: str) -> list[dict]:
    keep = KEEP_FROM[plugin]
    releases = fetch_releases(REPOS[plugin])
    entries: list[dict] = []
    for r in releases:
        tag = r.get("tag_name") or ""
        if ver_key(tag) <= ver_key(keep):
            continue
        date = (r.get("published_at") or "")[:10]
        body = r.get("body") or ""
        if plugin == "weave" and tag == "1.1.0":
            _, en_block = split_lang(body)
            entry = {
                "version": tag,
                "date": date,
                "groups": groups_to_site(WEAVE_110_ZH, parse_sections(en_block)),
            }
        else:
            zh_block, en_block = split_lang(body)
            groups = groups_to_site(parse_sections(zh_block), parse_sections(en_block))
            if not groups:
                continue
            entry = {"version": tag, "date": date, "groups": groups}
        entries.append(entry)
    entries.sort(key=lambda e: ver_key(e["version"]), reverse=True)
    frozen_versions = {e["version"] for e in FROZEN_TAILS[plugin]}
    entries = [e for e in entries if e["version"] not in frozen_versions]
    return entries + FROZEN_TAILS[plugin]


def emit_plugin(name: str, entries: list[dict]) -> str:
    meta = META[name]
    lines = [
        f"          {name}: {{",
        f'            titleKey: {js_string(meta["titleKey"])},',
        f'            github: {js_string(meta["github"])},',
        "            entries: [",
    ]
    for i, entry in enumerate(entries):
        block = emit_entry(entry, latest=(i == 0), indent=14)
        if i < len(entries) - 1:
            block += ","
        lines.append(block)
    lines.append("            ]")
    lines.append("          }")
    return "\n".join(lines)


def patch_index(changelogs_js: str) -> None:
    html = INDEX.read_text(encoding="utf-8")
    start = html.find("        var CHANGELOGS = {")
    end = html.find("        function pack()", start)
    if start < 0 or end < 0:
        raise SystemExit("Could not locate CHANGELOGS block in index.html")
    INDEX.write_text(html[:start] + changelogs_js + "\n" + html[end:], encoding="utf-8")


def main() -> int:
    all_entries = {name: build_entries(name) for name in ("weave", "reader", "ir")}
    for name, entries in all_entries.items():
        print(f"{name}: {len(entries)} entries, latest={entries[0]['version']}")
    js = (
        "        var CHANGELOGS = {\n"
        + emit_plugin("weave", all_entries["weave"])
        + ",\n"
        + emit_plugin("reader", all_entries["reader"])
        + ",\n"
        + emit_plugin("ir", all_entries["ir"])
        + "\n        };\n"
    )
    (CACHE / "changelogs.generated.js").write_text(js, encoding="utf-8")
    patch_index(js)
    print(f"updated {INDEX}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
