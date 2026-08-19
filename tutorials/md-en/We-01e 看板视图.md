The Obsidian Weave card management interface supports table, grid, kanban, and other views. Kanban view organizes cards into multiple columns by status, deck, priority, question type, tags, and other dimensions. Some groupings support drag-and-drop to adjust membership. Here is a detailed guide:

## Open Kanban View
After installing the plugin, open the plugin main interface. Use the top-left menu to switch to **Card Management**.

1. After entering card management, choose **Kanban View** from the top view switcher. On desktop this is often a dropdown; on mobile, use colored dots.
2. Kanban arranges current cards into multiple columns by the chosen grouping—e.g. New, Learning, Review, or columns by deck or priority.
3. The top bar still supports property search filtering, e.g. `deck:`, `tag:`, `source:`, `status:`.

> Note: Kanban view may be an advanced feature. If prompted to activate when clicking, follow the plugin guidance.

## Switch Data Source
Kanban also supports different data sources.

1. Use the top-left menu or top data source button to switch between **Memory Decks** and **Exam Question Groups**.
2. **Memory Decks** suit organizing everyday cards by study status, deck, priority, etc.
3. **Exam Question Groups** suit viewing exam question distribution by status, type, priority, etc.
4. Different data sources remember their preferred grouping—switching back does not require resetting.

## Choose Grouping
Decide what the kanban columns represent—in view options or **Kanban Column Settings**.

1. **Status**: columns for New, Learning, Review, Relearning.
2. **Question Type**: columns for Q&A, multiple choice, cloze, etc.
3. **Priority**: columns for Urgent, High, Medium, Low.
4. **Deck**: columns by owning deck.
5. **Created Time**: columns for Today, Yesterday, Past 7 Days, Past 30 Days, Earlier, etc.
6. **Tag** or **Tag Group**: columns by tag dimension.

> Note: Changing grouping does not create another card set—only a different organization angle.

## Drag to Adjust
Not every grouping supports drag to change membership. Under memory decks / exam question groups, these drag adjustments are mainly supported:

1. When grouped by **Priority**, drag cards to another priority column to adjust priority directly.
2. When grouped by **Deck**, drag cards to another deck column to change deck membership.
3. When grouped by status, question type, created time, tag, or tag group, drag usually does not change columns—edit the card for those properties.

When dragging to another deck column, the plugin may ask how to handle it:

1. Remove from the original source deck and add to the target deck.
2. Keep the original deck and also add to the target deck so the card belongs to multiple decks.
3. Cancel this drag.

> Note: Groupings marked non-draggable in the menu will not change data when dragged.

## Display Density
Card spacing within kanban columns is adjustable.

1. Open density controls and switch among **Compact**, **Comfortable**, and **Spacious**.
2. Compact suits small screens or seeing more cards at once.
3. Comfortable is a balanced default look.
4. Spacious suits reading card content carefully.

## Kanban Column Settings
Fine-tune kanban for your workflow—interaction patterns reference Notion.

1. Open **Kanban Column Settings** or view options.
2. Switch grouping, set in-column sort (created time, due time, modified time, priority, difficulty, title, etc.).
3. Hide empty groups so columns with no cards take no space.
4. Fill column backgrounds to distinguish columns more easily.
5. Adjust column order, colors, and other appearance settings.
6. When a column has many cards, view a portion first, then **Load More** to expand.

## Single-Card and Multi-Select Operations
Cards in kanban columns use the same base interaction as grid cards.

1. Desktop: single-click to select; double-click to edit. Hover shows jump to source, convert to Markdown, edit, view details, delete.
2. Mobile: single-click to show or hide actions; double-click to edit; long-press for multi-select.
3. Use column header **Select All in Column** to quickly select all cards in a column.
4. After selection, the bottom batch bar supports create deck, change deck, add/remove tags, export, delete, etc.
5. Top-left card property badges can show source document, priority, unique identifier, accuracy, etc.

> Note: Kanban does not have table’s “long-press checkbox and swipe for continuous multi-select.” For fast bulk swipe, switch to table view; for whole-column batch work, **Select All in Column** fits better.

## Property Search and Filtering
Kanban shares top property search with other card management views.

1. Enter keywords to match card content.
2. Or use property prefixes such as `deck:`, `tag:`, `folder:`, `source:`, `priority:`, `type:`, `status:`, `created:`, `modified:`, `due:`, `yaml:`.
3. In exam question groups, also use `accuracy:`, `attempts:`, `error:`.
4. After search, kanban shows only matching cards and still columns them by the current grouping.

> Note: Syntax follows Obsidian search design.

## Locate-and-Jump and Linked Mode
1. With **Locate-and-Jump Mode** enabled, clicking a card prioritizes jumping to the source document location.
2. With **Linked Card Mode** enabled, clicking a card performs linked filtering instead of normal multi-select.
3. The two modes are usually mutually exclusive—enabling one turns off the other.

> Note: Linked card mode works best in grid card view. Kanban suits categorical organization and drag to adjust membership.
