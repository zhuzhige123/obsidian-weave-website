MS To Do Sync does **not** hard-depend on Obsidian Tasks, but it parses Tasks-style date and priority emojis. If you also use Tasks for queries and boards, watch the order of tokens on the line. Details below:

## 1. Why the comment must not follow emojis
Tasks reads metadata **backwards from the end** of the line and stops at unknown tokens. This breaks:

```markdown
- [ ] Fix sink #GTD/home 🔽 🛫 2026-09-28 <!-- mtd:id=mtd-xxx -->
```

Dates like `🛫` / `📅` may not match Tasks queries.

## 2. Compatible order used by this plugin
On write-back, the machine comment is placed **after title/tags and before Tasks emojis**:

```markdown
- [ ] Fix sink #GTD/home <!-- mtd:id=mtd-xxx --> 🔽 🛫 2026-09-28
```

1. Tasks can still read dates/priority from the end.
2. This plugin still parses `mtd:` comments by regex.
3. Legacy trailing comments migrate on the next sync write-back.

## 3. Emoji meanings (aligned with Tasks)
1. `📅` due
2. `⏳` scheduled (mapped to To Do start by default)
3. `🛫` start (parsed)
4. `⏫` `🔼` `🔽` priority

> Note: Prefer this tutorial / Tasks semantics over any README that loosely calls `⏳` “start date”.

## 4. Practical tips
1. Keep dates/priority toward the end; do not append free text after them.
2. Tags may appear after emojis (Tasks allows that); plugin write-back usually keeps tags before the comment.
3. Verify with Tasks queries such as `has due date` / `starts on or before today` after sync.
4. Do not hand-delete `<!-- mtd:… -->`; use the plugin menu to stop sync.

## 5. Without Tasks installed
1. Sync still works; this plugin parses emoji fields itself.
2. Tasks-only boards/queries are unavailable, but To Do two-way sync is unaffected.
