### Why import books manually, instead of auto-scanning the vault and adding every book to the bookshelf?

Books on the bookshelf are ones you intend to read carefully—deep reading. That choice is yours. If you need a library catalog, use the official Bases database or another plugin’s database features. Add an attachment path or book link in that database; opening it can default to this reader plugin.


### Why was auto-saving reading position removed?

This reader is not like a standalone ebook app. Many choices are different inside Obsidian. Using it here leans toward output: Markdown, Canvas, Excalidraw, Weave Deck, and other plugins. You often jump from excerpt backlinks into different places in the book to check the source text. Auto-saving position easily overwrites the last reading position by mistake. Reading progress and last viewed location should not be mixed up. Manually updating the reading position also feels closer to slipping a bookmark into a physical book—and that feedback is better.


### Why not auto-create a Markdown file for excerpts when you highlight text?

Auto-creating an excerpt Markdown file on highlight would match ordinary readers. Many designs differ by purpose and environment; readers are no exception. In Obsidian—a highly free note vault—excerpts can live in any file, serve as sources for an article with jumps back to the original text, or form a reading journal across linked Markdown files. Many other layouts that fit how you think are possible through Obsidian’s strong editing experience and its plugins.
So you choose: create a Markdown file in a way that fits Obsidian’s design philosophy to hold excerpts; or choose a Canvas file for mind-map excerpts…
In the end, the reader gathers excerpts scattered across files and shows them in the book text by excerpt type, links related note nodes, and traces back to the book body.

### Integrate AI?

At this stage, we do not plan to embed AI in the reader. The vision is a clean, immersive reading environment in Obsidian, with natural interactions and a comfortable text experience. We do not aim to meet needs like auto-parse, summary, or chat-style assistance through AI inside the reader. In most cases that would disrupt reading pace, split attention, and interrupt deep thinking.

If you need those capabilities, copy text, export the current chapter as Markdown, or use the plugin API for chapter content and excerpts, then work with other AI-capable plugins for custom automation. The reader’s API is designed for that.


### Why was reading-time tracking removed?

As above, some habits of ordinary readers do not fit Obsidian’s note environment. Ordinary readers focus on excerpts and ideas during a steady reading session, so recording duration has clear value. In Obsidian, pausing on a page to write a note is common; so is jumping from an excerpt link in a Markdown file back into the book to review the text.
Reading-time statistics then have little value.
A better approach is a timer plugin or an external Pomodoro-style tool, then add the cumulative time into a numeric book-management property created with official Bases.
