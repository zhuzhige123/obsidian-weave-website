MS To Do Sync is a standalone Obsidian plugin from the same developer (not part of the Weave series, and with no code dependency on it). It connects “plan in Obsidian, execute in Microsoft To Do on your phone” as a light two-way channel: only explicitly tagged tasks sync; everything else in the vault or To Do stays untouched. Details below:

## 1. What problem it solves
1. You keep study/work lists in Markdown, but reminders and check-off work better in mobile To Do.
2. You do not want to bind an entire To Do account or every vault task—only clearly marked lines.
3. You need notes and one level of sub-steps in To Do, plus a tap that jumps back to the exact Obsidian line.

## 2. Core principles (remember these)
1. **Selective sync**: Only tasks with the sync namespace tag (default `#mtd-sync`, including sub-tags like `#mtd-sync/work`), or lines you map via **Sync current task line**.
2. **List isolation**: Reads/writes only your main Obsidian sync list and dedicated route lists; other To Do lists never inbound.
3. **No text pollution**: Machine mapping lives in inline HTML comments `<!-- mtd:… -->`, hidden in reading view; no default visible `🆔`.
4. **Standalone**: Works fully without Weave Deck / EPUB Reader / Incremental Reading.

## 3. A typical day
1. Write tagged tasks with due dates in Obsidian.
2. After save/leave note, they appear in the dedicated To Do list.
3. Check off or edit on the phone; the plugin pulls changes back on a schedule.
4. Tap the Obsidian backlink in To Do to open, locate, and briefly highlight the line.

## 4. Suggested reading order
1. New users: `Mt-01a` → `Mt-01b` → `Mt-02a`.
2. Daily use: `Mt-02b` → `Mt-02c`.
3. Advanced: `Mt-03a` → `Mt-03b` → `Mt-03c`.
4. Settings & troubleshooting: `Mt-04a`–`Mt-04c`.

> Note: Minimum Obsidian version is **1.11.4**. Source and releases: `zhuzhige123/obsidian-microsoft-todo-sync` on GitHub.
