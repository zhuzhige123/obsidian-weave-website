# -*- coding: utf-8 -*-
"""Convert tutorial Markdown drafts into tutorials-data.js for the website prototype."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_WEAVE_MD = Path(
    r"C:\Users\lihua\Desktop\obsidian weave插件系列开发\plugin testing library"
    r"\10-项目\Weave产品\02-宣传与教程\obsidian weave 教程"
)
SOURCE_READER_MD = Path(
    r"C:\Users\lihua\Desktop\obsidian weave插件系列开发\plugin testing library"
    r"\10-项目\Weave产品\02-宣传与教程\obsidian weave epub reader 教程"
)
WEAVE_MD_DIR = ROOT / "tutorials" / "md"
WEAVE_MD_EN_DIR = ROOT / "tutorials" / "md-en"
READER_MD_DIR = ROOT / "tutorials" / "md-reader"
READER_MD_EN_DIR = ROOT / "tutorials" / "md-reader-en"
MSTODO_MD_DIR = ROOT / "tutorials" / "md-mstodo"
MSTODO_MD_EN_DIR = ROOT / "tutorials" / "md-mstodo-en"
OUT_JS = ROOT / "tutorials-data.js"
ASSETS = ROOT / "assets" / "tutorials"

LINK_MAP = {
    "We-01a 新建卡片": "create-card",
    "We-01b 表格视图": "table-view",
    "We-01c 网格视图": "grid-view",
    "We-01d 时间线视图": "timeline-view",
    "We-01e 看板视图": "kanban-view",
    "We-01f 关联卡片模式": "linked-cards",
    "We-01g 卡片题型": "card-types",
    "We-01h AI制卡": "ai-cards",
    "We-01i 批量解析": "batch-parse",
    "We-02a 牌组学习界面": "deck-study-ui",
    "We-02b 记忆牌组分析图表": "deck-analytics",
    "We-02c 记忆学习界面": "study-session",
    "We-02d 考试题组": "exam-deck",
    "We-02e 插入牌组视图": "embed-deck",
    "Er-00a 设计理念下的一些考虑": "reader-design",
    "Er-01a 安装与打开书架": "reader-install-shelf",
    "Er-01b 阅读器界面与阅读模式": "reader-ui-modes",
    "Er-01c 书签、进度与参考阅读点": "reader-bookmarks-progress",
    "Er-02a 摘录笔记工作流": "reader-excerpt-workflow",
    "Er-02b 高亮、想法与样式标注": "reader-highlights",
    "Er-02c 摘录汇总与时间线": "reader-excerpt-timeline",
    "Er-02d 双向溯源与正文回显": "reader-bidirectional",
    "Er-02e Canvas 脑图摘录": "reader-canvas-excerpt",
    "Er-02f 截图摘录": "reader-screenshot-excerpt",
    "Er-02g 行内摘录回显": "reader-inline-excerpt-echo",
    "Er-03a 段落阅读与沉浸式全屏": "reader-paragraph-immersive",
    "Er-03b 生词标注与词汇表": "reader-vocabulary",
    "Er-03c 目录标记与全书地图": "reader-toc-map",
    "Er-03d 书架书单": "reader-bookshelf-lists",
    "Er-03e 脚注与隐藏文本": "reader-footnotes",
    "Er-04a 导出笔记与模板": "reader-export-templates",
    "Er-04b 阅读器设置与数据同步": "reader-settings-sync",
    "Er-04c 与 Weave 制卡、增量阅读、AI 联动": "reader-weave-integration",
    "Er-04d 高级支持、隐私与常见问题": "reader-faq",
    "Mt-00a 这是什么、适合谁": "mtd-intro",
    "Mt-01a 安装与登录": "mtd-install-login",
    "Mt-01b 同步范围与第一条任务": "mtd-first-task",
    "Mt-02a 任务写法与字段映射": "mtd-task-format",
    "Mt-02b 备注、子任务与提醒": "mtd-notes-steps",
    "Mt-02c 云图标菜单与命令面板": "mtd-menu-commands",
    "Mt-03a 入站捕获与子标签路由": "mtd-inbound-routes",
    "Mt-03b 从 To Do 回链到 Obsidian": "mtd-backlink",
    "Mt-03c 与 Obsidian Tasks 并用": "mtd-tasks-compat",
    "Mt-04a 设置说明与数据隐私": "mtd-settings-privacy",
    "Mt-04b 常见问题": "mtd-faq",
    "Mt-04c 与 Weave 系列的关系": "mtd-vs-weave",
}

WEAVE_CATALOG = [
    {
        "file": "We-01a 新建卡片.md",
        "id": "create-card",
        "code": "We-01a",
        "plugin": "weave",
        "group": "creation",
        "level": "beginner",
        "title": {"zh": "新建卡片", "en": "Create cards"},
    },
    {
        "file": "We-01h AI制卡.md",
        "id": "ai-cards",
        "code": "We-01h",
        "plugin": "weave",
        "group": "creation",
        "level": "intermediate",
        "title": {"zh": "AI 制卡", "en": "AI card generation"},
    },
    {
        "file": "We-01i 批量解析.md",
        "id": "batch-parse",
        "code": "We-01i",
        "plugin": "weave",
        "group": "creation",
        "level": "intermediate",
        "title": {"zh": "批量解析", "en": "Batch parse import"},
    },
    {
        "file": "We-01b 表格视图.md",
        "id": "table-view",
        "code": "We-01b",
        "plugin": "weave",
        "group": "management",
        "level": "beginner",
        "title": {"zh": "表格视图", "en": "Table view"},
    },
    {
        "file": "We-01c 网格视图.md",
        "id": "grid-view",
        "code": "We-01c",
        "plugin": "weave",
        "group": "management",
        "level": "beginner",
        "title": {"zh": "网格视图", "en": "Grid view"},
    },
    {
        "file": "We-01d 时间线视图.md",
        "id": "timeline-view",
        "code": "We-01d",
        "plugin": "weave",
        "group": "management",
        "level": "intermediate",
        "title": {"zh": "时间线视图", "en": "Timeline view"},
    },
    {
        "file": "We-01e 看板视图.md",
        "id": "kanban-view",
        "code": "We-01e",
        "plugin": "weave",
        "group": "management",
        "level": "intermediate",
        "title": {"zh": "看板视图", "en": "Kanban view"},
    },
    {
        "file": "We-01f 关联卡片模式.md",
        "id": "linked-cards",
        "code": "We-01f",
        "plugin": "weave",
        "group": "management",
        "level": "intermediate",
        "title": {"zh": "关联卡片模式", "en": "Linked cards mode"},
    },
    {
        "file": "We-01g 卡片题型.md",
        "id": "card-types",
        "code": "We-01g",
        "plugin": "weave",
        "group": "management",
        "level": "beginner",
        "title": {"zh": "卡片题型", "en": "Card types"},
    },
    {
        "file": "We-02a 牌组学习界面.md",
        "id": "deck-study-ui",
        "code": "We-02a",
        "plugin": "weave",
        "group": "study",
        "level": "beginner",
        "title": {"zh": "牌组学习界面", "en": "Deck study screen"},
    },
    {
        "file": "We-02b 记忆牌组分析图表.md",
        "id": "deck-analytics",
        "code": "We-02b",
        "plugin": "weave",
        "group": "study",
        "level": "intermediate",
        "title": {"zh": "记忆牌组分析图表", "en": "Deck analytics"},
    },
    {
        "file": "We-02c 记忆学习界面.md",
        "id": "study-session",
        "code": "We-02c",
        "plugin": "weave",
        "group": "study",
        "level": "beginner",
        "title": {"zh": "记忆学习界面", "en": "Study session"},
    },
    {
        "file": "We-02d 考试题组.md",
        "id": "exam-deck",
        "code": "We-02d",
        "plugin": "weave",
        "group": "study",
        "level": "intermediate",
        "title": {"zh": "考试题组", "en": "Exam decks"},
    },
    {
        "file": "We-02e 插入牌组视图.md",
        "id": "embed-deck",
        "code": "We-02e",
        "plugin": "weave",
        "group": "study",
        "level": "intermediate",
        "title": {"zh": "插入牌组视图", "en": "Embedded deck view"},
    },
]

READER_CATALOG = [
    {
        "file": "Er-00a 设计理念下的一些考虑.md",
        "id": "reader-design",
        "code": "Er-00a",
        "plugin": "reader",
        "group": "start",
        "level": "beginner",
        "title": {"zh": "设计理念下的一些考虑", "en": "Design considerations"},
        "lead_en": "Why the reader makes certain choices in Obsidian.",
        "created": "2026-09-02",
        "layout": "essay",
        "numberedHeadings": True,
    },
    {
        "file": "Er-01a 安装与打开书架.md",
        "id": "reader-install-shelf",
        "code": "Er-01a",
        "plugin": "reader",
        "group": "er01",
        "level": "beginner",
        "title": {"zh": "安装与打开书架", "en": "Install & bookshelf"},
    },
    {
        "file": "Er-01b 阅读器界面与阅读模式.md",
        "id": "reader-ui-modes",
        "code": "Er-01b",
        "plugin": "reader",
        "group": "er01",
        "level": "beginner",
        "title": {"zh": "阅读器界面与阅读模式", "en": "Reader UI & modes"},
    },
    {
        "file": "Er-01c 书签、进度与参考阅读点.md",
        "id": "reader-bookmarks-progress",
        "code": "Er-01c",
        "plugin": "reader",
        "group": "er01",
        "level": "beginner",
        "title": {"zh": "书签、进度与参考阅读点", "en": "Bookmarks & progress"},
    },
    {
        "file": "Er-02a 摘录笔记工作流.md",
        "id": "reader-excerpt-workflow",
        "code": "Er-02a",
        "plugin": "reader",
        "group": "er02",
        "level": "beginner",
        "title": {"zh": "摘录笔记工作流", "en": "Excerpt workflow"},
    },
    {
        "file": "Er-02b 高亮、想法与样式标注.md",
        "id": "reader-highlights",
        "code": "Er-02b",
        "plugin": "reader",
        "group": "er02",
        "level": "beginner",
        "title": {"zh": "高亮、想法与样式标注", "en": "Highlights & notes"},
    },
    {
        "file": "Er-02c 摘录汇总与时间线.md",
        "id": "reader-excerpt-timeline",
        "code": "Er-02c",
        "plugin": "reader",
        "group": "er02",
        "level": "intermediate",
        "title": {"zh": "摘录汇总与时间线", "en": "Excerpt list & timeline"},
    },
    {
        "file": "Er-02d 双向溯源与正文回显.md",
        "id": "reader-bidirectional",
        "code": "Er-02d",
        "plugin": "reader",
        "group": "er02",
        "level": "intermediate",
        "title": {"zh": "双向溯源与正文回显", "en": "Bidirectional links"},
    },
    {
        "file": "Er-02e Canvas 脑图摘录.md",
        "id": "reader-canvas-excerpt",
        "code": "Er-02e",
        "plugin": "reader",
        "group": "er02",
        "level": "intermediate",
        "title": {"zh": "Canvas 脑图摘录", "en": "Canvas excerpts"},
    },
    {
        "file": "Er-02f 截图摘录.md",
        "id": "reader-screenshot-excerpt",
        "code": "Er-02f",
        "plugin": "reader",
        "group": "er02",
        "level": "intermediate",
        "title": {"zh": "截图摘录", "en": "Screenshot excerpts"},
    },
    {
        "file": "Er-02g 行内摘录回显.md",
        "id": "reader-inline-excerpt-echo",
        "code": "Er-02g",
        "plugin": "reader",
        "group": "er02",
        "level": "intermediate",
        "badge": "new",
        "title": {"zh": "行内摘录回显", "en": "Inline excerpt echo"},
    },
    {
        "file": "Er-03a 段落阅读与沉浸式全屏.md",
        "id": "reader-paragraph-immersive",
        "code": "Er-03a",
        "plugin": "reader",
        "group": "er03",
        "level": "intermediate",
        "title": {"zh": "段落阅读与沉浸式全屏", "en": "Paragraph & immersive mode"},
    },
    {
        "file": "Er-03b 生词标注与词汇表.md",
        "id": "reader-vocabulary",
        "code": "Er-03b",
        "plugin": "reader",
        "group": "er03",
        "level": "intermediate",
        "title": {"zh": "生词标注与词汇表", "en": "Vocabulary & word lists"},
    },
    {
        "file": "Er-03c 目录标记与全书地图.md",
        "id": "reader-toc-map",
        "code": "Er-03c",
        "plugin": "reader",
        "group": "er03",
        "level": "intermediate",
        "title": {"zh": "目录标记与全书地图", "en": "TOC marks & book map"},
    },
    {
        "file": "Er-03d 书架书单.md",
        "id": "reader-bookshelf-lists",
        "code": "Er-03d",
        "plugin": "reader",
        "group": "er03",
        "level": "beginner",
        "title": {"zh": "书架书单", "en": "Bookshelf lists"},
    },
    {
        "file": "Er-03e 脚注与隐藏文本.md",
        "id": "reader-footnotes",
        "code": "Er-03e",
        "plugin": "reader",
        "group": "er03",
        "level": "intermediate",
        "title": {"zh": "脚注与隐藏文本", "en": "Footnotes & hidden text"},
    },
    {
        "file": "Er-04a 导出笔记与模板.md",
        "id": "reader-export-templates",
        "code": "Er-04a",
        "plugin": "reader",
        "group": "er04",
        "level": "intermediate",
        "title": {"zh": "导出笔记与模板", "en": "Export & templates"},
    },
    {
        "file": "Er-04b 阅读器设置与数据同步.md",
        "id": "reader-settings-sync",
        "code": "Er-04b",
        "plugin": "reader",
        "group": "er04",
        "level": "intermediate",
        "title": {"zh": "阅读器设置与数据同步", "en": "Settings & sync"},
    },
    {
        "file": "Er-04c 与 Weave 制卡、增量阅读、AI 联动.md",
        "id": "reader-weave-integration",
        "code": "Er-04c",
        "plugin": "reader",
        "group": "er04",
        "level": "intermediate",
        "title": {"zh": "与 Weave / 增量阅读 / AI 联动", "en": "Weave & IR integration"},
    },
    {
        "file": "Er-04d 高级支持、隐私与常见问题.md",
        "id": "reader-faq",
        "code": "Er-04d",
        "plugin": "reader",
        "group": "er04",
        "level": "beginner",
        "title": {"zh": "高级支持、隐私与常见问题", "en": "Premium, privacy & FAQ"},
    },
]

MSTODO_CATALOG = [
    {
        "file": "Mt-00a 这是什么、适合谁.md",
        "id": "mtd-intro",
        "code": "Mt-00a",
        "plugin": "mstodo",
        "group": "start",
        "level": "beginner",
        "title": {"zh": "这是什么、适合谁", "en": "What it is & who it’s for"},
    },
    {
        "file": "Mt-01a 安装与登录.md",
        "id": "mtd-install-login",
        "code": "Mt-01a",
        "plugin": "mstodo",
        "group": "mt01",
        "level": "beginner",
        "title": {"zh": "安装与登录", "en": "Install & sign in"},
    },
    {
        "file": "Mt-01b 同步范围与第一条任务.md",
        "id": "mtd-first-task",
        "code": "Mt-01b",
        "plugin": "mstodo",
        "group": "mt01",
        "level": "beginner",
        "title": {"zh": "同步范围与第一条任务", "en": "Scope & first task"},
    },
    {
        "file": "Mt-02a 任务写法与字段映射.md",
        "id": "mtd-task-format",
        "code": "Mt-02a",
        "plugin": "mstodo",
        "group": "mt02",
        "level": "beginner",
        "title": {"zh": "任务写法与字段映射", "en": "Task syntax & field map"},
    },
    {
        "file": "Mt-02b 备注、子任务与提醒.md",
        "id": "mtd-notes-steps",
        "code": "Mt-02b",
        "plugin": "mstodo",
        "group": "mt02",
        "level": "beginner",
        "title": {"zh": "备注、子任务与提醒", "en": "Notes, steps & reminders"},
    },
    {
        "file": "Mt-02c 云图标菜单与命令面板.md",
        "id": "mtd-menu-commands",
        "code": "Mt-02c",
        "plugin": "mstodo",
        "group": "mt02",
        "level": "beginner",
        "title": {"zh": "云图标菜单与命令面板", "en": "Cloud menu & commands"},
    },
    {
        "file": "Mt-03a 入站捕获与子标签路由.md",
        "id": "mtd-inbound-routes",
        "code": "Mt-03a",
        "plugin": "mstodo",
        "group": "mt03",
        "level": "intermediate",
        "title": {"zh": "入站捕获与子标签路由", "en": "Inbound capture & routes"},
    },
    {
        "file": "Mt-03b 从 To Do 回链到 Obsidian.md",
        "id": "mtd-backlink",
        "code": "Mt-03b",
        "plugin": "mstodo",
        "group": "mt03",
        "level": "intermediate",
        "title": {"zh": "从 To Do 回链到 Obsidian", "en": "Backlink from To Do"},
    },
    {
        "file": "Mt-03c 与 Obsidian Tasks 并用.md",
        "id": "mtd-tasks-compat",
        "code": "Mt-03c",
        "plugin": "mstodo",
        "group": "mt03",
        "level": "intermediate",
        "title": {"zh": "与 Obsidian Tasks 并用", "en": "Using with Obsidian Tasks"},
    },
    {
        "file": "Mt-04a 设置说明与数据隐私.md",
        "id": "mtd-settings-privacy",
        "code": "Mt-04a",
        "plugin": "mstodo",
        "group": "mt04",
        "level": "beginner",
        "title": {"zh": "设置说明与数据隐私", "en": "Settings & privacy"},
    },
    {
        "file": "Mt-04b 常见问题.md",
        "id": "mtd-faq",
        "code": "Mt-04b",
        "plugin": "mstodo",
        "group": "mt04",
        "level": "beginner",
        "title": {"zh": "常见问题", "en": "FAQ"},
    },
    {
        "file": "Mt-04c 与 Weave 系列的关系.md",
        "id": "mtd-vs-weave",
        "code": "Mt-04c",
        "plugin": "mstodo",
        "group": "mt04",
        "level": "beginner",
        "title": {"zh": "与 Weave 系列的关系", "en": "Relation to Weave series"},
    },
]


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def inline(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text)
    text = re.sub(r"\s*\^[A-Za-z0-9_-]+\s*$", "", text)
    text = re.sub(r"!\[\[([^\]]+)\]\]", wiki_image, text)

    def wiki_or_code(m: re.Match[str]) -> str:
        name = m.group(1).strip()
        tid = LINK_MAP.get(name)
        if tid:
            return f'<a href="#{tid}" data-goto="{tid}">{esc(name)}</a>'
        return f"<code>{esc(name)}</code>"

    text = re.sub(r"`([^`]+)`", wiki_or_code, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def wiki_image(m: re.Match[str]) -> str:
    name = m.group(1).strip()
    local = ASSETS / name
    lower = name.lower()
    is_video = lower.endswith((".mp4", ".webm", ".mov"))
    if lower.endswith(".gif"):
        kind = "GIF"
    elif is_video:
        kind = "Video"
    else:
        kind = "Screenshot"
    if local.exists():
        if is_video:
            return (
                f'<figure class="figure figure-video">'
                f'<video controls playsinline preload="metadata" '
                f'src="assets/tutorials/{esc(name)}"></video>'
                f"<figcaption>{esc(name)}</figcaption></figure>"
            )
        return (
            f'<figure class="figure"><img src="assets/tutorials/{esc(name)}" alt="" />'
            f"<figcaption>{esc(name)}</figcaption></figure>"
        )
    return (
        f'<figure class="figure is-placeholder"><div class="ph">{kind} · {esc(name)}</div>'
        f"<figcaption>Place image at assets/tutorials/{esc(name)}</figcaption></figure>"
    )


def note_inline(text: str) -> str:
    """Inline markdown for rendered note previews (links, ==highlight==, bold, code)."""

    def link_sub(m: re.Match[str]) -> str:
        return f'<a href="{esc(m.group(2))}">{esc(m.group(1))}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_sub, text)
    text = re.sub(
        r"==([^=]+)==",
        r'<mark class="note-hl">\1</mark>',
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", lambda m: f"<code>{esc(m.group(1))}</code>", text)
    return text


def convert_note_preview(md: str) -> str:
    """Render a sample note as HTML (no h3, so it won't pollute the page TOC)."""
    lines = md.replace("\r\n", "\n").strip().split("\n")
    out: list[str] = []
    list_items: list[str] = []
    para: list[str] = []

    def flush_para() -> None:
        if not para:
            return
        out.append(f"<p>{note_inline(' '.join(para))}</p>")
        para.clear()

    def flush_list() -> None:
        nonlocal list_items
        if not list_items:
            return
        out.append("<ul>" + "".join(f"<li>{x}</li>" for x in list_items) + "</ul>")
        list_items = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_para()
            flush_list()
            continue
        m_h = re.match(r"^#{2,4}\s+(.+)$", stripped)
        if m_h:
            flush_para()
            flush_list()
            out.append(f'<p class="note-preview-h">{note_inline(m_h.group(1))}</p>')
            continue
        m_ul = re.match(r"^[-*]\s+(.+)$", stripped)
        if m_ul:
            flush_para()
            list_items.append(note_inline(m_ul.group(1)))
            continue
        flush_list()
        para.append(stripped)
    flush_para()
    flush_list()
    return f'<div class="note-preview">{"".join(out)}</div>'


def flush_para(buf: list[str], out: list[str]) -> None:
    if not buf:
        return
    text = inline(" ".join(x.strip() for x in buf if x.strip()))
    buf.clear()
    if text:
        out.append(f"<p>{text}</p>")


def list_item_html(raw: str) -> str:
    nested = re.match(r"^(.*?):\s*$", raw.strip())
    return inline(raw.strip())


def convert_table(rows: list[str]) -> str:
    parsed = []
    for row in rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        parsed.append(cells)
    if len(parsed) < 2:
        return ""
    head, body = parsed[0], parsed[2:] if is_sep(parsed[1]) else parsed[1:]
    html = ["<table><thead><tr>"]
    html.extend(f"<th>{inline(c)}</th>" for c in head)
    html.append("</tr></thead><tbody>")
    for row in body:
        html.append("<tr>")
        html.extend(f"<td>{inline(c)}</td>" for c in row)
        html.append("</tr>")
    html.append("</tbody></table>")
    return "".join(html)


def is_sep(cells: list[str]) -> bool:
    return all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells if c)


