After sync, you can open Obsidian from Microsoft To Do, jump to the task line, and briefly highlight it. This relies on a stable inline `mtd:id` and optional deep-link attachment. Details below:

## 1. Enable backlink-related settings
Under **General → To Do links**, optionally enable:

1. **Append Obsidian backlink in To Do notes**: adds an `obsidian://mtd-sync?…` block at the end of the body.
2. **Create linked resource in To Do**: shows an Obsidian entry in linked resources (depends on Graph / To Do client).

## 2. What the deep link looks like
Typical form (parameters as generated):

```text
obsidian://mtd-sync?vault=YourVault&file=path&task=mtd-xxxxxxxx
```

1. `task` matches the inline `mtd:id=` value.
2. The plugin opens the file, scans for `mtd:id`, scrolls to the line, and flashes a highlight (source / Live Preview / reading view).

## 3. Open from To Do
1. Tap the note link or linked-resource entry in To Do (desktop or mobile).
2. Obsidian should launch; keep the correct vault open and matching the `vault` parameter.
3. On success, the task line is located and briefly highlighted.

## 4. Copy the link in Obsidian
1. Use the cloud menu **Copy Obsidian task link**.
2. Paste into other notes, calendars, or bookmarks.
3. If copy/open fails, confirm the line already has an `mtd:id` (synced at least once).

## 5. If it does not open
1. Is Obsidian running on the correct vault?
2. Does the line still contain the same `mtd:id` (moved files are usually found via vault scan)?
3. Does the OS allow `obsidian://` handlers (desktop is usually more reliable)?
4. If backlink append is off, To Do notes may lack a link—use **Copy link** to verify mapping.
