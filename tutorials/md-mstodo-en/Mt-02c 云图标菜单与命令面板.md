Besides auto-sync, you can push/pull a single line or the whole vault manually. The cloud icon is for per-task actions; the command palette covers batch and today/reminder actions. Details below:

## 1. Cloud icon menu
On a tagged or mapped task, open the cloud menu (exact UI depends on view mode). Common items:

1. **Push** current line to Microsoft To Do.
2. **Pull** fields for that task from To Do.
3. **Open in To Do** when a remote mapping exists.
4. **Copy Obsidian task link** (`obsidian://mtd-sync?…`).
5. **Stop syncing** (unlink locally; optional remote backlink cleanup per settings).

> Note: Stop sync does not delete the To Do task by default; delete remotely in To Do if needed.

## 2. Common commands
Search the command palette for “MS To Do” / “sync”. Typical commands:

1. **Sync all tagged tasks**
2. **Sync tasks in current note**
3. **Sync current task line**
4. **Pull remote task changes**
5. **Add to today (due + myday)** and reminder commands

> Note: Labels follow the UI language (English / 中文).

## 3. Auto-sync timing
Under **General → Auto sync**:

1. **On leave note** (default-friendly): fewer mid-typing pushes.
2. **After idle delay**: push N seconds after you stop typing.
3. **Manual only**: commands and cloud icon only.

Also: sync after login, tag-line delay, pull interval (minutes), notify on auto sync.

## 4. Recommended habits
1. Tag and date first, then leave the note so auto-sync can run.
2. After important phone edits, pull once in Obsidian to confirm.
3. For a single bad line, use cloud push/pull before a full-vault sync.