def convert_markdown(md: str) -> tuple[str, str]:
    md = md.replace("\r\n", "\n").strip()
    md = re.sub(r"<!-- weave-test-stats:.*?-->", "", md)
    parts = re.split(r"(```[\s\S]*?```)", md)
    lead = ""
    html_parts: list[str] = []

    def convert_text_block(block: str, is_first: bool) -> None:
        nonlocal lead
        lines = block.split("\n")
        para: list[str] = []
        list_items: list[tuple[str, int, str]] | None = None
        table_rows: list[str] = []
        seen_heading = False
        i = 0

        def flush_list() -> None:
            nonlocal list_items
            if not list_items:
                return
            html_parts.append(render_list(list_items))
            list_items = None

        def flush_table() -> None:
            nonlocal table_rows
            if table_rows:
                html_parts.append(convert_table(table_rows))
                table_rows = []

        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            if not stripped:
                flush_para(para, html_parts)
                flush_table()
                i += 1
                continue
            if stripped.startswith("|") and stripped.endswith("|"):
                flush_para(para, html_parts)
                flush_list()
                table_rows.append(stripped)
                i += 1
                continue
            flush_table()
            m_h = re.match(r"^(#{2,4})\s+(.+)$", stripped)
            if m_h:
                flush_para(para, html_parts)
                flush_list()
                seen_heading = True
                level = len(m_h.group(1))
                tag = "h3" if level == 2 else f"h{level}"
                html_parts.append(f"<{tag}>{inline(m_h.group(2))}</{tag}>")
                i += 1
                continue
            if stripped.startswith(">"):
                flush_para(para, html_parts)
                flush_list()
                quote = [re.sub(r"^>\s?", "", stripped)]
                i += 1
                while i < len(lines) and lines[i].strip().startswith(">"):
                    quote.append(re.sub(r"^>\s?", "", lines[i].strip()))
                    i += 1
                html_parts.append(f"<blockquote><p>{inline(' '.join(quote))}</p></blockquote>")
                continue
            m_ol = re.match(r"^(\d+)\.\s+(.+)$", stripped)
            m_ul = re.match(r"^[-*]\s+(.+)$", stripped)
            indent_ul = re.match(r"^(\s{2,})[-*]\s+(.+)$", line)
            indent_ol = re.match(r"^(\s{2,})\d+\.\s+(.+)$", line)
            if m_ol or m_ul or indent_ul or indent_ol:
                flush_para(para, html_parts)
                if list_items is None:
                    list_items = []
                if indent_ul:
                    list_items.append(("ul", 1, indent_ul.group(2)))
                elif indent_ol:
                    list_items.append(("ol", 1, indent_ol.group(2)))
                elif m_ol:
                    list_items.append(("ol", 0, m_ol.group(2)))
                else:
                    list_items.append(("ul", 0, m_ul.group(1)))
                i += 1
                continue
            # Lead is only the first paragraph before any heading (tutorial intro style).
            if is_first and not lead and not seen_heading and not stripped.startswith("#"):
                lead = re.sub(r"\s+", " ", stripped)
                i += 1
                continue
            flush_list()
            para.append(stripped)
            i += 1
        flush_para(para, html_parts)
        flush_list()
        flush_table()

    for idx, part in enumerate(parts):
        if part.startswith("```"):
            inner = part[3:]
            nl = inner.find("\n")
            lang = inner[:nl].strip() if nl != -1 else ""
            code = inner[nl + 1 :] if nl != -1 else inner
            if code.endswith("```"):
                code = code[:-3]
            code = code.rstrip()
            if lang in ("note", "preview", "note-preview"):
                html_parts.append(convert_note_preview(code))
            else:
                html_parts.append(
                    f'<pre><code class="lang-{esc(lang)}">{esc(code)}</code></pre>'
                )
        else:
            convert_text_block(part, idx == 0)
    return lead.rstrip("：:").replace("以下是详细介绍", "").strip(" ：:"), "".join(html_parts)


