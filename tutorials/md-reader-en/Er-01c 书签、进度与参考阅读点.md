The reader remembers where you left off and lets you pin two kinds of positions: a current-page bookmark, and a **paragraph-level resume** spot. Progress suits **continue where I stopped**; bookmarks suit multiple marks within a chapter; resume suits selecting body text to pin an exact paragraph so reopen locates with a brief highlight, or stepping away to check earlier text and jumping back. Details below:

## 1. Where Reading Progress Is Saved
Each book’s progress, bookmarks, timers, and bookshelf membership live in `library-state.json` under the book data folder (commonly `Weave Reader`); covers are cached under matching `covers/`.

1. Closing the reader or switching books generally saves the last reading position.
2. The bookshelf shows reading progress percentage and prompts such as **Continue reading**.
3. This data lives in the Vault and can sync to other devices with your Vault sync.

> Note: Older versions created a `data_*.md` page per book. If leftovers remain, the plugin may prompt migration into `library-state.json` and cleanup; your excerpts in Markdown / Canvas files are unchanged.

## 2. Auto-Save Reading Position
Enable **Auto-save reading position** in settings. It serves **continuous forward reading**, not treating every backlink jump as resume.

1. After reading continuously for a set number of pages, the current position is saved automatically.
2. Page count has min/max bounds; defaults are described on the settings page.
3. Even with auto-save off, closing the reader or switching books still saves the last position.
4. If you care more about **not overwriting resume while checking sources**, prefer the paragraph-level resume pin—see the next section and `Er-00a 设计理念下的一些考虑`.

## 3. Current-Page Bookmarks
Bookmarks pin **this page / this spot**; you can keep multiple in one book.

1. At a position you want to remember, click **Add current-page bookmark** at the top, or use the matching menu item.
2. On success you are notified the bookmark was added; if the page already has one, you are told it exists.
3. Open the bookmark list in the sidebar to jump to a bookmark or delete it.
4. An empty list prompts: click the top bookmark button to save the current position.

## 4. Paragraph-Level Resume Position
Resume usually keeps one resume anchor at a time, and supports **paragraph-precise locate after selecting text** (free tier).

1. Select the sentence or paragraph you want to resume at, then tap **Pin as resume** on the selection toolbar, or use the matching menu / toolbar action.
2. You can also record the current position from the toolbar without a selection; for best accuracy, prefer selecting text first.
3. After pinning, use **Jump to resume position** to return instantly; reopening the book also tries to locate that paragraph with a brief highlight.
4. Continuous paging and source-link browsing **do not** auto-overwrite this pin; to update it, select text and pin again.
5. When no longer needed, **Clear resume position**.
6. The top bar may show a badge or sticker; the bottom progress scale can show a resume pin when the scale is on. See `Er-03i 阅读进度刻度条`.

> Note: The paragraph pin means “back to this sentence.” It is not the same as “last browse position saved on close,” which may still update when you close or switch books. The pin protects the resume sentence you chose.

## 5. Progress, Bookmarks, and Resume—How to Choose
Use them for different goals; they do not replace each other.

1. **Resume at an exact paragraph**: select text and pin paragraph-level resume; **Continue reading** from the bookshelf also tries to honor that pin.
2. **Several spots in this chapter to revisit**: use current-page bookmarks and jump from the sidebar list.
3. **Check an earlier sentence, then return to this one**: pin resume first, then browse.
4. **Mostly linear reading with little pinning**: rely on close-time save or continuous-reading auto-save; still pin paragraph resume at important breaks.
5. **Finished the whole book**: you can **Mark as finished**; resume rules above still apply—marking does not automatically clear bookmarks.

## 6. PDF Special Case
PDF appears on the bookshelf but opens in Obsidian’s built-in viewer.

1. Open the PDF first.
2. From the bookshelf book menu, choose **Remember current position**, or run **Remember PDF reading position** (exact command name in the palette).
3. On success you may see page number and progress percentage.
4. Trying to remember position without opening the PDF prompts you to open the file first.

## 7. Common Prompts
1. **No resume position pinned yet**: select text and pin first, then jump.
2. **Current page already has a bookmark**: no need to add again on the same page.
3. **Bookmark does not exist or was deleted**: list refreshed—just add again.
4. If the source file is lost, the bookshelf may remove the book; excerpt notes remain in their original Markdown files.
