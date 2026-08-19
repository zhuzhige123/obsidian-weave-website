Bidirectional tracing lets notes, Canvas, cards, and the original book jump to each other: click the book icon in a note to return to the sentence; click a highlight in the book to open the source note. Precise positioning is premium support; without it you can still read and make basic excerpts, but links may not land on the exact sentence. Details below:

## 1. Where Trace Links Come From
After inserting excerpts into Markdown, Canvas, or decks per `Er-02a 摘录笔记工作流`, entries carry book location info.

1. The reader draws re-highlight in the body from that data.
2. Clickable book icons or links appear in notes.
3. Changing color or adding a thought on the same excerpt syncs re-highlight when possible.

> Note: Plain copied text without trace fields is just a quote—the reader cannot jump or re-highlight from it.

## 2. From Book to Note
1. Click a highlight in the body.
2. On the toolbar, choose jump to note.
3. Obsidian opens the Markdown (or other) file that holds the excerpt and scrolls to the paragraph when possible.

> Note: If one excerpt is referenced in multiple places, you may see a source list—pick which note to open.

## 3. From Note Back to Book
1. In the note that holds the excerpt, click the book icon or deep link beside it.
2. The reader opens the matching book and tries to scroll to the original sentence.
3. Backlinks on Canvas nodes work the same way back into the book.
4. Weave cards with reader traces can also jump back from study UI. See source-field notes in `We-01a 新建卡片`.

> Note: Precise positioning may prompt for premium activation. Without activation, the book may open but not land on the exact sentence.

## 4. Supported Formats
Tracing targets formats the reader supports, including EPUB, MOBI, TXT, CBZ, and more.

1. Internal positioning differs by format; usage is still **click link to return**.
2. PDF uses Obsidian’s built-in viewer—jump behavior differs from EPUB.
3. After moving or renaming book files, old links may break; re-excerpt or check paths.

> Note: Keeping book files at stable paths inside the Vault makes tracing more reliable.

## 5. Legacy Link Migration
If notes still use old long links with full text embedded in the URL, editing feels awkward.

1. When opening related notes, you may be prompted to shorten EPUB trace links.
2. After confirming, body text parameters are removed from links and location data is compressed.
3. Quoted body text inside callouts is not changed.
4. You can defer migration and handle it later.

> Note: Migration changes link structure only—not your thought text. Back up notes or rely on sync recovery first.

## 6. When Re-Highlight Does Not Appear
1. Confirm the excerpt was written to Vault files, not clipboard only.
2. Confirm the book is still at the same path and opens from the bookshelf.
3. Close and reopen the reader so indexing rescans.
4. Check whether the linked paragraph was deleted from the note.