def render_list(items: list[tuple[str, int, str]]) -> str:
    if not items:
        return ""
    # Group nested bullets under previous top-level item.
    kind = items[0][0]
    chunks: list[str] = [f"<{kind}>"]
    i = 0
    while i < len(items):
        typ, depth, text = items[i]
        if depth == 0:
            nested: list[tuple[str, int, str]] = []
            j = i + 1
            while j < len(items) and items[j][1] > 0:
                nested.append((items[j][0], 0, items[j][2]))
                j += 1
            inner = f"<li>{inline(text)}"
            if nested:
                inner += render_list(nested)
            inner += "</li>"
            chunks.append(inner)
            i = j
        else:
            chunks.append(f"<li>{inline(text)}</li>")
            i += 1
    chunks.append(f"</{kind}>")
    return "".join(chunks)


WELCOME = {
    "id": "welcome",
    "code": "—",
    "plugin": "weave",
    "group": "start",
    "level": "beginner",
    "title": {"zh": "教程导读与学习路径", "en": "Guide & learning paths"},
    "lead": {
        "zh": "按你的目标选择阅读顺序。每篇教程对应插件内的一个具体界面或任务。",
        "en": "Pick a path by goal. Each article maps to a concrete screen or task in the plugin.",
    },
    "body": {
        "zh": """<div class="path-cards">
<article class="path-card"><h4>新用户 15 分钟</h4><p>先会制卡，再会学习。</p><a href="#create-card" data-goto="create-card">新建卡片 → 牌组学习 → 记忆学习</a></article>
<article class="path-card"><h4>整理已有卡片</h4><p>表格筛选、看板与时间线。</p><a href="#table-view" data-goto="table-view">从表格视图开始</a></article>
<article class="path-card"><h4>批量制卡</h4><p>AI 生成与规则解析两条路径。</p><a href="#ai-cards" data-goto="ai-cards">AI 制卡 → 批量解析</a></article>
</div>
<h3>教程与插件界面的对应关系</h3>
<p>「卡片管理」与「牌组学习」是两个不同入口：前者偏查看、筛选与整理；后者偏复习、开练与牌组操作。左侧目录按此划分。</p>
<p>正文来自产品库 <code>obsidian weave 教程</code>。顶栏可切换到 EPUB Reader 阅读器教程。</p>""",
        "en": """<div class="path-cards">
<article class="path-card"><h4>15-minute start</h4><p>Create cards, then study.</p><a href="#create-card" data-goto="create-card">Create → Deck study → Review</a></article>
<article class="path-card"><h4>Organize cards</h4><p>Table, kanban, timeline.</p><a href="#table-view" data-goto="table-view">Start with table view</a></article>
<article class="path-card"><h4>Batch creation</h4><p>AI generation vs rule parsing.</p><a href="#ai-cards" data-goto="ai-cards">AI cards → Batch parse</a></article>
</div>
<h3>How tutorials map to the plugin</h3>
<p>Card management and deck study are separate entry points. Switch the top tab for EPUB Reader guides.</p>""",
    },
}

