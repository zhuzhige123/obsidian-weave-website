After login, confirm **what syncs and where**, then write your first tagged task. Correct scope prevents template scans and wrong lists. Details below:

## 1. Open sync scope
1. Open **Settings → MS To Do Sync → General**.
2. Find the **Sync scope** group.

## 2. Sync namespace (tag)
1. Default namespace is `mtd-sync` (write `#mtd-sync` on the task line).
2. Tasks with `#mtd-sync` or `#mtd-sync/subtag` are eligible.
3. In settings, enter the name **without `#`**; sub-tags under the namespace match.

> Note: Untagged tasks never sync. Use **Sync current task line** to tag and map a single line.

## 3. Main Obsidian sync list
1. Setting **Obsidian main sync list**: the Microsoft To Do list name (often `Obsidian Sync`).
2. Only this list and dedicated route lists participate in inbound capture.
3. Ensure the list exists in To Do, or allow the plugin to use/create it by name (per current version behavior).

## 4. Default inbound note for the main list
1. Set **Default inbound note for main list**, e.g. `Microsoft To Do/Inbox.md`.
2. New tasks in the main list without a page locator append to that note (created if missing).

## 5. Excluded folders (optional)
1. Add template folders under **Excluded folders**.
2. Markdown there is **not** scanned for sync tags, so sample tasks are not pushed.

## 6. First task checklist
1. In any note, write for example:

```markdown
- [ ] Review chapter 3 #mtd-sync 📅 2026-06-20
```

2. Save, or let auto-sync run on leave/idle; or run **Sync tasks in current note**.
3. Open Microsoft To Do and confirm the task in the main sync list.
4. Check it off in To Do, then wait for pull or run **Pull remote task changes**—the line should become `- [x]`.

> Note: For the first run, push manually once to confirm the channel before relying on auto-sync.
