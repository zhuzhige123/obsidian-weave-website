# Obsidian Weave 官网

Weave 插件系列的静态官网。

## 在线访问（正式入口）

**https://zhuzhige123.github.io/obsidian-weave-website/**

请统一使用上述 HTTPS 地址对外宣传、插件内跳转与外链。

### 自定义域名说明（obsidian-weave.xyz）

DNS 已指向 GitHub Pages，但 **HTTPS 证书尚未签发**，强行绑定会导致：

- `github.io` 被 301 到 `http://obsidian-weave.xyz/`
- `https://obsidian-weave.xyz/` 证书错误，搜索引擎难以收录

因此仓库已暂时移除 `CNAME`，优先保证可被搜索的 HTTPS 主站。

证书就绪后可再启用自定义域名：

1. 在仓库根目录重新添加内容为 `obsidian-weave.xyz` 的 `CNAME` 文件并推送
2. 打开 **Settings → Pages**，等待域名旁显示 DNS check 通过
3. 勾选 **Enforce HTTPS**（若提示证书不存在，再等数小时后重试）
4. 确认 `https://obsidian-weave.xyz/` 可打开后，再把全文链接与 `sitemap.xml` / `robots.txt` 改成该域名

### 让搜索引擎收录（需你本人操作一次）

1. 打开 [Google Search Console](https://search.google.com/search-console)
2. 添加资源：网址前缀 `https://zhuzhige123.github.io/obsidian-weave-website/`
3. 按提示完成所有权验证
4. 提交站点地图：`https://zhuzhige123.github.io/obsidian-weave-website/sitemap.xml`
5. 可选：用「网址检查」请求编入索引首页与 `tutorials.html`

Bing 可到 [Bing Webmaster Tools](https://www.bing.com/webmasters) 做同样提交。

## 本地预览

在本目录启动任意静态服务器，例如：

```bat
python -m http.server 8765
```

然后打开 `http://127.0.0.1:8765/`

## 内容说明

| 文件 | 说明 |
|------|------|
| `index.html` | 正式首页；顶栏「教程」可切换至教程界面 |
| `tutorials.html` | 教程页（侧栏目录 + 正文 + 本页目录） |
| `robots.txt` / `sitemap.xml` | 搜索引擎抓取与站点地图 |
| `tutorials-data.js` | 由教程 Markdown 生成的正文数据，勿手改 |
| `tutorials/md/` | Weave Deck 教程稿 |
| `tutorials/md-reader/` | EPUB Reader 教程稿 |
| `scripts/build-tutorials.py` | 从 Markdown 生成 `tutorials-data.js` |
| `uploads/` | 产品截图 |
| `assets/` | 品牌与辅助资源 |

支持：深浅色切换、中英切换、B 站 / YouTube 幻灯片嵌入。

## GitHub Pages 设置

1. 打开仓库 **Settings → Pages**
2. Source 选 **Deploy from a branch**
3. Branch 选 **main**，文件夹选 **/ (root)**
4. 保存后等待 1–2 分钟即可访问
