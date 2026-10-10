The plugin parses Tasks-style emoji fields on the task line and maps them to Microsoft To Do. Stable syntax keeps dates, priority, and completion two-way. Details below:

## 1. Minimal syncable line
```markdown
- [ ] Buy milk #mtd-sync
```

After save/sync, an inline machine comment appears (hidden in reading view), e.g.:

```markdown
- [ ] Buy milk #mtd-sync <!-- mtd:id=mtd-xxxxxxxx -->
```

With dates or priority, the comment sits **near tags, before Tasks emojis**:

```markdown
- [ ] Buy milk #mtd-sync <!-- mtd:id=mtd-xxxxxxxx --> 📅 2026-06-20
```

> Note: Placement keeps Obsidian Tasks happy (Tasks reads from the end of the line). Do not delete `mtd:id` or the mapping breaks.

## 2. Field map

| In Obsidian | In Microsoft To Do |
|---|---|
| `#mtd-sync` (or your namespace) | Eligible; `#tag/subtag` can route |
| `📅 2026-06-20` (optional time) | Due date |
| `⏳ 2026-06-18` | Scheduled (Tasks) → To Do start |
| `🛫 2026-06-18` | Start (Tasks; parsed) |
| `⏫` / `🔼` / `🔽` | High / normal / low importance |
| `- [/]` | In progress |
| `- [x]` | Completed |

## 3. Complete vs delete
1. **Complete** in To Do → Obsidian becomes `- [x]`; line is **not** deleted by default.
2. **Permanently delete** in To Do → follows the deletion policy setting (delete line / unlink / keep).

## 4. In progress
1. Use checkbox `- [/]` for in progress.
2. Maps to To Do in-progress status (per current field mapping).

## 5. What to avoid
1. Do not append free text after emoji metadata (Tasks stops parsing).
2. Do not put the sync tag on non-task lines.
3. Do not hand-edit `mtd:id`; use the cloud menu or commands to stop sync.
