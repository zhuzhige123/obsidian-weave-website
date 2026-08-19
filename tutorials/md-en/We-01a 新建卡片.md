
Weave Deck supports several ways to create cards: standard new card, selected text, AI card generation, batch parsing, and importing from external files in multiple formats. Here is a detailed guide:

## Standard New Card
After installing the plugin, a floating action button with a ➕ icon and pulse animation appears in the Obsidian interface. You can long-press and drag it to any position. If you prefer not to see it, you can turn it off in the plugin settings.

1. After clicking the new-card floating button, enter card content in the modal, choose a deck, and save. At the top of the modal is a pin button—useful when you want to create and save multiple cards without closing the modal.
2. The new-card editor uses Obsidian’s official editor, so it works naturally with many plugins. For example, after opening the new-card modal, you can open the PDF++ plugin and automatically paste PDF selections into the modal, then save. Note that cards are saved in non-Markdown JSON files—`.wdeck` deck files—so PDF++ cannot render the selection box inside the PDF file itself. However, Weave Deck supports tracing back to the PDF selection location.
3. To add a source link for a new card, find the YAML field named `we_source` in the editor and fill in the source link. Supported formats include Obsidian links, PDF++, Excalidraw, Weave EPUB Reader, and external URLs. The plugin parses this automatically when saving.

## Create Card from Selected Text
Unlike standard new card, creating from selected text automatically generates a block-level source link. Steps:

1. In Obsidian’s hotkey settings, find the command for creating a card from selected text and assign a shortcut.
2. Open any Markdown file, select a passage, and trigger the shortcut. The selection is filled into the new-card modal that opens automatically. A block ID for source tracing is also created at the source location—this is an official Obsidian feature. You can edit it freely as long as the ID stays consistent.
3. To keep the card content in Weave Deck in sync with edits in the source document, use another shortcut: “Create card from embedded block link.” This follows Obsidian’s block reference design—fetching specified content from a document, heading, or block so the rendered reference always matches the source. ^we-bu9lor

## AI Batch Card Generation
This feature uses AI to read document content and batch-generate memory cards that follow good card-design principles. The plugin includes two built-in prompt sets and supports multiple common AI providers for everyday use.

1. Open the plugin main interface. Use the top-left menu to switch to AI Card Generation.
2. Select a file or folder. Choosing a folder lets AI read all files under it.
3. Select an AI provider and model.
4. Click Generate.
5. Preview the AI-generated cards and selectively import them into a target deck.

> Note: You can open AI Card Generation settings from the top-left menu to configure card count, question types, custom prompts, and more.

## Batch Parse and Import Cards
This feature is for files that already contain multiple cards in a standard format, or Markdown files with multiple memory cards produced while chatting with other tools. Configure a custom regex template to parse card content and import into a target deck.

1. Open the plugin main interface, switch to AI Card Generation via the top-left menu, then click the colored dot at the top to switch to Parse Preview.
2. Select a file or folder.
3. Choose a parse template.
4. Click Start Parsing.
5. Preview parsed cards and select the ones you want.
6. Choose a deck and import.

> Note: The plugin includes several built-in regex parse templates. Both AI card generation and regex parsing mark selected files as source documents for cards, but not at block-level precision.

## Adding Word-Type Cards
The latest Weave EPUB Reader adds a vocabulary feature for assisted reading of English originals. It works with adding looked-up words to Weave Deck.

1. Search for the fingertip translation plugin in the Obsidian community plugin marketplace.
2. It supports lookup on text selection and Ctrl+selection without extra setup—lightweight and practical for basic needs.
3. After selecting text, a lookup popup appears. Click Add to Weave Deck in the bottom-right corner, choose a deck, and the word is added.

> Note: Word cards added to Weave Deck can auto-play pronunciation when you switch cards. US vs. UK pronunciation defaults follow fingertip translation plugin settings.

## Import External Card Files
This feature is for legacy APKG and CSV files.

1. Open the plugin main interface.
2. In the Deck Study interface, open the top-left menu and find CSV and legacy APKG import.
3. Follow the on-screen steps from there.
