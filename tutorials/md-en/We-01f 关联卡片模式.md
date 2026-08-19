Obsidian Weave supports enabling linked card mode in card management to view reference relationships between one card and others. After enabling, clicking a card filters cards it references and cards that reference it. Here is a detailed guide:

## Linked Card Mode
This feature shows the reference network between cards via in-content references. It works best in grid card view and can also be used in kanban view.

1. Open the plugin main interface and use the top-left menu to switch to **Card Management**.
2. Switch to grid view or kanban view.
3. Click the **Link** button in the top bar, or enable **Linked Card Mode** in the top-left menu.
4. After enabling, click a card to filter from that card as the starting point. Results include the current card and others referenced in each other’s content.
5. If the card has no other linked cards, a notice appears and focus stays on the current card itself.
6. Click **Link** again or disable the mode in the menu to exit; linked filter results are cleared on exit.

> Note: Linked card mode and locate-and-jump mode usually cannot run together—enabling one turns off the other.

## Build Card References
Linked card mode depends on Weave card references in card content—not automatic guessing by same deck, tag, or source document.

1. In grid view, set top-left card property to **Unique Identifier**.
2. Click the identifier to copy the linked card reference format.
3. Paste the copied content into another card’s content to establish a reference.
4. While editing, you can also type `@_` and pick a card from completions.
5. After references exist, enable linked card mode and click one card to filter mutually referenced cards.

> Note: Without card references to each other in content, linked mode usually shows only the current card itself.

## Link Active Document
Unlike linked card mode, **Link Active Document** filters cards whose sources point to the document currently open in Obsidian’s content area.

1. Move the card management interface to an Obsidian sidebar; it automatically switches to a cleaner sidebar mode.
2. Switch to grid view and enable **Link Active Document**.
3. After opening notes, PDFs, EPUBs, etc. in the main content area, the sidebar automatically filters cards sourced from the active document.
4. See which memory cards, excerpt notes, and test questions came from the current document.
5. You can also enable linked card mode on top and click a card to continue viewing its references to other cards.

> Note: Linked card mode shows card-to-card references; Link Active Document shows document-to-card source relationships. Both can be used together.
