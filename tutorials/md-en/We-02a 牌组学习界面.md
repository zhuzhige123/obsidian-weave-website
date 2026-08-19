In the Weave Deck main interface, **Deck Study** and **Card Management** are two important entries. Deck Study works at the deck level—for creating decks, browsing decks, starting memory study, and import/export. Here is a detailed guide:
![[QQ_1786447495859.png]]

![[QQ_1786447562170.png]]
## Create a Deck
Use this when you need a learnable deck entry first.

1. Open the plugin main interface and enter **Deck Study**.
2. Click **Create Memory Deck** in the top-left menu.
3. Fill in deck name and related info per prompts and save.
4. After creation, the new deck appears in Deck Study; you can add cards to it afterward.

> Note: If currently switched to exam question group mode, the menu shows **Create Exam Question Group** instead. The rest of this article follows the memory deck main path.

## Deck Interface
Deck Study shows each deck as a deck card with name, study-related status, and direct entry to study.

1. In the main content area, decks usually display in a kanban-style multi-column layout—good for wide screens and many decks.
2. Each deck is a clickable card with its own menu.
3. Here you manage **decks**, not individual memory cards as in Card Management.
![[QQ_1786447637557.png]]
## Switch Deck Card Style
Deck cards in Deck Study support two style themes you can switch by preference.

1. Open plugin settings and find **Deck Card Style**.
2. **Default**: standard deck card appearance.
3. **Elegant Chinese Style**: an alternate deck card visual with a more traditional Chinese aesthetic.
4. After switching, Deck Study, related grid displays, and embedded deck views in notes all follow the chosen style.

> Note: This theme is deck card appearance—not formal vs. emergent decks, and not the Obsidian appearance theme.

![[QQ_1786447666804.png]]
![[QQ_1786447683734.png]]
## Deck Card Menu
Open the menu on a deck card for deck-level management.

1. Edit deck: change deck name, description, and related info.
2. Deck analysis: view study and review statistics for this deck.
3. Study ahead: study some cards outside the normal due queue.
4. Export as APKG: export the deck to the legacy common card package format.
5. Dissolve deck: remove deck organization—confirm per prompts before proceeding.
6. For emergent decks, you can also **Convert to Formal Deck**.

> Note: Dissolving a deck is not the same as deleting cards. Dissolve affects deck entry and organization; deleting cards removes card content.


## Enter Memory Study
Use this to start review from a deck.

1. Click start study on a deck card.
2. If that deck has an in-progress study session, you can continue where you left off.
3. In memory study, rate the current card, edit, and jump back to source documents when trace info exists.
4. After finishing the session, you get settlement and follow-up guidance.

> Note: Rating keys, toolbar, and more actions inside memory study are in `We-02c 记忆学习界面`.

![[QQ_1786447683734.png]]
## Import CSV and Legacy APKG
Use this to import existing card packages or spreadsheet data into Weave Deck—not everyone needs it, so entries can be hidden in settings.

1. Open the top-left menu in Deck Study.
2. Choose **Import Legacy Card Package** or **Import CSV File**.
3. Follow the wizard to select files and complete import.
4. If you do not use these entries, disable the corresponding buttons in plugin settings and they disappear from the menu.

> Note: CSV import may be an advanced feature. After import, confirm the deck appears in Deck Study, then check card content in Card Management.

![[QQ_1786447838801.png]]
## Position Adaptation and Note Embedding
Deck Study works in different Obsidian positions and can be embedded in Markdown notes.

1. After moving the main interface to an Obsidian sidebar, it can auto-switch to a grid card view suited to narrow columns; moving back to the main content area can auto-switch to kanban view.
2. Enable or disable **Auto-switch deck study view by position** in basic plugin settings.
3. Insert a `weave-decks` code block in an `.md` file to embed a deck view in a note for direct browsing and study.

> Note: Position adaptation changes how Deck Study displays; note embedding puts deck entry on ordinary note pages.

![[QQ_1786447877556.png]]
## Emergent Decks and Kanban Column Settings
This section covers further organization of deck display.

1. Emergent decks can configure **Emergent Filter Groups** to auto-generate study views by tags and rules.
2. In kanban display, open **Kanban Column Settings** to organize deck columns by tags and similar dimensions.
3. In kanban column settings you can show/hide columns, adjust column order, and create, edit, or delete tag groups used for columns.

> Note: Kanban column settings affect how decks columnize; emergent decks affect which deck views are auto-aggregated. Both are organization—not rewriting card body text.

![[QQ_1786447922937.png]]
## Switch to Exam Question Groups
Deck Study also supports switching to exam question groups.

1. Use top colored dots to switch from memory decks to exam question groups.
2. After switching, the main area shows exam question group cards; the top-left create entry becomes **Create Exam Question Group**.
3. Exam question groups may be an advanced feature. Questions in groups are usually batch-imported from Card Management—qualifying multiple-choice cards, etc.

> Note: Memory decks focus on spaced repetition; exam question groups focus on testing and group-style practice. Learn memory decks on the main path first, then switch to exam groups as needed.
