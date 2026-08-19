The reader remembers where you left off and lets you pin two different positions manually: a current-page bookmark and a reference reading point. Progress suits **resume where I stopped**; bookmarks suit multiple marks within a chapter; reference points suit stepping away, checking earlier text, then jumping back. Details below:

## 1. Where Reading Progress Is Saved
Each book’s progress, bookmarks, cover, and related info are written to book data notes in the Vault (default folder `Weave EPUB Reader`, filenames like `data_*.md`).

1. Closing the reader or switching books generally saves the last reading position.
2. The bookshelf shows reading progress percentage and prompts such as **Continue reading**.
3. This data lives in the Vault and can sync to other devices with your Vault sync.


## 2. Auto-Save Reading Position
Enable **Auto-save reading position** in settings.

1. After reading continuously for a set number of pages, the current position is saved automatically.
2. Page count has min/max bounds; defaults are described on the settings page.
3. Even with auto-save off, closing the reader or switching books still saves the last position.


## 3. Current-Page Bookmarks
Bookmarks pin **this page / this spot**; you can keep multiple in one book.

1. At a position you want to remember, click **Add current-page bookmark** at the top, or use the matching menu item.
2. On success you are notified the bookmark was added; if the page already has one, you are told it exists.
3. Open the bookmark list in the sidebar to jump to a bookmark or delete it.
4. An empty list prompts: click the top bookmark button to save the current position.


## 4. Reference Reading Point
A reference reading point usually keeps one **comparison anchor** at a time—good for flipping elsewhere, then jumping back.

1. At the spot you need to return to, use **Record reference reading position** or the toolbar record action.
2. After recording, use **Jump to reference reading position** to return instantly.
3. If the position changed, use **Update reading position** to overwrite with the current spot.
4. When no longer needed, **Clear reference reading position**.
5. The top bar may show a badge or sticker indicating the recorded reference point and relative progress.


## 5. Progress, Bookmarks, and Reference Points—How to Choose
Use them for different goals; they do not replace each other.

1. **Resume reading**: Rely on auto-saved or close-time last position; from the bookshelf, click **Continue reading**.
2. **Several spots in this chapter to revisit**: Use current-page bookmarks and jump from the sidebar list.
3. **Check an earlier sentence, then return to this one**: Use a reference reading point.
4. **Finished the whole book**: You can **Mark as finished**; resume position still follows the rules above—marking does not automatically clear bookmarks.


## 6. PDF Special Case
PDF appears on the bookshelf but opens in Obsidian’s built-in viewer.

1. Open the PDF first.
2. From the bookshelf book menu, choose **Remember current position**, or run **Remember PDF reading position** (exact command name in the palette).
3. On success you may see page number and progress percentage.
4. Trying to remember position without opening the PDF prompts you to open the file first.


## 7. Common Prompts
1. **No reference reading position recorded yet**: Record first, then jump.
2. **Current page already has a bookmark**: No need to add again on the same page.
3. **Bookmark does not exist or was deleted**: List refreshed—just add again.
4. If the source file is lost, the bookshelf may remove the book; excerpt notes remain in their original Markdown files.
