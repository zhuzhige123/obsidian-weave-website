# Element: Weave 插件 Logo（交织斜条标记）

> Source: `C:\Users\lihua\Desktop\插件logo.png`（1024×1024 RGBA）  
> Kind: **`hybrid`**（几何结构可用 SVG 重建；当前官网用栅格资产落地）  
> 用途：官网顶栏 mark、favicon、品牌规范参考  
> 官网落点：`obsidian-weave-website/assets/brand/`

---

## 一句话

黑底上的双色斜条交织符：青绿与暖米交替穿插，形成可读作 **W / 双 X / 编织** 的中心徽标，直接对应产品名「Weave」。

---

## Tokens

| Token | Value | Notes |
|-------|-------|-------|
| `color.bg` | `#101010` | 近纯黑画布（采样主色，非纯 `#000`） |
| `color.stroke.teal` | `#188090` | 中饱和青绿条 |
| `color.stroke.cream` | `#E8E0D0` | 暖米/象牙条 |
| `color.mix.edge` | `#787068` / `#104850` | 抗锯齿边缘混色，重建时勿当品牌色 |
| `geometry.angle` | ≈ 45° | 两族对角线 |
| `geometry.barWidth` | 约画布 12–14% | 四条等宽粗条 |
| `geometry.ends` | 水平裁切 | 顶/底边缘齐平，非尖角 |
| `geometry.center` | 菱形负形 | 中心黑色空隙 |
| `style` | Flat, no gradient / shadow / texture | 现代几何标 |

---

## Structure（可读成）

1. **画布**：正方形，满铺深色底。  
2. **四条粗斜条**：两族方向（↘ 与 ↗），青绿与暖米交替。  
3. **编织层叠**：故意「上压下」穿插，形成织纹，而非单纯交叉线。  
4. **外轮廓**：整体落在正方形安全区内，四周留黑边，适合当 App/插件方标。

语义映射：

- **Weave** → 交织穿插  
- **Obsidian 深色生态** → 黑底 + 冷静青绿  
- **纸质/阅读气质** → 暖米第二条色（不是冷白）

---

## 官网适配结论

| 问题 | 结论 |
|------|------|
| 能否上官网？ | **能。** 已接入真仓 `obsidian-weave-website` |
| 顶栏 | 文字「Weave 系列」前增加方标图 |
| Favicon | 已用缩小 PNG（32/48/64/180） |
| 注意 | 官网字标强调色仍是**紫色**（`--accent: #a68cf5`），与 logo 青绿不同系；短期可并存（图=织纹身份，紫=站点点缀），长期若要统一品牌，需另开一轮「字标强调色是否改青绿」的产品决定 |

---

## 资产清单（已生成）

路径根：`obsidian-weave-website/assets/brand/`

| 文件 | 用途 |
|------|------|
| `weave-mark.png` | 原图 1024（分享/高清） |
| `weave-mark-256.png` / `weave-mark-128.png` | 顶栏与中尺寸 |
| `favicon.png` / `favicon-32.png` / `favicon-48.png` | 浏览器图标 |
| `apple-touch-icon.png` | iOS 主屏 |

HTML 已改：`index.html`、`tutorials.html`、`privacy.html`、`terms.html`。

---

## Reconstruction notes

### A. 栅格用法（当前）

- 顶栏：`weave-mark-128.png`，约 26–28px，圆角 5–6px，细描边与深色顶栏分离。  
- 勿在浅色主题下直接铺黑底大方块而不加描边——会显得发脏；当前站点默认深色，黑底方标自然。

### B. SVG 重建提示（后续可选，更利小尺寸）

用 4 个平行四边形 / `polygon`，青绿与暖米交替，靠 **图层顺序 + clipPath** 做「上压下」穿插；中心留菱形透明/黑色洞。  
不要用描边描出交叉——要用面填充 + 遮挡，否则织感会假。

### C. 生成式复刻 prompt（isolated）

```text
PALETTE: background #101010, bar A #188090 teal, bar B #E8E0D0 warm cream
SUBJECT: square app icon, four thick equal-width diagonal bars woven over-under like a braid, reading as a stylized W / double-X weave mark, flat ends cropped horizontally top and bottom, diamond-shaped black negative space in the exact center
STYLE: flat vector logo, sharp edges, no gradients, no shadows, no texture, no text, no glow
FORMAT: isolated single subject, square 1024, full-bleed black canvas matching #101010, generous but tight safe margin inside square
```

---

## Do / Don't

- **Do** 保持青绿 + 暖米双色；不要改成站点紫去「硬统一」除非产品明确换色。  
- **Do** 小尺寸优先用已缩放 PNG 或未来 SVG，避免每次塞 1024 原图。  
- **Don't** 加光晕、渐变、立体挤出。  
- **Don't** 把抗锯齿灰边当成第三品牌色。
