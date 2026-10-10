Besides vault → To Do, you can create tasks in managed To Do lists and have the plugin write them into the vault. Sub-tag routes send different tags to different lists and default notes. Details below:

## 1. Inbound capture (To Do → vault)
1. Only tasks created in the **main sync list** or **dedicated route lists** inbound.
2. Tasks in other To Do lists are **never** pulled in.
3. Inbound lines get the sync tag, an `mtd:id`, and a mapping.

## 2. Default landing path
1. Main list: **Default inbound note for main list** (e.g. `Microsoft To Do/Inbox.md`).
2. Route lists: the “To Do → Obsidian (default note)” column for that row.
3. Missing files can be created (including parent folders).

## 3. Target a note from the To Do body (optional)
On managed lists only, write in the To Do notes field:

1. First line: `[[Note path or name#Heading]]` or `page: [[Note#Heading]]`
2. Next line: `---`
3. Then the real note body

Without a locator, the list default note is used. Enable **Strip inbound route header** to remove the locator from To Do after capture.

## 4. Dedicated sync lists (sub-tag routes)
Open **General → Dedicated sync lists (sub-tag routes)**. Each row is a two-way channel:

| Column | Meaning |
|---|---|
| Obsidian → To Do (sub-tag) | e.g. `#mtd-sync/nursing` (must be a sub-tag under the namespace) |
| Dedicated To Do list | List name in Microsoft To Do |
| To Do → Obsidian (default note) | Vault path for inbound defaults |

1. Click **New**, fill fields, then **Save** on the row.
2. Vault tasks with that sub-tag push to the matching list.
3. New tasks in that list without a page locator land in the default note.

> Note: Namespace-only tags are invalid; do not map the same sub-tag or To Do list twice. Save after edits.

## 5. Tips
1. Personal inbox: main list + one default note is enough.
2. Split by course/project with routes when lists get crowded.
3. Put template folders in **Excluded folders** so sample `#mtd-sync` lines are not pushed.
