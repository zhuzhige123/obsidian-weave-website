Install the plugin into the current vault, then sign in through Microsoft’s official page. Only after a successful login can Obsidian push and pull tasks via Microsoft Graph. Details below:

## 1. Community install (recommended)
1. Open Obsidian **Settings → Community plugins → Browse**.
2. Search for **MS To Do Sync**, install and enable it.
3. After enabling, a ribbon icon may appear; you can also find Microsoft To Do commands in the command palette.

> Note: If it is not listed yet, use manual install below. Display name follows the marketplace and `manifest.json`.

## 2. Manual install
1. From [GitHub Releases](https://github.com/zhuzhige123/obsidian-microsoft-todo-sync/releases), download the package matching the version and get `main.js`, `manifest.json`, and `styles.css`.
2. Copy them into `.obsidian/plugins/ms-todo-sync/` (same folder, matching versions).
3. Restart Obsidian and enable **MS To Do Sync** under **Settings → Community plugins**.

## 3. Sign in with Microsoft
1. Open **Settings → MS To Do Sync → Account**.
2. Click **Sign in**. The browser opens Microsoft’s login page.
3. Finish authorization; you should return to Obsidian with a “Connecting…” style notice.
4. When successful, the Account tab shows connected status (and possibly the account name).

> Note: “Please finish signing in in the browser, then return to Obsidian” is **not an error**—the browser flow is in progress. Use **Login help** in settings for common issues.

## 4. Login troubleshooting
1. **Browser OK, Obsidian silent**: Keep Obsidian open; do not restart or switch vault mid-login; try Edge/Chrome; switch back to Obsidian after login.
2. **net::ERR_FAILED**: Often network, VPN, proxy, or firewall blocking token exchange. Switch network, toggle VPN, or try a phone hotspot; some antivirus (e.g. corporate ESET) may also block—allow temporarily and retry.
3. **Microsoft maintenance page**: Microsoft-side outage; retry later.
4. **Missing PKCE / need to sign in again**: Obsidian was closed or the vault changed mid-flow—sign in again in one continuous pass.
5. **Personal Microsoft account**: Keep Azure tenant `common`; leave client ID empty to use the built-in app.

## 5. Sign out
1. Click **Sign out** on the Account tab.
2. Tokens are cleared from local `secretStorage`; Markdown task lines are not deleted.
3. On a new device, sign in again (index can rebuild from inline `mtd:id`).