READER_WELCOME = {
    "id": "reader-welcome",
    "code": "—",
    "plugin": "reader",
    "group": "start",
    "level": "beginner",
    "title": {"zh": "阅读器教程导读", "en": "Reader guide & paths"},
    "lead": {
        "zh": "在 Obsidian 里读书、摘录、回链与制卡的完整路径。",
        "en": "Read, excerpt, link back, and integrate with Weave Deck in Obsidian.",
    },
    "body": {
        "zh": """<div class="path-cards">
<article class="path-card"><h4>设计理念</h4><p>为何手动书架、手动进度、不自动建摘录文件。</p><a href="#reader-design" data-goto="reader-design">设计理念下的一些考虑</a></article>
<article class="path-card"><h4>第一次打开</h4><p>安装插件，把书放进书架。</p><a href="#reader-install-shelf" data-goto="reader-install-shelf">安装与打开书架</a></article>
<article class="path-card"><h4>边读边记</h4><p>摘录写入笔记并跳回原文。</p><a href="#reader-excerpt-workflow" data-goto="reader-excerpt-workflow">摘录工作流 → 双向溯源</a></article>
<article class="path-card"><h4>英文原著</h4><p>生词标注与词汇表。</p><a href="#reader-vocabulary" data-goto="reader-vocabulary">生词标注与词汇表</a></article>
</div>
<h3>Er-00～Er-04 怎么读</h3>
<p><strong>Er-00</strong> 设计理念；<strong>Er-01</strong> 入门与界面；<strong>Er-02</strong> 摘录与高亮；<strong>Er-03</strong> 阅读增强；<strong>Er-04</strong> 导出、设置与系列联动。正文来自产品库 <code>obsidian weave epub reader 教程</code>。</p>""",
        "en": """<div class="path-cards">
<article class="path-card"><h4>Design</h4><p>Manual shelf, manual progress, excerpts where you choose.</p><a href="#reader-design" data-goto="reader-design">Design considerations</a></article>
<article class="path-card"><h4>First open</h4><p>Install and add books.</p><a href="#reader-install-shelf" data-goto="reader-install-shelf">Install & bookshelf</a></article>
<article class="path-card"><h4>Read & excerpt</h4><p>Notes with bidirectional links.</p><a href="#reader-excerpt-workflow" data-goto="reader-excerpt-workflow">Excerpt workflow</a></article>
</div>
<p>Er-00 design, Er-01 setup, Er-02 excerpts, Er-03 reading features, Er-04 export & integration.</p>""",
    },
}

