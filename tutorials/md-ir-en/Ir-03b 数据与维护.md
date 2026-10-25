Topics and reading points live in vault data. The plugin folder mainly holds settings and rebuildable cache. Back up the data root and every `.irdeck` first.

## Two layers
1. **Vault data** — topics, points, materials, registry — high backup priority.
2. **Plugin folder** — `data.json`, cache, state — mostly rebuildable.

## Vault data root
Default folder name: `weave Incremental reading/` (change under Settings → Basic → Data folder). Typical layout:

```
weave Incremental reading/
  points/                  # .irdeck topic files
  materials/
  registry/
  pdf-bookmark-tasks.json
  epub-bookmark-tasks.json
  IR/                      # compatibility import folder
  editor/                  # temp editor files when produced
```

`IR/` is a legacy compatibility path—use Add link or Import for day-to-day capture.

## `.irdeck` topic files
Each topic is one `.irdeck`: metadata plus a points array (schedule, trace, relations, …). Treat `.irdeck` records as the source of truth across tools.

## Plugin folder
Usually `.obsidian/plugins/weave-incremental-reading/`. Uninstall does not auto-delete vault `.irdeck` data.

## Data management and backup
Entry: Settings → Data management, or calendar More → Data management. Use it to inspect topics, unify formats, and handle duplicates. Migrate legacy Markdown point formats here—do not keep teaching legacy create paths.

Back up the whole data root (including every `.irdeck`). Confirm the old folder is ready before changing the data root path.
