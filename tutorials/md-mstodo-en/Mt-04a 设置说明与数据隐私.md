Settings are split into **General / Account / About**. UI language can follow Obsidian or stay English/中文. This article explains what to change and where data lives. Details below:

## 1. UI language
1. **General → Interface**: Auto / English / 中文.
2. Affects this plugin’s settings and some notices, not your note language.

## 2. Sync scope and routes
See `Mt-01b` and `Mt-03a`: namespace, main list, inbound default note, excluded folders, sub-tag route table.

## 3. Auto sync and remote pull
1. **Auto-sync timing**: leave note / idle delay / manual only.
2. **Idle delay & tag-line delay**: fewer mid-typing pushes.
3. **Sync after login**: push soon after connecting.
4. **Pull interval (minutes)**: how often To Do changes are fetched.
5. **Notify on auto sync**: toast when background push succeeds.

## 4. To Do links and deletion policy
1. Note backlinks, linked resources, cleanup on unlink.
2. Strip inbound route headers from To Do after capture.
3. **When a task is permanently deleted in To Do**: delete Obsidian line / unlink only / keep—unrelated to “complete”.

## 5. Account and advanced
1. **Sign in / Sign out**; **Login help** for common failures.
2. **Advanced**: Azure client ID and tenant. Personal accounts usually keep tenant `common` and empty client ID.

## 6. Where data lives
1. **Good to sync with the vault**: Markdown tasks, notes, subtasks.
2. **Plugin dir / secretStorage** (usually not hand-copied): tokens, sync index. Sign in again on a new device.
3. **Network**: only mapped task fields via Microsoft Graph; the whole vault is **not** uploaded.

> Note: Full privacy terms live in the plugin repository. Never commit secrets, `.env`, or refresh tokens to public git.

## 7. About tab
1. Name, version, plugin ID (`ms-todo-sync`).
2. Docs, issues, email links.
