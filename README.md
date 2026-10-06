# Obsidian Weave 官网

Weave 插件系列的静态官网。

## 在线访问（正式入口）

**https://obsidian-weave.xyz/**

请统一使用上述 HTTPS 地址对外宣传、插件内跳转与外链。  
`https://zhuzhige123.github.io/obsidian-weave-website/` 会由 GitHub Pages 跳转到正式域名。

### 自定义域名（GitHub Pages）

仓库根目录的 `CNAME` 文件内容必须是：

```
obsidian-weave.xyz
```

DNS（阿里云万网）需要同时具备：

| 记录类型 | 主机记录 | 记录值 |
|------|------|------|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |
| CNAME | `www` | `zhuzhige123.github.io` |

AAAA（IPv6）建议补齐，否则 GitHub 有时迟迟签不出 HTTPS 证书。

绑定后打开 **Settings → Pages**：

1. Custom domain 显示 `obsidian-weave.xyz`
2. 等待 DNS check 通过
3. 证书就绪后勾选 **Enforce HTTPS**

### 让搜索引擎收录（需你本人操作一次）

1. 打开 [Google Search Console](https://search.google.com/search-console)
2. 添加资源：网址前缀 `https://obsidian-weave.xyz/`
3. 按提示完成所有权验证
4. 提交站点地图：`https://obsidian-weave.xyz/sitemap.xml`
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
