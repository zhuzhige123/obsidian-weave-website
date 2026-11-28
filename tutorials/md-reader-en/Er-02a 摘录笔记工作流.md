Excerpts only become syncable, backlinkable notes when they land in Vault files. The reader uses those backlinks to re-highlight the book. Details below:

## 1. Where Excerpts Can Go
Pick by scenario:

1. **Per-book excerpt Markdown (default)**: Created or appended on highlight—see the next section.
2. **A Markdown note you choose**: Open a `.md`, place the cursor, then turn on top **Auto insert**.
3. **Canvas**: After binding a canvas, excerpts become nodes. See `Er-02e Canvas 脑图摘录`.
4. **Weave Review decks**: With Weave Review installed, fill memory cards. See `Er-04c 与 Weave Review 制卡、增量阅读、AI 联动`.

> Note: The reader does not treat invisible plugin cache as formal notes. Long-term keep requires Vault files.

## 2. Auto-Write Book Excerpt Notes on Highlight
**Auto-write book excerpt notes on highlight** is on by default and is separate from top **Auto insert**.

1. With **Auto insert off**: Highlighting creates a Markdown excerpt named after the book in Obsidian’s **default new-note folder** (or appends if that book already has one).
2. The note carries book backlinks and frontmatter so body re-highlight and the sidebar excerpt list can index it.
3. Turn the setting off if you do not want automatic per-book notes; **Auto insert** and Canvas are unaffected.
4. Design trade-offs: `Er-00a 设计理念下的一些考虑`.

> Note: This is the default “mark and it sticks” path. To write into a specific note you are editing, use Auto insert below.

## 3. Auto Insert: Current Note or Canvas
Top **Auto insert** decides whether highlights write into the **current workflow**.

1. **On (insert)**: Excerpts go to the current Markdown cursor or a bound Canvas—good for a chosen file while reading.
2. **Off**: No insert into the open note; if **Auto-write book excerpt notes on highlight** is still on, highlights still go to the per-book excerpt Markdown.
3. Toolbar **Copy** still puts content on the clipboard for other apps.

## 4. Recommended Flow (Write into a Specific Note)
First time writing into one note while reading:

1. Create or open a Markdown note as this book’s reading journal.
2. Place the cursor where excerpts should land.
3. Open the book and turn on top **Auto insert**.
4. Select text in the body and create a highlight or excerpt from the selection toolbar.
5. Switch back to the note; confirm the excerpt and a clickable book backlink.
6. Click the book icon or link; you should jump back to the matching place in the book.

> Note: Auto insert fails if there is no active Markdown editor. Keep the note tab open with the cursor in the editor. If you only want the automatic per-book excerpt note, leave Auto insert off.

## 5. Selection Toolbar
After selecting body text, common actions include:

1. Pick highlight color.
2. Insert excerpt (into the current note when Auto insert is on) or copy.
3. Add a thought.
4. Copy plain text.
5. Create a card (needs Weave Review).
6. Add to vocabulary (see `Er-03b 生词标注与词汇表`).

## 6. Why a Highlight Disappears
Usually nothing landed in a Vault file.

1. **Auto-write book excerpt notes** is off, Auto insert is off, and no Canvas is bound—nowhere to write.
2. Auto insert is on, but no usable Markdown / Canvas is open—insert fails.
3. Inserted content lacks a backlink, so the reader cannot re-highlight.
4. The source note was deleted, moved out of the Vault, or the path broke.

> Note: The sidebar **Excerpts** list indexes Vault excerpts it can find. An empty list usually means nothing was written successfully.

## 7. How Body Re-Highlight Works
After notes are written, the reader scans book location data in those excerpts and paints the matching sentences.

1. Color changes and thoughts on the same excerpt update the re-highlight when possible.
2. Clicking the book icon in a note or Canvas jumps back (precise locate may need premium—see `Er-02d 双向溯源与正文回显`).
3. Deleting that excerpt in the note removes the re-highlight in the book.

> Note: Re-highlight depends on note content—not a separate highlight store. Editing the note edits the book’s marks.

## 8. Mobile and Multi-Device
Excerpts live in Vault files and follow your sync.

1. Sync the whole Vault (official Sync, iCloud, cloud Vault sync, etc.).
2. Do not force-sync cache under `.obsidian/plugins/weave-epub-reader/`.
3. On a new device, open notes to confirm excerpts exist, then open the book for re-highlight.
