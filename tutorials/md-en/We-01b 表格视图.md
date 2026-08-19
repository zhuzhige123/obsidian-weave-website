The Obsidian Weave card management interface supports table, grid, kanban, and other views. Table view suits browsing large batches of cards, property search and filtering, sorting, inline edits, and batch organization. Here is a detailed guide:

## Open Table View
After installing the plugin, open the plugin main interface. Use the top-left menu to switch to **Card Management**.

1. After entering card management, table view is usually the default. If not, choose **Table View** from the top view switcher. On desktop this is often a dropdown; on mobile, use colored dots.
2. Table view shows one card per row with front, back, status, deck, tags, priority, source document, and related fields.
3. If you have many cards, use the top search box for property matching before other operations.

> Note: Card management and deck study are different entries. Deck study focuses on spaced repetition and practice; card management focuses on viewing, filtering, editing, and organizing.

## Switch Data Source
Card management handles more than memory decks. Use **Data Source Switch** in the top-left menu to switch between database sources.

1. **Memory Decks**: everyday management and organization of memory cards.
2. **Exam Question Groups**: view and manage questions imported into exam groups—question type, accuracy, attempt count, error level, and other exam fields.
3. After switching to exam question groups, table columns lean toward exam scenarios. Column presets **Minimal**, **Exam**, and **All** quickly shift display focus.
4. In exam question group data source, the search box also supports exam property matching, e.g. `accuracy:`, `attempts:`, `error:`, `type:`.

> Note: After multi-selecting in memory decks, you can batch-add qualifying multiple-choice cards and others to exam question groups.

## Basic Info Mode and Review History Mode
In memory deck data source, table view supports two column modes.

1. Open the top-left menu and find table view sub-items.
2. Choose **Basic Info Mode**: front/back content, deck, tags, priority, source document, and other everyday management fields.
3. Choose **Review History Mode**: next review, retention, interval, difficulty, review count, and other review analytics fields.

> Note: Both modes show the same cards—only the column set changes.

## Field Management and Column Presets
Use this when you need to show table fields on demand.

1. In the card management top toolbar or top-left menu, open **Field Management** or **Column Settings**.
2. Check columns to display as needed.
3. Or use column presets directly: memory decks have **Minimal**, **Study**, **Review**, **All**; exam question groups have **Minimal**, **Exam**, **All**.
4. Drag table header edges to adjust column width; adjustments are remembered for next time.

## Property Search and Filtering
Use Obsidian-style search syntax to match card properties.

1. Click the top search box. Enter plain keywords to match card content.
2. Or use property prefixes for precise filtering. Common forms include:
   - `deck:` match deck
   - `tag:` match tag
   - `folder:` match source folder
   - `source:` match source document
   - `priority:` match priority
   - `type:` match question type
   - `status:` match study status
   - `created:` / `modified:` / `due:` filter by date
   - `yaml:` filter by YAML properties
3. In exam question group data source, also use `accuracy:`, `attempts:`, `error:` and other exam properties.
4. After typing a prefix, the plugin suggests completions you can pick.
5. Combine multiple conditions. Use `-` prefix to exclude.

> Note: Search first, then batch operations—usually steadier and faster.

## Sorting
Most column headers support click sorting.

1. Click a column header to sort by that field.
2. Click the same header again to toggle ascending and descending.

## Inline Edit Tags and Priority
Table view lets you edit tags and priority directly in cells without opening the edit modal for every card.

1. Click in the **Tags** column to add or remove tags. Press Enter to confirm.
2. Click in the **Priority** column to switch among Low, Medium, High, Urgent, etc.
3. Changes save automatically.

> Note: To edit front, back, stem, options, etc., use that row’s action menu to open the editor.

## View, Edit, and Source Jump for a Single Card
Each row has an action menu on the right.

1. Click **More** at row end to view card details, edit, or delete.
2. For memory cards, you can also **Reset to New Card**—clears review history and study progress but keeps card content.
3. If the table shows a **Source Document** column, click the name to jump. With block reference info, it tries to locate the block. Also supports jumping to linked PDF, EPUB, canvas, and other sources.

> Note: Cards live in non-Markdown `.wdeck` deck files. Source jumps depend on source info recorded on the card; cards without sources cannot be located.

## Multi-Select and Batch Operations
Table view supports multi-select. After selecting multiple cards, a batch action bar appears at the bottom.

1. Check row checkboxes for individual cards; check the header checkbox to select all in the current list.
2. Only table view supports quick swipe multi-select: long-press a row checkbox and slide up or down to select a continuous range quickly. Grid, kanban, and other views do not have this long-press swipe multi-select.
3. After selection, the bottom batch bar commonly includes: create deck, change deck, add to exam question group, add tags, remove tags, export summary to Markdown, delete, cancel selection.
4. Delete asks for confirmation. Batch delete cannot be undone.

> Note: For batch deck changes, it is safer to filter to the same source deck first, then batch operate.

## Locate-and-Jump Mode
Use this when you want to read cards while jumping back to source documents for context.

1. Enable **Locate-and-Jump Mode** in card management top bar or menu.
2. When enabled, clicking a card prioritizes jumping to its source document or trace location.
3. Turn off when done to restore normal selection and organization.

> Note: Locate-and-jump mode and linked card mode are usually mutually exclusive—enabling one turns off the other.

## Linked Card Mode and Sidebar Integration
Linked card mode works best in grid card view. After dragging card management to an Obsidian sidebar, the interface automatically switches to a cleaner sidebar mode.

1. Move card management to the left or right Obsidian sidebar.
2. Switch to grid view and enable **Linked Card Mode** or **Link Active Document**.
3. When you open notes, PDFs, EPUBs, etc. in the main content area, the sidebar can link to the active document and automatically filter cards whose sources point to that document.
4. Quickly see which memory cards, excerpt notes, and test questions came from the current document.
5. In linked card mode, clicking a card can further filter other cards linked to it.
