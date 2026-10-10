MS To Do Sync 与 Weave Deck、EPUB Reader、Incremental Reading **同属一位开发者**，但**不是 Weave 系列产品包的一部分**，也**没有代码依赖**。可以单独安装使用。以下是详细介绍：

## 1. 独立意味着什么
1. 不安装任何 Weave 插件，MS To Do Sync 也能完成登录、双向同步、入站与回链。
2. 不共享 Weave 的激活码或高级支持体系；本插件按自身许可（GPL-3.0-or-later）与发行方式提供。
3. 仓库、发行包、Issues 均在独立项目：`obsidian-microsoft-todo-sync`。

## 2. 为何教程出现在 Weave 官网
1. 官网教程壳支持多个插件标签页（Deck / Reader / IR…）。
2. 本教程作为**同一开发者的独立插件文档**挂在同一站点，方便查找与中英切换。
3. 顶栏切换到 **MS To Do Sync** 即可只浏览本插件目录；与 Weave 教程互不影响。

## 3. 和阅读 / 制卡怎么配合（可选）
1. 在 EPUB Reader 或普通笔记里写出学习任务，打上 `#mtd-sync`，即可进 To Do 提醒执行。
2. Weave Deck 复卡片与 To Do 执行清单是不同场景：前者偏间隔重复，后者偏待办执行；无需强行打通。
3. 若笔记中同时使用 Tasks 查询，请遵循 `Mt-03c` 的行序约定。

## 4. 安装位置对照
| 插件 | 典型插件目录 |
|---|---|
| MS To Do Sync | `.obsidian/plugins/ms-todo-sync/` |
| Weave EPUB Reader | `.obsidian/plugins/weave-epub-reader/`（以实际 ID 为准） |
| Weave Deck | 以社区页 / manifest 为准 |

## 5. 获取帮助
1. 功能问题优先查本标签页教程与插件内设置说明。
2. 缺陷与需求请开 GitHub Issues。
3. 官网交流群 / 邮箱亦可反馈；说明你用的是 **MS To Do Sync**，避免与 Weave 功能混淆。
