### Why add books to the bookshelf deliberately, instead of auto-scanning the vault and adding every book?

Books on the bookshelf are ones you intend to read carefully—deep reading. That choice is yours. You can add them by scanning the Vault and checking items, importing files from outside the vault, or opening a supported file then launching the reader. If you need a full library catalog, use the official Bases database or another plugin’s database features: add an attachment path or book link, and opening it can default to this reader plugin.

### Why isn’t auto-saving reading position the default design?

This reader is not like a standalone ebook app. Many choices are different inside Obsidian. Using it here leans toward output: Markdown, Canvas, Excalidraw, Weave Review, and other plugins. You often jump from excerpt backlinks into different places in the book to check the source text. Treating every jump as “last reading position” easily overwrites the resume point by mistake. Reading progress and last viewed location should not be mixed up.

A closer match to a physical bookmark is pinning a **resume** spot: select a paragraph, pin an exact anchor, and reopen to locate with a brief highlight. Current-page bookmarks suit multiple marks in one chapter. For steady forward reading, you can still enable “auto-save after N continuous pages” in settings—that serves linear reading, not backlink browsing.

### Excerpts on highlight: why create a per-book Markdown by default, while still allowing free destinations?

Ordinary readers often have only a built-in highlight store. In Obsidian you usually need both: a highlight that leaves a backlinkable note immediately, and the freedom to write excerpts into any article, Canvas, or deck.

So the reader splits the paths:

1. **Auto-write book excerpt notes on highlight** (settings, on by default): With top **Auto insert** off, highlighting creates (or appends to) a Markdown excerpt named after the book in Obsidian’s default new-note folder, with book backlinks and body re-highlight. Good for “mark first, organize later.”
2. **Top Auto insert**: When on, highlights prefer the **currently** open Markdown cursor (or a bound Canvas)—your chosen workflow. Good for writing into a specific note while reading.
3. You can still create any Markdown, multi-file reading journals, or mind-map Canvas; the reader gathers scattered excerpts and re-highlights them in the book. Turn off **Auto-write book excerpt notes on highlight** if you do not want automatic per-book notes.

Free destinations did not go away; default per-book notes only make the first highlight stick.

### Integrate AI?

At this stage, we do not plan to embed AI in the reader. The vision is a clean, immersive reading environment in Obsidian, with natural interactions and a comfortable text experience. We do not aim to meet needs like auto-parse, summary, or chat-style assistance through AI inside the reader. In most cases that would disrupt reading pace, split attention, and interrupt deep thinking.

If you need those capabilities, copy text, export the current chapter as Markdown, or use the plugin API for chapter content and excerpts, then work with other AI-capable plugins for custom automation. The reader’s API is designed for that.

### Why isn’t a “reading-time dashboard” the core?

As above, some habits of ordinary readers do not fit Obsidian’s note environment. Ordinary readers often assume a calm, continuous session and treat wall-clock duration as the main metric. In Obsidian, pausing on a page to write a note is common; so is jumping from an excerpt link in a Markdown file back into the book to check one sentence, then leaving again. Counting every stay as “time spent reading” easily mixes browsing, note-taking, and focused reading.

So the reader does not chase a heavier duration dashboard. For focus rhythm, use the in-reader Pomodoro focus timer (accumulated from real reading time). For “how long left in this chapter / book,” use the remaining reading-time sticker. For reviewing footprints, the content-area bookshelf home **Stats** view and activity heatmap cover common retrospectives. Richer metrics can still be built with Dataview or official Bases.

### Why not built-in audiobook / TTS?

Full-book listen mode and the reader’s main path—read, excerpt, note—do not fit together cleanly: listening while selecting, writing thoughts, and tracing backlinks rarely stays natural. Shipping a TTS / audiobook stack also pulls the reader toward a media player and away from focused text and output.

If you need it, use system selection speech, export the current chapter as Markdown, or hand chapter text to another TTS / audiobook plugin via the public API.

### Why not built-in RSS?

RSS is feed intake and subscription management—a different product line from opening a book, immersive reading, and writing excerpts. Packing feeds, unread queues, and refresh into the reader would dilute the bookshelf and body experience, and would rarely beat a dedicated RSS tool.

If you want subscriptions inside Obsidian, we recommend [qiaomu AI RSS](https://github.com/joeseesun/qiaomu-ai-rss) or similar specialized plugins; materials you want to read deeply can then be imported or connected to this reader and Incremental Reading workflows.

### What else is deliberately not built in?

The boundary stays on focused reading and excerpts; extensions go to better-fitting tools. For example: dictionaries to Finger and similar look-up plugins; deep PDF annotation to Obsidian’s built-in viewer or PDF++ (the bookshelf can still catalog PDFs); skins and background colors follow Obsidian themes and CSS snippets. The public API, Markdown export, and collaboration with Canvas / Excalidraw / Weave Review / Incremental Reading are the extension surface—re-implementing what the ecosystem already does well is not the direction.
