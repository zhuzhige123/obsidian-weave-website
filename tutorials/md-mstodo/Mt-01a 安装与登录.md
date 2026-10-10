先把插件装进当前库，再用微软官方页面完成登录。登录成功后，Obsidian 才能向 Microsoft Graph 推送与拉取任务。以下是详细介绍：

## 1. 社区插件安装（推荐）
1. 打开 Obsidian **设置 → 社区插件 → 浏览**。
2. 搜索 **MS To Do Sync**，安装并启用。
3. 启用后，左侧功能区可能出现同步相关图标；也可在命令面板搜索「Microsoft To Do」相关命令。

>备注：若市场尚未收录，请用下方「手动安装」。插件显示名以市场与 `manifest.json` 为准。

## 2. 手动安装
1. 从 [GitHub Releases](https://github.com/zhuzhige123/obsidian-microsoft-todo-sync/releases) 下载与版本号一致的发布包，取得 `main.js`、`manifest.json`、`styles.css`。
2. 复制到库目录 `.obsidian/plugins/ms-todo-sync/`（三个文件同一文件夹，版本互相匹配）。
3. 重启 Obsidian，在 **设置 → 社区插件** 中启用 **MS To Do Sync**。

## 3. 登录微软账户
1. 打开 **设置 → MS To Do Sync → 账户**。
2. 点击 **登录**。浏览器会打开微软官方登录页。
3. 在浏览器中完成授权后，应自动跳回 Obsidian，并出现「正在连接…」之类提示。
4. 成功后，账户页显示已连接（可能显示账户名）。

>备注：提示「请在浏览器中完成登录，然后返回 Obsidian」**不是报错**，表示浏览器流程进行中。设置里有 **登录帮助**，可对照常见问题。

## 4. 登录排错（常见）
1. **浏览器成功但 Obsidian 无反应**：保持 Obsidian 打开，勿中途重启或换库；尝试 Edge/Chrome；登录后手动切回 Obsidian。
2. **net::ERR_FAILED**：多为网络、VPN、代理或防火墙拦截令牌交换。可切换网络、开关 VPN，或用手机热点重试；部分杀毒软件（如企业版 ESET）也可能拦截，可临时放行后再试。
3. **微软站点维护页**：属微软侧问题，稍后重试。
4. **缺少 PKCE / 需重新登录**：登录中途关闭了 Obsidian 或切换了库，请重新点「登录」并一次完成。
5. **个人微软账户**：高级设置里 Azure 租户保持 `common`；客户端 ID 可留空使用内置应用。

## 5. 退出登录
1. 在 **账户** 页点击 **退出登录**。
2. 令牌会从本机 `secretStorage` 清除；库内 Markdown 任务行不会因此被删除。
3. 换设备或重装后，重新登录即可继续同步（索引可按行内 `mtd:id` 重建）。
