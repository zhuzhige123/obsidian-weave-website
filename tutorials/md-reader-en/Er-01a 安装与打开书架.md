Weave Reader is the reader in the Obsidian Weave plugin family. It opens books in Obsidian—including EPUB, TXT, FB2/FBZ, MOBI, AZW3, CBZ, and PDF—and manages imports, covers, progress, and reading status through **My Bookshelf**. It works on its own; after installing Weave Review, you can also connect card creation, Incremental Reading, and AI. Details below:

## 1. Install and Enable
We recommend installing from the Community Plugins marketplace.

1. Open Obsidian **Settings → Community plugins → Browse**.
2. Search for **Weave Reader**, then install and enable it.
3. After enabling, a bookshelf icon appears in the left ribbon. Click it to open **My Bookshelf**.
4. You can also run **My Bookshelf** from the command palette.

> Note: Minimum Obsidian version is 1.8.7. Available on desktop and mobile.

## 2. Manual Installation
If the Community marketplace is unavailable, install manually from the GitHub release package.

1. Download the release package that matches the version in `manifest.json`, and obtain `main.js`, `manifest.json`, and `styles.css`.
2. Copy them to `.obsidian/plugins/weave-epub-reader/` in your Vault.
3. Restart Obsidian, then enable **Weave Reader** under **Settings → Community plugins**.

> Note: For manual installation, all three files must sit in the same plugin folder and match each other in version.

## 3. Supported Book Formats
The bookshelf can catalog and open the formats below. Book files must first be placed in the current Vault.

1. Opens in the reader’s own interface: EPUB, TXT, FB2 / FBZ, MOBI, AZW3, CBZ.
2. PDF appears on the bookshelf but opens in Obsidian’s built-in PDF viewer, not the reader’s custom text renderer.
3. TXT is split into chapters by paragraph, making TOC navigation easier.

## 4. Open the Bookshelf and Add Books
On first use, the bookshelf is usually empty. Two common ways to add books: **scan files already in the Vault**, or **import from outside the vault**.

1. Click the bookshelf icon in the ribbon, or run the **My Bookshelf** command.
2. An empty bookshelf prompts you: no books or comics yet—you can scan Vault files and add them.
3. **Scan Vault**: Click **Scan Vault to Add Books**, or open **Scan Vault for Books and Comics** from the menu; check files to add. Items already on the bookshelf are marked as already added.
4. **Import from outside the vault**: In the bookshelf menu choose **Import books from outside vault**, pick EPUB / TXT / MOBI (and other supported formats) with the system file picker; the plugin copies them into a Vault folder and adds them to the shelf. Multi-select is supported.
5. After a successful add, cover, title, and progress appear on the shelf.

> Note: The first time you open the bookshelf, an onboarding page may introduce multi-format reading, shelf views, reading layouts, excerpt backlinks, and links to the site and in-reader tutorial. Outside-vault import suits books still in a Downloads folder; you still choose what joins the shelf—nothing auto-dumps the whole library onto it.

## 5. Bookshelf Display Modes
The bookshelf supports several layouts. Default is **Follow location**. Switch from the bookshelf menu or settings.

1. **Follow location**: Reading calendar in the sidebar; bookshelf home in the main content area (next section).
2. **Reading calendar**: Browse the shelf timeline by month (e.g. “September” groups) to revisit reading footprints.
3. **Card grid**: Covers plus key info (author, progress, and more).
4. **Banner cards**: Horizontal cover banners with reading status and progress (premium).
5. **Covers only**: A pure cover wall—less info, more browsing (premium).

> Note: Sidebar and main content favor different widths. **Follow location** picks a suitable form for where the pane sits, without leaving the home shell.

## 6. Content-Area Bookshelf Home
When the bookshelf sits in Obsidian’s **main content area**, you get bookshelf home—not only a narrow list.

1. The top bar switches among **Shelf / Notes / Stats** (mobile may use top dots).
2. **Shelf**: Status, sort, and filters; reading-list shortcuts; recent reading in the bottom bar. Display mode only changes card / calendar style inside home.
3. **Notes**: Entry to the full-bookshelf excerpt timeline (premium; locked state shows a prompt).
4. **Stats**: Favorites, reading portrait, completion footprints, yearly heatmap, and more (premium; may be time-limited).
5. Optionally show a **Continue reading** info card at the top, or the bookshelf activity heatmap (premium; heatmap and info card are usually mutually exclusive).

> Note: In the sidebar, the reading calendar is better for quick finds. For stats and cross-book note trails, drag the bookshelf into the main content area. To group books by theme, see `Er-01d 书架书单`.

## 7. Open a Book
Once a book is on the bookshelf, you can start reading.

1. Click the title or cover to open the reader.
2. For side-by-side comparison, choose **Open in new tab** from the book menu.
3. If you are already viewing a supported book file in the Vault, you can also run **Open Weave Reader** from the command palette.
4. If the source file is moved or deleted, refreshing the bookshelf cleans up stale entries and may prompt that the book was removed from the shelf.

## 8. Common Book Menu Actions
Open the menu on a bookshelf book for everyday organization.

1. **View full book info**: Author, word count, chapter count, and more.
2. **Rename**: Syncs to the bookshelf, reader tab, and bookmark notes.
3. **Mark as finished** or remove that mark.
4. **Custom book cover**: Pick an image from the Vault, or restore the built-in cover.
5. **Remove from bookshelf**: Removes from the shelf only; does not delete the book in the Vault.
6. **Delete book file**: Deletes the book file in the Vault; excerpt notes remain in their original Markdown files.

## 9. Search and Filter
When you have many books, use the top search bar.

1. Type keywords such as the book title.
2. You can also use property prefixes, e.g. `status:`, `author:`, `created:`.
3. Reading status includes **Not started**, **Reading**, and **Finished**.

## 10. Relationship with the Main Weave Review Plugin
The reader can handle reading, the bookshelf, and basic excerpts on its own.

1. Without Weave Review installed, you can still read, manage the bookshelf, and write excerpts to Markdown / Canvas.
2. With Weave Review installed, you can optionally connect card review, Incremental Reading, AI menus, and writing excerpts to decks.
3. If Weave Review is activated, the reader’s premium support can inherit that license—you do not need a separate reader activation code.
