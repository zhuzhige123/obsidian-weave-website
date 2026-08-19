Weave Deck supports embedding a **Deck Study view** in ordinary Markdown notes. In the editor, use the right-click menu to insert selected memory decks as a `weave-decks` code block; after the note renders, deck cards display directly and you can start study from there. Good for putting study entry in course notes, review checklists, topic pages, or dashboards. Here is a detailed guide:

## Overview

The embedded deck view essentially moves deck cards from the plugin’s **Deck Study** onto the current note page.

1. It shows **memory decks**, not exam question groups.
    
2. Each deck card still shows due counts, study status, etc., and you can click to start study directly.
    
3. Insertion produces a code block in the note; in Obsidian reading mode or live preview, the block renders as a visual deck grid.
    
4. This differs from opening the plugin main window for Deck Study: the main interface suits centralized management; note embedding puts study entry beside the document you are reading or organizing.
    

> Note: When the plugin main interface is dragged to a sidebar, **position adaptation** changes how the main window displays; this article covers writing deck views into `.md` note body text.

## Insert via Editor Right-Click

The most common insertion path is the Weave Deck right-click menu in the Markdown editor.

1. Open any Markdown note and place the cursor where you want insertion.
    
2. **Right-click** in the edit area to open the Obsidian editor menu.
    
3. Find **Weave Deck Actions** and open its submenu.
    
4. Choose **Insert Deck View** to expand the deck selection list.
    
5. Check decks to display in the list; tap again to toggle check state.
    
6. When ready, click **Insert into Current Note**.
    
7. The plugin inserts a `weave-decks` code block at the cursor and notifies how many decks were inserted.
    

> Note: If no memory decks exist yet, the submenu may show **No decks available**. Create decks in plugin **Deck Study** first, then retry.

## Deck Selection Submenu

Besides the deck list, **Insert Deck View** submenu has helper actions.

1. **Deck list**: lists memory decks in the vault; a check mark before the name means selected.
    
2. **Select All**: select all available memory decks at once.
    
3. **Clear Selection**: clear current checks to re-pick.
    
4. **Insert into Current Note**: generate the code block from current checks and write to the note.
    

The plugin remembers your last deck checks. Next time you open the same submenu, checks usually restore—convenient for inserting the same deck set into different notes repeatedly.

> Note: If **Insert into Current Note** is clicked with no decks checked, the interface prompts **Please check decks to display in the submenu first**.

## Generated Code Block After Insert

After successful insertion, the note contains a code block similar to:

```weave-decks
title: My Decks
size: medium
deckNames:
  - Deck A
  - Deck B
sort: due
limit: 6
```

Field meanings:

1. **title**: title shown above the embedded area; leave empty or delete the line if not needed.
    
2. **size**: deck card size—`small`, `medium`, or `large`; shorthand `s` / `m` / `l` or Chinese 小/中/大 also work.
    
3. **deckNames**: list of deck names to show; names must match memory deck names in the plugin exactly.
    
4. **sort**: sort order. `due` prioritizes decks with most due reviews; `name` sorts by name.
    
5. **limit**: max decks to show; e.g. `6` shows only the first 6 matching decks.
    

> Note: You can hand-write the code block without right-click; right-click insert auto-generates the template and fills checked deck names.

## Display in Notes

When Obsidian renders the note, the code block becomes an actual deck card grid.

1. If **title** is set, it appears above deck cards.
    
2. Each deck shows as a card; style follows **Deck Card Style** in plugin settings (e.g. **Default**, **Elegant Chinese Style**).
    
3. Cards show deck name, due/review status, etc.—consistent with grid deck cards in main Deck Study.
    
4. Wrong, deleted, or non-matching deck names may show **No decks found to display**.
    
5. While data loads, **Loading decks...** may appear briefly.
    

> Note: Embedded view shows **deck entry**, not a list of individual memory cards. For specific card management, use plugin **Card Management**.

## Start Study from Embedded View

Embedded deck cards are not display-only—you can operate them directly.

1. Click a deck card to **start study** that deck like in the main interface.
    
2. Open the menu on a deck card for edit, study ahead, analysis, export, etc.—same items as main Deck Study deck card menu.
    
3. Study enters normal memory study; after completion you return to the note and the embedded view stays in place.
    

> Note: Rating, toolbar, and more inside memory study are in `We-02c 记忆学习界面`.

## Manually Adjust Embedded Content

After insertion, edit the code block directly to fine-tune scope or appearance without repeating right-click.

1. **Show only some decks**: edit the `deckNames` list and keep needed names.
    
2. **Change card size**: set `size` to `small`, `medium`, or `large`.
    
3. **Prioritize most due decks**: set `sort` to `due` and use `limit` to cap count.
    
4. **Add a topic page title**: change `title`, e.g. to “This Week’s Review” or “Chapter 3 Decks”.
    
5. Save the note; Obsidian re-renders to show changes.
    

If a deck was just created or renamed but the embed still cannot find it, first verify `deckNames` exactly matches current deck names.

## Typical Use Cases

Use flexibly by how you organize notes:

1. **Course/chapter notes**: insert corresponding decks at each chapter end—study right after reading.
    
2. **Review dashboard**: a dedicated “Today’s Review” note with `sort: due` and `limit` to focus on the most urgent decks.
    
3. **Topic summary page**: multiple decks under one theme—one insert or manual `deckNames` list for unified display.
    
4. **Obsidian home or navigation page**: embed frequently used decks in an entry note to reduce switching to the plugin main interface.
    

## Relation to Main Deck Study

Both complement each other—combine by habit:

| Comparison | Embedded deck view in notes | Plugin main · Deck Study |
|--------|------------------|------------------------|
| Entry | Code block in Markdown notes | Plugin main window |
| Best for | Study entry written in documents | Browse, create, manage all decks centrally |
| View | Grid cards | Kanban / grid (position adaptive) |
| Question groups | Cannot embed exam question groups | Can switch to exam question group mode |

> Note: Create deck, kanban column settings, position adaptation in main Deck Study are in `We-02a 牌组学习界面`. Exam question groups are in `We-02d 考试题组`.

## FAQ

**Q: Why is a deck missing from the list?**  
A: Embedding currently supports **memory decks** only; exam question groups do not appear in **Insert Deck View**.

**Q: After insert it shows “No decks found to display”?**  
A: Usually `deckNames` does not match real deck names, or the deck was deleted/renamed. Compare names in plugin Deck Study and edit the code block.

**Q: Can I insert in Excalidraw, Canvas, or non-Markdown pages?**  
A: This feature targets Markdown editor right-click; use `weave-decks` code blocks in `.md` notes.

**Q: Will embedded view look different from the main interface?**  
A: Deck card style follows **Deck Card Style** in plugin settings; changing settings updates both main interface and note embeds together.