MSTODO_WELCOME = {
    "id": "mtd-welcome",
    "code": "—",
    "plugin": "mstodo",
    "group": "start",
    "level": "beginner",
    "title": {"zh": "MS To Do Sync 教程导读", "en": "MS To Do Sync guide & paths"},
    "lead": {
        "zh": "在 Obsidian 规划任务，在 Microsoft To Do 执行；选择性同步，与 Weave 系列无依赖。",
        "en": "Plan in Obsidian, execute in Microsoft To Do—selective sync, no Weave dependency.",
    },
    "body": {
        "zh": """<div class="path-cards">
<article class="path-card"><h4>这是什么</h4><p>独立插件、适合谁、核心原则。</p><a href="#mtd-intro" data-goto="mtd-intro">这是什么、适合谁</a></article>
<article class="path-card"><h4>15 分钟上手</h4><p>安装登录，写第一条带标签任务。</p><a href="#mtd-install-login" data-goto="mtd-install-login">安装与登录 → 第一条任务</a></article>
<article class="path-card"><h4>日常写法</h4><p>日期、备注、子任务与云图标。</p><a href="#mtd-task-format" data-goto="mtd-task-format">任务写法 → 备注与步骤</a></article>
<article class="path-card"><h4>进阶与排错</h4><p>入站路由、回链、Tasks 兼容与 FAQ。</p><a href="#mtd-inbound-routes" data-goto="mtd-inbound-routes">入站路由 → 常见问题</a></article>
</div>
<h3>Mt-00～Mt-04 怎么读</h3>
<p><strong>Mt-00</strong> 定位；<strong>Mt-01</strong> 安装与范围；<strong>Mt-02</strong> 日常同步；<strong>Mt-03</strong> 入站 / 回链 / Tasks；<strong>Mt-04</strong> 设置、隐私与和 Weave 的关系。本插件<strong>不属于</strong> Weave 系列产品包，仅同属一位开发者。</p>""",
        "en": """<div class="path-cards">
<article class="path-card"><h4>What it is</h4><p>Standalone plugin, audience, principles.</p><a href="#mtd-intro" data-goto="mtd-intro">What it is & who it’s for</a></article>
<article class="path-card"><h4>15-minute start</h4><p>Install, sign in, first tagged task.</p><a href="#mtd-install-login" data-goto="mtd-install-login">Install → first task</a></article>
<article class="path-card"><h4>Daily syntax</h4><p>Dates, notes, steps, cloud menu.</p><a href="#mtd-task-format" data-goto="mtd-task-format">Task syntax → notes & steps</a></article>
<article class="path-card"><h4>Advanced & FAQ</h4><p>Inbound routes, backlinks, Tasks, FAQ.</p><a href="#mtd-inbound-routes" data-goto="mtd-inbound-routes">Inbound → FAQ</a></article>
</div>
<p><strong>Mt-00</strong> intro; <strong>Mt-01</strong> setup; <strong>Mt-02</strong> daily sync; <strong>Mt-03</strong> inbound / backlink / Tasks; <strong>Mt-04</strong> settings & relation to Weave. Not part of the Weave product bundle—same developer only.</p>""",
    },
}

