# Obsidian Weave 官网

Weave 插件系列的静态官网（单页）。

## 在线访问

启用 GitHub Pages 后地址一般为：

`https://zhuzhige123.github.io/obsidian-weave-website/`

（仓库名若不同，以实际仓库为准。）

## 本地预览

在本目录启动任意静态服务器，例如：

```bat
python -m http.server 8765
```

然后打开 `http://127.0.0.1:8765/`

## 内容说明

| 文件 | 说明 |
|------|------|
| `index.html` | 正式首页（Obsidian 气质版）；顶栏「教程」可切换至教程界面 |
| `tutorials.html` | 教程界面原型（侧栏目录 + 正文 + 本页目录） |
| `tutorials-data.js` | 由教程 Markdown 生成的正文数据，勿手改 |
| `tutorials/md/` | 从产品库迁入的 Weave 主插件教程稿 |
| `tutorials/md-reader/` | 从产品库迁入的 EPUB Reader 教程稿 |
| `scripts/build-tutorials.py` | 从上述 Markdown 生成 `tutorials-data.js` |
| `scripts/build-tutorials.py` | 把 Markdown 转成 `tutorials-data.js` |
| `tech.html` | 科技风备选页 |
| `uploads/` | 产品截图占位（放入同名 png 即可显示） |
| `assets/` | 辅助资源 |

支持：深浅色切换、中英切换、B 站 / YouTube 幻灯片嵌入。

## GitHub Pages 设置

1. 打开仓库 **Settings → Pages**
2. Source 选 **Deploy from a branch**
3. Branch 选 **main**，文件夹选 **/ (root)**
4. 保存后等待 1–2 分钟即可访问

如需自定义域名，在 Pages 设置里填写域名，并添加 `CNAME` 文件。
