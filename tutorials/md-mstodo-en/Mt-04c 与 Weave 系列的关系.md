MS To Do Sync and Weave Deck / EPUB Reader / Incremental Reading share a **developer**, but MS To Do Sync is **not** part of the Weave product bundle and has **no code dependency**. Install it alone. Details below:

## 1. What “standalone” means
1. Without any Weave plugin, MS To Do Sync still does login, two-way sync, inbound capture, and backlinks.
2. It does not share Weave activation / premium entitlements; it ships under its own license (GPL-3.0-or-later) and release channel.
3. Repo, releases, and Issues live in `obsidian-microsoft-todo-sync`.

## 2. Why tutorials appear on the Weave site
1. The site tutorial shell already hosts multiple plugin tabs (Deck / Reader / IR…).
2. These articles are **same-developer docs for an independent plugin**, with ZH/EN switching.
3. Switch the top tab to **MS To Do Sync** to browse only this catalog; Weave tutorials are unaffected.

## 3. Optional overlap with reading / cards
1. Write study tasks in EPUB Reader notes or any note, tag `#mtd-sync`, and execute them in To Do.
2. Weave Deck spaced repetition and To Do checklists are different jobs—no forced bridge.
3. If you also use Tasks queries, follow `Mt-03c` line order.

## 4. Install path cheat sheet
| Plugin | Typical folder |
|---|---|
| MS To Do Sync | `.obsidian/plugins/ms-todo-sync/` |
| Weave EPUB Reader | `.obsidian/plugins/weave-epub-reader/` (confirm ID) |
| Weave Deck | per community page / manifest |

## 5. Getting help
1. Prefer this tab’s tutorials and in-plugin settings copy.
2. Bugs/requests → GitHub Issues.
3. Site chat / email also work—say you mean **MS To Do Sync** so it is not confused with Weave features.
