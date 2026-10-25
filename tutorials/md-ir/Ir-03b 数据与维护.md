阅读点与专题的真相来源在 Vault 数据里；插件目录主要存设置与可重建的缓存。备份与同步时请优先保护数据根与全部 `.irdeck` 文件。

## 两层存储
1. **Vault 数据**：专题、阅读点、材料与注册信息等——高优先级备份。
2. **插件目录**：`data.json` 设置、cache、state——多数可重建。

## Vault 数据根
默认文件夹名为 `weave Incremental reading/`，可在设置 → 基础 → 数据文件夹中修改。典型结构：

```
weave Incremental reading/
  points/                  # .irdeck 专题文件
  materials/
  registry/
  pdf-bookmark-tasks.json
  epub-bookmark-tasks.json
  IR/                      # 兼容用导入目录
  editor/                  # 临时编辑文件（若产生）
```

`IR/` 为历史兼容路径；日常收录请走添加链接或导入阅读材料。

## .irdeck 专题文件
每个专题是一份 `.irdeck`：包含专题元数据与 points 数组（调度、溯源、关联等）。跨工具协作时，应以 `.irdeck` 中的记录为唯一真相。

## 插件目录
路径通常为 `.obsidian/plugins/weave-incremental-reading/`。卸载插件不会自动删除 Vault 内已创建的 `.irdeck` 与阅读点数据。

## 数据管理与备份
入口：设置 → 数据管理，或日历更多 → 数据管理。用于专题巡检、格式统一、重复处理等。若仍有旧版 Markdown 阅读点格式，请在此统一 / 迁移，不要继续按旧格式新建。

备份请包含整个数据根（含全部 `.irdeck`）。更改数据根路径前，确认旧目录内容已就绪。
