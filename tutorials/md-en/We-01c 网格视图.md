The Obsidian Weave card management interface supports table, grid, kanban, and other views. Grid card view suits browsing content as a card wall, multi-select organization, and placing in an Obsidian sidebar alongside the active document for linked viewing. Here is a detailed guide:

## Open Grid View
After installing the plugin, open the plugin main interface. Use the top-left menu to switch to **Card Management**.

1. After entering card management, choose **Grid View** from the top view switcher. On desktop this is often a dropdown; on mobile, use colored dots.
2. Grid view renders each card as a browsable content tile rather than a table row.
3. The top bar still supports property search filtering, e.g. `deck:`, `tag:`, `source:`.

## Switch Data Source
Grid view also supports switching data sources.

1. Use the top-left menu or top data source button to switch between **Memory Decks** and **Exam Question Groups**.
2. **Memory Decks** suit browsing everyday memory card content.
3. **Exam Question Groups** suit browsing questions imported for exams; card property badges in the top-left can show accuracy and other exam info.

## Three Grid Layouts
Grid view includes three layouts—switch in **Grid Layout** in the top-left menu or via top layout buttons.

1. **Fixed Layout**: more uniform card height, steady browsing rhythm, usually better performance. Recommended when you have many cards.
2. **Masonry Layout**: cards flow by content height—good when card lengths vary widely.
3. **Timeline View**: groups cards by time—good for reviewing cards chronologically. This may be an advanced feature.

> Note: Switching layouts changes display only—not card content.

## Top-Left Card Property Display
Each grid card can show one auxiliary property in the top-left corner.

1. Open the **Card Property** menu.
2. Choose none, or show: unique identifier, source document, priority, retention, modified time, accuracy, etc.
3. For incremental reading data, reading status and reading priority may also appear.
4. When set to unique identifier, clicking the identifier copies a card reference for use in notes or other cards.

## Desktop and Mobile Interaction
1. Desktop: single-click to select, or perform locate/jump or linked actions in those modes; double-click to edit.
2. Desktop hover shows top-right actions: jump to source, convert to Markdown, edit, view details, delete.
3. Mobile: single-click to show or hide top-right actions; double-click to edit; long-press for multi-select.
4. Grid view does not have table view’s “long-press checkbox and swipe for continuous multi-select.” Multi-select relies mainly on single-click toggle or mobile long-press.

> Note: For fast swipe selection of many cards, switch back to table view.

## Common Single-Card Actions
Top-right actions on grid cards cover everyday single-card tasks.

1. Jump to source: return to the note, PDF, EPUB, etc. for this card.
2. Edit: open the editor to change card content.
3. View details: see fuller card information.
4. Convert to Markdown: export or write card content into a note.
5. Delete: remove the card. Confirm before deleting.

## Multi-Select and Batch Operations
Grid view also supports multi-select; a batch action bar appears at the bottom after selection.

1. Desktop single-click toggles selection; mobile long-press enters multi-select.
2. After selection: create deck, change deck, add to exam question group, add/remove tags, export summary to Markdown, delete, etc.
3. Before batch operations, narrow the set with top property search, then select cards to process.

## Locate-and-Jump Mode
Use this when browsing grid cards while jumping back to source documents for context.

1. Enable **Locate-and-Jump Mode**.
2. After that, clicking a card prioritizes jumping to its source document or trace location.
3. Turn off when done to restore normal click-to-organize behavior.

> Note: Locate-and-jump mode and linked card mode are usually mutually exclusive—enabling one turns off the other.

## Linked Card Mode and Sidebar Integration
Linked card mode works best in grid card view. After dragging card management to an Obsidian sidebar, the interface automatically switches to a cleaner sidebar mode.

1. Move card management to the left or right Obsidian sidebar.
2. Switch to grid view and enable **Linked Card Mode** or **Link Active Document**.
3. When you open notes, PDFs, EPUBs, etc. in the main content area, the sidebar links to the active document and automatically filters cards whose sources point to that document.
4. Quickly see which memory cards, excerpt notes, and test questions came from the current document.
5. In sidebar mode, grid cards also support drag interactions for use with the Obsidian content area.

## Property Search and Filtering
Grid view shares the same top search as table view.

1. Enter keywords to search card content.
2. Or use property prefixes such as `deck:`, `tag:`, `folder:`, `source:`, `priority:`, `type:`, `status:`, `created:`, `modified:`, `due:`, `yaml:`.
3. In exam question groups, also use `accuracy:`, `attempts:`, `error:`.
4. Prefix input shows suggestions; use `-` to exclude.

> Note: Syntax follows Obsidian search design.
