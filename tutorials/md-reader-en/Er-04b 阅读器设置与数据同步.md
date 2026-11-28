The reader settings page covers UI language, default bookshelf display, auto progress save, book data directory, and export template directory. When syncing, distinguish **books and notes in the Vault** from **plugin cache**. Details below:

## 1. Open Settings
1. Click **Settings** on the bookshelf toolbar, or open Weave Reader under Obsidian settings.
2. Common tabs: Basic, Vocabulary, License, About.
3. **About** shows version, supported formats, platform, and contact info.

## 2. Interface Language
1. Default is **Follow Obsidian**.
2. You can also pick Simplified Chinese, Traditional Chinese, English, Japanese, Korean, Russian, German, Spanish, French, Arabic, and more individually.
3. After specifying a language, the plugin UI may not revert to English when you change Obsidian’s language.

## 3. Default Bookshelf Display
**Default display mode for Weave Reader** matches bookshelf menu modes: follow location, reading calendar, card grid; banner cards and covers-only need premium. See `Er-01a 安装与打开书架`.

## 4. Auto-Save Reading Position
1. Toggle **Auto-save reading position**.
2. Set how many pages of continuous reading trigger a save.
3. Closing the reader or switching books still saves last position. See `Er-01c 书签、进度与参考阅读点`.
4. Design trade-offs (why every jump is not treated as resume) are in `Er-00a 设计理念下的一些考虑`.

## 5. Auto-Write Book Excerpt Notes on Highlight
1. Toggle **Auto-write book excerpt notes on highlight** (on by default).
2. When on: with top **Auto insert** off, highlights create or append a per-book Markdown excerpt in the default new-note folder.
3. When off: highlights no longer auto-create that per-book note; top **Auto insert** and Canvas are unaffected.
4. Workflow details: `Er-02a 摘录笔记工作流`.

## 6. Book Data Directory
Reading progress, bookmarks, and bookshelf membership default to `library-state.json` under a Vault folder (commonly `Weave Reader`); covers live under matching `covers/`.

1. You can change this directory in settings.
2. On change, `library-state.json`, covers, and related data migrate to the new location when possible.
3. Same-name files at the destination are skipped to avoid overwrite.
4. New directory cannot be a child or parent of the current directory.

> Note: If legacy `data_*.md` book pages remain, follow the plugin prompt to migrate into `library-state.json` and clean up; excerpt notes are unaffected.

## 7. Export Template Directory
Specifies which folder export templates are loaded from. If changing directory fails, move files manually per prompt. See `Er-04a 导出笔记与模板`.

## 8. What to Sync
**Recommended to sync with Vault:**

1. Original book files (epub, pdf, etc.), including copies imported from outside the vault.
2. Your Markdown excerpts (including auto-created per-book excerpt notes), Canvas, Weave Review.
3. `library-state.json` and `covers/` in the book data directory.

**Usually no need to sync across devices:**

1. Reading cache and indexes.
2. Other local state under the plugin directory.
3. Do not treat the whole `.obsidian/plugins/weave-epub-reader/` folder as **notes** to sync.

> Note: Multi-device use relies on Vault sync. On a new computer, confirm books and notes exist before opening the bookshelf.

## 9. Premium Preview Toggle
**Show premium feature preview** is on by default. Basic UI shows locked premium entries; click for tier explanation. Turn off for less clutter—the choice is remembered.

## 10. Diagnostics
Development and diagnostic switches are for troubleshooting only. Keep them off during everyday reading to avoid log noise.
