If push/pull/login misbehaves, start here. Most cases are tags, list names, network, or Tasks line order. Details below:

## 1. Task not showing in To Do?
1. Sync tag present (default `#mtd-sync`)?
2. Signed in?
3. Main list name matches To Do?
4. File inside an **excluded folder**?
5. Try **Sync tasks in current note** or **Sync all tagged tasks**.

## 2. Will all my To Do tasks sync in?
**No.** Only the main sync list and dedicated route lists inbound.

## 3. I completed a task in To Do—what happens?
The line becomes `- [x]`. Completing does not delete the line by default. Permanent delete uses the deletion policy.

## 4. Can I sync everything without tags?
**No.** Use **Sync current task line** for one-off lines.

## 5. My Day support?
No Graph API. Use **Add to today (due + myday)** or a `myday` marker.

## 6. Obsidian link from To Do does nothing?
See `Mt-03b`: Obsidian open, vault name match, `mtd:id` still on the line. Use **Copy Obsidian task link** to verify.

## 7. Tasks queries miss dates?
See `Mt-03c`: comment must be **before** emojis. Sync once to migrate legacy trailing comments.

## 8. Login failed?
See `Mt-01a` and in-settings **Login help**. Corporate antivirus/proxies can block token exchange—allow temporarily and retry.

## 9. Plugin folder name?
Plugin ID: `ms-todo-sync` → `.obsidian/plugins/ms-todo-sync/`.

## 10. Feedback
1. GitHub Issues: `zhuzhige123/obsidian-microsoft-todo-sync`
2. About-tab email / community links (same developer channels as Weave site; feature is independent)