SERIES = {
    "id": "series-intro",
    "code": "—",
    "plugin": "weave",
    "group": "series",
    "level": "beginner",
    "title": {"zh": "Weave 系列插件介绍", "en": "Weave plugin series intro"},
    "lead": {
        "zh": "Weave Deck、EPUB Reader、Incremental Reading 三款插件如何分工与组合。",
        "en": "How Weave Deck, EPUB Reader, and IR divide work and combine.",
    },
    "body": {
        "zh": "<p>Weave Deck、EPUB Reader、增量阅读三款插件如何分工与组合。各插件操作教程见顶栏切换。</p>",
        "en": "<p>How Weave Deck, EPUB Reader, and IR divide work. Switch plugins from the Tutorials menu in the top bar.</p>",
    },
}

IR = {
    "id": "ir-soon",
    "code": "—",
    "plugin": "ir",
    "group": "series",
    "level": "beginner",
    "title": {"zh": "增量阅读教程（筹备中）", "en": "Incremental Reading (coming)"},
    "lead": {
        "zh": "阅读点、专题与增量阅读日历的操作指南筹备中。",
        "en": "Reading points, topics, and IR calendar — in progress.",
    },
    "body": {
        "zh": "<p>增量阅读插件独立教程将在系列文档第二批发布。</p>",
        "en": "<p>IR tutorials ship in batch two of the docs rollout.</p>",
    },
}


