The reader settings page covers UI language, default bookshelf display, auto progress save, book data directory, and export template directory. When syncing, distinguish **books and notes in the Vault** from **plugin cache**. Details below:

## 1. Open Settings
1. Click **Settings** on the bookshelf toolbar, or open Weave EPUB Reader under Obsidian settings.
2. Common tabs: Basic, Vocabulary, License, About.
3. **About** shows version, supported formats, platform, and contact info.


## 2. Interface Language
1. Default is **Follow Obsidian**.
2. You can also pick Simplified Chinese, Traditional Chinese, English, Japanese, Korean, Russian, German, Spanish, Arabic, and more individually.
3. After specifying a language, the plugin UI may not revert to English when you change Obsidian’s language.


## 3. Default Bookshelf Display
**Default display mode for My Bookshelf** matches bookshelf menu modes: follow location, list details, card grid, covers only. See `Er-01a 安装与打开书架`.

## 4. Auto-Save Reading Position
1. Toggle **Auto-save reading position**.
2. Set how many pages of continuous reading trigger a save.
3. Closing the reader or switching books still saves last position. See `Er-01c 书签、进度与参考阅读点`.

## 5. Book Data Directory
Progress, bookmarks, and covers for each book default to a Vault folder (commonly `Weave EPUB Reader`), filenames like `data_*.md`, covers in matching `covers/`.

1. You can change this directory in settings.
2. On change, existing `data_*.md` and covers migrate to the new location when possible.
3. Same-name files at the destination are skipped to avoid overwrite.
4. New directory cannot be a child or parent of the current directory.


## 6. Export Template Directory
Specifies which folder export templates are loaded from. If changing directory fails, move files manually per prompt. See `Er-04a 导出笔记与模板`.

## 7. What to Sync
**Recommended to sync with Vault:**

1. Original book files (epub, pdf, etc.).
2. Your Markdown excerpts, Canvas, Weave Deck.
3. Book data notes `data_*.md` and covers.

**Usually no need to sync across devices:**

1. Reading cache and indexes.
2. Other local state under the plugin directory.
3. Do not treat the whole `.obsidian/plugins/weave-epub-reader/` folder as **notes** to sync.

> Note: Multi-device use relies on Vault sync. On a new computer, confirm books and notes exist before opening the bookshelf.

## 8. Premium Preview Toggle
**Show premium feature preview** is on by default. Basic UI shows locked premium entries; click for tier explanation. Turn off for less clutter—the choice is remembered.


## 9. Diagnostics
Development and diagnostic switches are for troubleshooting only. Keep them off during everyday reading to avoid log noise.
