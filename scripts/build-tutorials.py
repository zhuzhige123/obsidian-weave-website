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
    "Er-01a 安装与打开书架": "reader-install-shelf",
    "Er-01b 阅读器界面与阅读模式": "reader-ui-modes",
    "Er-01c 书签、进度与参考阅读点": "reader-bookmarks-progress",
    "Er-02a 摘录笔记工作流": "reader-excerpt-workflow",
    "Er-02b 高亮、想法与样式标注": "reader-highlights",
    "Er-02c 摘录汇总与时间线": "reader-excerpt-timeline",
    "Er-02d 双向溯源与正文回显": "reader-bidirectional",
    "Er-02e Canvas 脑图摘录": "reader-canvas-excerpt",
    "Er-02f 截图摘录": "reader-screenshot-excerpt",
    "Er-03a 段落阅读与沉浸式全屏": "reader-paragraph-immersive",
    "Er-03b 生词标注与词汇表": "reader-vocabulary",
    "Er-03c 目录标记与全书地图": "reader-toc-map",
    "Er-03d 书架书单": "reader-bookshelf-lists",
    "Er-03e 脚注与隐藏文本": "reader-footnotes",
    "Er-04a 导出笔记与模板": "reader-export-templates",
    "Er-04b 阅读器设置与数据同步": "reader-settings-sync",
    "Er-04c 与 Weave 制卡、增量阅读、AI 联动": "reader-weave-integration",
    "Er-04d 高级支持、隐私与常见问题": "reader-faq",
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
    if local.exists():
        return (
            f'<figure class="figure"><img src="assets/tutorials/{esc(name)}" alt="" />'
            f"<figcaption>{esc(name)}</figcaption></figure>"
        )
    return (
        f'<figure class="figure is-placeholder"><div class="ph">Screenshot · {esc(name)}</div>'
        f"<figcaption>Place image at assets/tutorials/{esc(name)}</figcaption></figure>"
    )


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
            if is_first and not lead and not stripped.startswith("#"):
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
            html_parts.append(
                f'<pre><code class="lang-{esc(lang)}">{esc(code.rstrip())}</code></pre>'
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
<article class="path-card"><h4>第一次打开</h4><p>安装插件，把书放进书架。</p><a href="#reader-install-shelf" data-goto="reader-install-shelf">安装与打开书架</a></article>
<article class="path-card"><h4>边读边记</h4><p>摘录写入笔记并跳回原文。</p><a href="#reader-excerpt-workflow" data-goto="reader-excerpt-workflow">摘录工作流 → 双向溯源</a></article>
<article class="path-card"><h4>英文原著</h4><p>生词标注与词汇表。</p><a href="#reader-vocabulary" data-goto="reader-vocabulary">生词标注与词汇表</a></article>
</div>
<h3>Er-01～Er-04 怎么读</h3>
<p><strong>Er-01</strong> 入门与界面；<strong>Er-02</strong> 摘录与高亮；<strong>Er-03</strong> 阅读增强；<strong>Er-04</strong> 导出、设置与系列联动。正文来自产品库 <code>obsidian weave epub reader 教程</code>。</p>""",
        "en": """<div class="path-cards">
<article class="path-card"><h4>First open</h4><p>Install and add books.</p><a href="#reader-install-shelf" data-goto="reader-install-shelf">Install & bookshelf</a></article>
<article class="path-card"><h4>Read & excerpt</h4><p>Notes with bidirectional links.</p><a href="#reader-excerpt-workflow" data-goto="reader-excerpt-workflow">Excerpt workflow</a></article>
</div>
<p>Er-01 setup, Er-02 excerpts, Er-03 reading features, Er-04 export & integration.</p>""",
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


def copy_sources() -> None:
    WEAVE_MD_DIR.mkdir(parents=True, exist_ok=True)
    READER_MD_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    if not SOURCE_WEAVE_MD.exists() or not SOURCE_READER_MD.exists():
        print("skip copy: product-library source folders not found; using committed markdown")
        return
    weave_count = 0
    for src in SOURCE_WEAVE_MD.glob("*.md"):
        shutil.copy2(src, WEAVE_MD_DIR / src.name)
        weave_count += 1
    reader_count = 0
    for src in SOURCE_READER_MD.glob("*.md"):
        shutil.copy2(src, READER_MD_DIR / src.name)
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
) -> None:
    for item in catalog:
        path = md_dir / item["file"]
        if not path.exists():
            raise SystemExit(f"Missing: {path}")
        md = path.read_text(encoding="utf-8")
        lead, body = convert_markdown(md)
        lead_obj = {"zh": lead, "en": english_lead(item, lead)}
        body_obj: dict[str, str] = {"zh": body}
        if md_en_dir is not None:
            en_path = md_en_dir / item["file"]
            if en_path.exists():
                en_md = en_path.read_text(encoding="utf-8")
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
            }
        )


def build() -> None:
    copy_sources()
    tutorials = [WELCOME, READER_WELCOME]
    append_catalog(tutorials, WEAVE_CATALOG, WEAVE_MD_DIR, WEAVE_MD_EN_DIR)
    append_catalog(tutorials, READER_CATALOG, READER_MD_DIR, READER_MD_EN_DIR)
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