def rename_plugin_mentions(text: str) -> str:
    """Display name is Weave Deck; series name stays Weave. Do not touch technical ids."""
    if not text:
        return text
    tokens = [
        ("Weave EPUB Reader", "\x00EPUB_READER\x00"),
        ("weave epub reader", "\x00epub_reader\x00"),
        ("Weave Deck", "\x00WEAVE_DECK\x00"),
        ("Obsidian Weave 插件系列", "\x00SERIES_ZH\x00"),
        ("Obsidian Weave plugin series", "\x00SERIES_EN\x00"),
        ("Obsidian Weave plugin family", "\x00SERIES_FAM\x00"),
        ("Weave 系列", "\x00SERIES_ZH2\x00"),
        ("Weave series", "\x00SERIES_EN2\x00"),
        ("Weave Series", "\x00SERIES_EN3\x00"),
        ("Weave-family", "\x00SERIES_FAM2\x00"),
        ("obsidian weave epub reader 教程", "\x00DIR_ER\x00"),
        ("obsidian weave 教程", "\x00DIR_WE\x00"),
        ("weave-decks", "\x00CODE_DECKS\x00"),
        ("weave-epub-reader", "\x00ID_READER\x00"),
        ("we_source", "\x00WE_SOURCE\x00"),
    ]
    for src, token in tokens:
        text = text.replace(src, token)
    text = text.replace("Weave 主插件", "\x00WEAVE_DECK\x00")
    text = text.replace("the main Weave plugin", "\x00WEAVE_DECK\x00")
    text = text.replace("main Weave plugin", "\x00WEAVE_DECK\x00")
    text = re.sub(r"Obsidian Weave", "\x00WEAVE_DECK\x00", text)
    text = re.sub(r"obsidian weave", "\x00WEAVE_DECK\x00", text)
    text = re.sub(
        r"Weave(?! Deck)(?! EPUB)(?! 系列)(?!-family)(?! series)(?! Series)",
        "\x00WEAVE_DECK\x00",
        text,
    )
    text = re.sub(r"(?<![A-Za-z0-9_\-])weave(?![A-Za-z0-9_\-])", "\x00WEAVE_DECK\x00", text)
    for src, token in tokens:
        restored = "Weave EPUB Reader" if src == "weave epub reader" else src
        text = text.replace(token, restored)
    text = re.sub(r"(Weave Deck)(?=[\u4e00-\u9fff])", r"\1 ", text)
    text = re.sub(r"(?<=[\u4e00-\u9fff])(Weave Deck)", r" \1", text)
    text = re.sub(r"(Weave EPUB Reader)(?=[\u4e00-\u9fff])", r"\1 ", text)
    text = re.sub(r"(?<=[\u4e00-\u9fff])(Weave EPUB Reader)", r" \1", text)
    text = text.replace("Weave Deck后", "Weave Deck 后")
    text = text.replace("Weave Deck中", "Weave Deck 中")
    text = text.replace("Weave Deck时", "Weave Deck 时")
    text = text.replace("Weave Deck的", "Weave Deck 的")
    text = text.replace("Weave Deck与", "Weave Deck 与")
    while "Weave Deck Deck" in text:
        text = text.replace("Weave Deck Deck", "Weave Deck")
    return text


