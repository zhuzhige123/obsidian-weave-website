Weave Incremental Reading turns “read later” into a schedulable, resumable queue. This page explains why it is designed this way—and what it is not.

## Saving is not reading
Bookmarks and clip folders store things. They rarely answer what to read today, how to handle overdue items, how to continue a long source split into many pieces, or how to return to the exact place you left.

This plugin turns materials into **reading points**, uses a **calendar** for daily rhythm, and keeps **resume links** so the queue moves.

## Three design principles
1. **Decide on the calendar; read in the source.** The calendar handles day selection, load, priority, progress, and reschedule. Opening a point jumps to Markdown / PDF++ / Canvas / web / EPUB. The path is queue + resume—not a second daily “in-plugin reader.”
2. **One primary capture path, many shortcuts.** Daily capture goes through calendar **Add link** (commands may say Add reading target). Import is for whole documents / book outlines; folder subscription is for an ongoing clip inbox (premium).
3. **Incremental reading ≠ spaced repetition (FSRS).** This plugin owns what to read, when it returns, and how to resume. Weave Deck owns what to remember and when to review. Scheduling here means reading-point due dates, not FSRS.

## Why topics (`.irdeck`)
Topics group points by plan and live as vault `.irdeck` files—backupable and syncable. Open a topic to switch between topic view and calendar. The topic chip on the month header filters All vs one topic. Keep names stable so one plan does not fragment.

## Free baseline vs premium depth
The free loop is **calendar + Markdown points + Add link + basic scheduling + continuous reading**. PDF/EPUB bulk chapters, subscription, deep strategy knobs, timers, analytics, and associated notes are premium extensions.

## Do not treat these as the daily path
1. Legacy main reading view — removed; redirects to the calendar.
2. Paragraph reading workbench — experimental; use the calendar sidebar.
3. Tag groups as a primary workflow — still being improved; prefer topics, priority, and basic scheduling.
4. FSRS as this plugin’s scheduler — belongs to Weave Deck.
