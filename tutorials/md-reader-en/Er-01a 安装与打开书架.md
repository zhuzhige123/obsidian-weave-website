Weave EPUB Reader is the reader in the Obsidian Weave plugin family. It opens books in Obsidian—including EPUB, TXT, FB2/FBZ, MOBI, AZW3, CBZ, and PDF—and manages imports, covers, progress, and reading status through **My Bookshelf**. It works on its own; after installing the main Weave plugin, you can also connect card creation, Incremental Reading, and AI. Details below:

## 1. Install and Enable
We recommend installing from the Community Plugins marketplace.

1. Open Obsidian **Settings → Community plugins → Browse**.
2. Search for **Weave EPUB Reader**, then install and enable it.
3. After enabling, a bookshelf icon appears in the left ribbon. Click it to open **My Bookshelf**.
4. You can also run **My Bookshelf** from the command palette.

> Note: Minimum Obsidian version is 1.8.7. Available on desktop and mobile.

## 2. Manual Installation
If the Community marketplace is unavailable, install manually from the GitHub release package.

1. Download the release package that matches the version in `manifest.json`, and obtain `main.js`, `manifest.json`, and `styles.css`.
2. Copy them to `.obsidian/plugins/weave-epub-reader/` in your Vault.
3. Restart Obsidian, then enable **Weave EPUB Reader** under **Settings → Community plugins**.

> Note: For manual installation, all three files must sit in the same plugin folder and match each other in version.

## 3. Supported Book Formats
The bookshelf can catalog and open the formats below. Book files must first be placed in the current Vault.

1. Opens in the reader’s own interface: EPUB, TXT, FB2 / FBZ, MOBI, AZW3, CBZ.
2. PDF appears on the bookshelf but opens in Obsidian’s built-in PDF viewer, not the reader’s custom text renderer.
3. TXT is split into chapters by paragraph, making TOC navigation easier.


## 4. Open the Bookshelf and Add Books
On first use, the bookshelf is usually empty.

1. Click the bookshelf icon in the ribbon, or run the **My Bookshelf** command.
2. An empty bookshelf prompts you: no books or comics yet—you can scan Vault files and add them.
3. Click **Scan Vault to Add Books**, or open **Scan Vault for Books and Comics** from the menu.
4. In the results, select files to add. Items already on the bookshelf are marked as already added.
5. After a successful add, cover, title, and progress appear in the list or grid.


## 5. Bookshelf Display Modes
The bookshelf supports several layouts—good for wide screens, sidebars, or cover-only browsing.

1. **List details**: Emphasizes title, author, tags, and progress.
2. **Card grid**: Shows covers and key info.
3. **Covers only**: A pure cover wall.
4. **Follow location**: List in the sidebar, card grid in the main content area.


## 6. Open a Book
Once a book is on the bookshelf, you can start reading.

1. Click the title or cover to open the reader.
2. For side-by-side comparison, choose **Open in new tab** from the book menu.
3. If you are already viewing a supported book file in the Vault, you can also run **Open EPUB Reader** from the command palette.
4. If the source file is moved or deleted, refreshing the bookshelf cleans up stale entries and may prompt that the book was removed from the shelf.


## 7. Common Book Menu Actions
Open the menu on a bookshelf book for everyday organization.

1. **View full book info**: Author, word count, chapter count, and more.
2. **Rename**: Syncs to the bookshelf, reader tab, and bookmark notes.
3. **Mark as finished** or remove that mark.
4. **Custom book cover**: Pick an image from the Vault, or restore the built-in cover.
5. **Remove from bookshelf**: Removes from the shelf only; does not delete the book in the Vault.
6. **Delete book file**: Deletes the book file in the Vault; excerpt notes remain in their original Markdown files.


## 8. Search and Filter
When you have many books, use the top search bar.

1. Type keywords such as the book title.
2. You can also use property prefixes, e.g. `status:`, `author:`, `created:`.
3. Reading status includes **Not started**, **Reading**, and **Finished**.


## 9. Relationship with the Main Weave Plugin
The reader can handle reading, the bookshelf, and basic excerpts on its own.

1. Without Weave installed, you can still read, manage the bookshelf, and write excerpts to Markdown / Canvas.
2. With Weave installed, you can optionally connect card review, Incremental Reading, AI menus, and writing excerpts to decks.
3. If the main Weave plugin is activated, the reader’s premium support can inherit that license—you do not need a separate reader activation code.