def copy_sources() -> None:
    WEAVE_MD_DIR.mkdir(parents=True, exist_ok=True)
    READER_MD_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    if not SOURCE_WEAVE_MD.exists() or not SOURCE_READER_MD.exists():
        print("skip copy: product-library source folders not found; using committed markdown")
        return
    weave_count = 0
    for src in SOURCE_WEAVE_MD.glob("*.md"):
        dest = WEAVE_MD_DIR / src.name
        shutil.copy2(src, dest)
        dest.write_text(rename_plugin_mentions(dest.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
        weave_count += 1
    reader_count = 0
    for src in SOURCE_READER_MD.glob("*.md"):
        dest = READER_MD_DIR / src.name
        shutil.copy2(src, dest)
        dest.write_text(rename_plugin_mentions(dest.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
        reader_count += 1
    print(f"copied {weave_count} weave markdown -> {WEAVE_MD_DIR}")
    print(f"copied {reader_count} reader markdown -> {READER_MD_DIR}")


def english_lead(item: dict, zh_lead: str) -> str:
    if item.get("lead_en"):
        return item["lead_en"]
    en_title = item.get("title", {}).get("en", "")
    if en_title:
        return f"Step-by-step guide to {en_title}."
    return zh_lead


def append_catalog(
    tutorials: list,
    catalog: list,
    md_dir: Path,
    md_en_dir: Path | None = None,
    *,
    apply_rename: bool = True,
) -> None:
    for item in catalog:
        path = md_dir / item["file"]
        if not path.exists():
            raise SystemExit(f"Missing: {path}")
        md = path.read_text(encoding="utf-8")
        if apply_rename:
            md = rename_plugin_mentions(md)
            path.write_text(md, encoding="utf-8", newline="\n")
        lead, body = convert_markdown(md)
        lead_obj = {"zh": lead, "en": english_lead(item, lead)}
        body_obj: dict[str, str] = {"zh": body}
        if md_en_dir is not None:
            en_path = md_en_dir / item["file"]
            if en_path.exists():
                en_md = en_path.read_text(encoding="utf-8")
                if apply_rename:
                    en_md = rename_plugin_mentions(en_md)
                    en_path.write_text(en_md, encoding="utf-8", newline="\n")
                en_lead, en_body = convert_markdown(en_md)
                body_obj["en"] = en_body
                if en_lead:
                    lead_obj["en"] = en_lead
            else:
                raise SystemExit(f"Missing English translation: {en_path}")
        tutorials.append(
            {
                "id": item["id"],
                "code": item["code"],
                "plugin": item["plugin"],
                "group": item["group"],
                "level": item["level"],
                "title": item["title"],
                "lead": lead_obj,
                "body": body_obj,
                **{
                    key: item[key]
                    for key in ("created", "updated", "layout", "numberedHeadings", "badge")
                    if key in item
                },
            }
        )


def build() -> None:
    copy_sources()
    tutorials = [WELCOME, READER_WELCOME, MSTODO_WELCOME]
    append_catalog(tutorials, WEAVE_CATALOG, WEAVE_MD_DIR, WEAVE_MD_EN_DIR)
    append_catalog(tutorials, READER_CATALOG, READER_MD_DIR, READER_MD_EN_DIR)
    append_catalog(
        tutorials,
        MSTODO_CATALOG,
        MSTODO_MD_DIR,
        MSTODO_MD_EN_DIR,
        apply_rename=False,
    )
    tutorials.extend([SERIES, IR])
    payload = json.dumps(tutorials, ensure_ascii=False, indent=2)
    OUT_JS.write_text(
        "/* generated by scripts/build-tutorials.py — do not edit by hand */\n"
        "window.WEAVE_TUTORIALS = "
        + payload
        + ";\n",
        encoding="utf-8",
    )
    print(f"wrote {len(tutorials)} tutorials -> {OUT_JS}")


if __name__ == "__main__":
    build()
