Reading excerpts become syncable, backlinkable notes only when written into Vault files. The reader uses trace links in those files to re-highlight text in the book. If save conditions are not met, a selection often shows only a brief highlight and no real data after close or refresh. Details below:

## 1. Where Excerpts Are Saved
Excerpts can land in three places—pick by scenario.

1. **Markdown notes**: Most common. Open a `.md` file and place the cursor where you want insertion.
2. **Canvas boards**: After binding a canvas, excerpts become nodes. See `Er-02e Canvas 脑图摘录`.
3. **Weave Deck**: With Weave Deck installed, content can fill memory cards. See `Er-04c 与 Weave Deck 制卡、增量阅读、AI 联动`.

> Note: The reader does not treat excerpts stored only in invisible plugin cache as formal notes. For long-term retention, they must land in Vault files.

## 2. Recommended Workflow
For a first excerpt, follow this order for the steadiest result.

1. Create or open a Markdown note as this book’s reading note.
2. Place the cursor where you want the excerpt inserted.
3. Open the book and turn on top-bar **Automation** (auto mode on: insert).
4. Select text in the body and use the selection toolbar to create a highlight or excerpt.
5. Switch back to the note and confirm content was inserted with a clickable book trace.
6. Click the book icon or link in the note—it should jump back to the matching spot in the book.

> Note: Auto insert fails when no active Markdown editor is found. Before inserting, keep the note tab open with the cursor in the edit area.

## 3. Auto Insert vs Copy
Top-bar **Automation** switches between two output modes.

1. **On (insert)**: Excerpts write directly at the cursor in the current note. Good for read-and-note in one flow.
2. **Off (copy)**: Excerpts go to the clipboard for you to paste. Good when you do not want to touch the current note yet, or paste elsewhere.


## 4. Selection Toolbar
After selecting body text, a toolbar appears. Common actions include:

1. Choose highlight color.
2. Insert excerpt (or copy, depending on auto mode).
3. Add a thought.
4. Copy plain text.
5. Create card (requires Weave Deck).
6. Add to vocabulary (requires related capability; see `Er-03b 生词标注与词汇表`).


## 5. Why Highlights Disappear Quickly
Common causes all tie to **not landing in Vault files**.

1. No Markdown open and no Canvas bound—auto insert has nowhere to write.
2. Auto mode off, copied to clipboard only, and never pasted into a note.
3. Inserted content lacks trace links—the reader cannot re-highlight from it.
4. Source note deleted, moved out of Vault, or path invalid.

> Note: The sidebar **Excerpts** list summarizes indexed Vault excerpts. An empty list usually means nothing was successfully written to notes yet.

## 6. How Body Re-Highlight Works
After writing to a note, the reader scans book location info in those excerpts and draws highlights on the matching sentences.

1. Changing color or adding a thought on the same excerpt updates re-highlight when possible.
2. Clicking the book icon in a note or Canvas can jump back to the book (precise positioning may need premium support; see `Er-02d 双向溯源与正文回显`).
3. Deleting that excerpt in the note removes re-highlight in the book.

> Note: Re-highlight depends on note content—not a separate, unrelated highlight store. Editing the note edits this book’s annotations.

## 7. Mobile and Multiple Devices
Excerpts live in Vault files and stay consistent across devices with your sync method.

1. Sync the whole Vault (Obsidian Sync, iCloud, cloud drive Vault sync, etc.).
2. You do not need to force-sync cache under `.obsidian/plugins/weave-epub-reader/`.
3. On a new device, open notes to confirm excerpts first, then open the book to check re-highlight.
