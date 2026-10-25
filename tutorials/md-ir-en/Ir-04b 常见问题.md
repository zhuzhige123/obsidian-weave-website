Find by symptom. If stuck, open a GitHub Issue with Obsidian version, plugin version, and platform.

## Can’t find the calendar
Command palette: Open incremental reading calendar. Confirm the plugin is enabled. Legacy “main reading” entries should redirect to the calendar—use the calendar as the only main UI.

## New topic missing from search briefly
Reopen the calendar sidebar; confirm the `.irdeck` is under the data root `points/`; use data management to verify readability.

## Paste not recognized / import unavailable
Check link completeness; don’t mix md/pdf/epub in one import batch. PDF/EPUB import needs premium; EPUB outlines need Weave EPUB Reader.

## Subscription ignores files or schedules oddly
Confirm a Markdown folder, bound topic, and enabled rule; run Update subscribed folders manually. Distinguish Add to today vs Schedule normally—only the latter spreads due across the horizon.

## Missing source / won’t open
Check moves, renames, deletes; verify PDF++ / EPUB / Canvas node / block ID still valid. EPUB resume needs Weave EPUB Reader; highlights alone are not reading points.

## PDF opens but not the selection
Add via PDF++ selection/bookmark links; path-only points can’t restore a precise selection.

## Rarely returns / returns too often
Check Processing vs Reading list and interval-related settings; suspended or archived?; daily cap / time budget blocking release? This plugin is not FSRS—use Weave Deck for spaced repetition.

## Tag groups do nothing
Still being improved—use topics, priority, and basic scheduling instead.

## Premium locked / Deck licensed but IR still locked
Activate under Settings → License, or confirm Weave Deck inheritance then reload plugins. Advanced preview shows entries; activation is still required to use them.

## Topics missing after machine switch
Did you sync the data root (`weave Incremental reading/` by default)? Does the settings path match the real folder?
