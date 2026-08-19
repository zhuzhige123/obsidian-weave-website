Timeline view in Weave Deck card management is a layout under grid view. It groups and arranges cards by time—good for reviewing recently added or organized cards and browsing thematic or document-related card history chronologically. Here is a detailed guide:

## Open Timeline View
Timeline is not a top-level view alongside table and grid—it is a layout within grid view.

1. Open the plugin main interface and use the top-left menu to switch to **Card Management**.
2. Switch to **Grid View** first.
3. Open **Grid Layout** and choose **Timeline View**. On desktop you can also switch via top layout controls.
4. After entering, cards group by date along a timeline axis toward the past.

> Note: Timeline view may be an advanced feature. If prompted to activate when clicking, follow the plugin guidance.

## Timeline Layout Rules
The timeline tries to order cards from newest to oldest by time.

1. It reads card creation time first; if missing, it falls back to modified time.
2. Within the same day, newer cards are still preferred toward the front.
3. Date groups show month/day and weekday; month and year headings appear when crossing months or years.
4. Today’s group is labeled **Today**; groups within the last 7 days are labeled **Last 7 Days**.
5. Cards without usable time info go under **Unrecorded** with **Time Missing** shown.

> Note: Timeline changes browse order and grouping only—it does not rewrite card content.

## Basic Operations
Each item in the timeline is still a grid card—operations match grid view.

1. Desktop: single-click to select, or perform locate/jump or linked actions in those modes; double-click to edit.
2. Desktop hover on a card shows top-right actions: jump to source, convert to Markdown, edit, view details, delete.
3. Mobile: single-click to show or hide actions; double-click to edit; long-press for multi-select.
4. Top-left card property badges can still show source document, priority, unique identifier, accuracy, etc.
5. After multi-select, the bottom bar supports the same batch actions: create deck, change deck, add/remove tags, export, delete.

> Note: Timeline does not have table’s “long-press checkbox and swipe for continuous multi-select.” For fast bulk swipe selection, switch back to table view first.

## Property Search and Filtering
Timeline shares top property search with other card management views.

1. Enter keywords to match card content.
2. Or use property prefixes such as `deck:`, `tag:`, `source:`, `folder:`, `priority:`, `type:`, `status:`, `created:`, `modified:`, `due:`, `yaml:`.
3. In exam question groups, also use `accuracy:`, `attempts:`, `error:`.
4. After search, the timeline shows only matching cards and still groups them by time.

> Note: Syntax follows Obsidian search design.

## Switch Data Source
Timeline also supports memory decks and exam question groups.

1. Switch via the top-left menu or top data source button.
2. **Memory Decks** suit reviewing everyday card creation and organization over time.
3. **Exam Question Groups** suit reviewing question-related history over time, with accuracy badges when helpful.

## Active Document and Sidebar Integration
Use this when placing the timeline in a sidebar alongside the document open in the main area.

1. Drag card management to an Obsidian sidebar; the interface switches to a cleaner sidebar mode.
2. With **Link Active Document** enabled, the timeline top bar notes that only cards linked to a given document are shown.
3. As you switch notes, PDFs, EPUBs, etc. in the content area, the timeline follows with that document’s card timeline.
4. You can also enable linked card mode and click a card to see other cards linked to it.

## Loading When Many Cards Exist
With large card counts, the timeline loads in batches.

1. Above a certain size, a recent batch of cards shows first.
2. Scrolling down gradually expands earlier time nodes.
3. The bottom may note batch loading and how many cards are currently shown.

> Note: This is batch display for browsing performance—not missing cards. Keep scrolling and earlier groups will appear.
