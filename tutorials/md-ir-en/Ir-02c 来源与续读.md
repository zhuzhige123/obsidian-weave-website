Each reading point stores a stable resume link and source kind. Opening from the calendar routes by type and locates the original position when possible.

## Principles
1. Prefer locatable info at create time (block ID, page selection, node ID, CFI, …).
2. Resume quality depends on built-in or companion capabilities.
3. Moves/renames can cause “missing source”—fix links or recreate the point.

## Obsidian Markdown
Add via `[[Note#^blockId]]`, line anchors, Current location, or selection quick-create. Resume opens the note and scrolls to the block/line. **Markdown focused reading** (settings, free) dims surrounding blocks for focus.

## PDF (PDF++)
Add via PDF++ selection/bookmark links, or import chapters from an outline (premium). Resume opens the PDF and resolves page/selection anchors. Precise selections work best with PDF++.

## Canvas nodes
Add via node menu or `[[board.canvas#^nodeId]]`. Resume opens the canvas and highlights by node ID. Requires built-in Obsidian Canvas.

## Web (Obsidian browser)
Add via Web Viewer “Add to incremental reading” or paste `https://…`; usually creates a reading-note carrier. Resume opens the URL in Obsidian’s browser.

## Weave EPUB Reader
Add from a reader selection or paste an EPUB location link. **Highlights alone do not become reading points.** Resume uses `obsidian://weave-epub-reader` to open at CFI/chapter. Requires Weave EPUB Reader.

## Associated notes (premium)
Context menu → Associated notes. PDF/EPUB use curated links; Markdown/web use outbound links from the source note. Without activation the entry may be hidden or locked.
