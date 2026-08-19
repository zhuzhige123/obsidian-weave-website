The Obsidian Weave memory study interface is where you actually review memory cards. After entering from Deck Study, you progress in a **view question → show answer → rate** loop until the session ends. Here is a detailed guide:

## Memory Study Interface
Use this to start today’s review from a memory deck.

1. Open the plugin main interface, enter **Deck Study**, and switch to memory decks.
2. Click the target deck card to enter memory study.
3. If that deck is finished for today, has no due cards, or is empty, a prompt appears instead of entering study directly.
4. When nothing is due, follow prompts to study ahead, view statistics, or take other next steps.
5. You can also choose **Study Ahead** from the deck menu to include cards not yet due but within the ahead window.

> Note: Memory study differs from Deck Study. Deck Study chooses which deck to practice; memory study reviews cards one by one and rates them.

## Interface Layout
After entering, the screen divides into a few areas—knowing them makes operation smoother.

1. **Top**: current deck name and session progress, e.g. card X of Y.
2. **Middle**: current card content. Before showing the answer, you usually see front or stem; after showing answer, back, explanation, cloze answers, etc.
3. **Bottom**: first **Show Answer** or **Confirm Answer**; after reveal, the four rating keys **Again**, **Hard**, **Good**, **Easy**.
4. **Right**: study toolbar—edit, delete, set reminder and priority, view card info, open more settings. On mobile, most of this moves to the top menu.

> Note: Remember **middle for content, bottom for rating, right for helpers**—most actions land in those three areas.

## Content Preview and Editing
Card content preview in memory study and the edit experience when opened both use official Obsidian capabilities—not a separate custom editor.

1. In preview, you see rendering close to native Obsidian.
2. In edit mode, you use the official Obsidian editing experience and can change content with normal Markdown habits.
3. Because preview and edit follow the official chain, most Obsidian plugins and community capabilities work—for example:
   - Images, audio, video, and other media
   - Components and custom display
   - Mind map plugins
   - Excalidraw
   - PDF++ excerpts and related display
   - Math formulas
   - And more content relying on Obsidian native edit/preview ecosystem
4. Editing and viewing cards in Weave therefore feels closer to “writing and reading notes in Obsidian” than entering another unfamiliar editor.

> Note: Cards still live in Weave deck data; what changed is preview and edit hook into official capabilities for broader ecosystem compatibility.

## Edit with Markdown Mindset; Types Parsed from Content
Weave has no separate “Q&A template,” “cloze template,” or “multiple-choice template.” Question type is not “pick template then fill”—it is parsed dynamically from patterns in card Markdown when saving and previewing.

1. When editing cards, write content directly in Markdown mindset.
2. Plain Q&A: write front and back like normal Markdown.
3. Cloze: on Q&A content, add highlight-style Markdown around hidden parts; after save and preview it auto-recognizes as cloze. Default common form is `==hidden text==`; symbols can be adjusted in plugin settings.
4. Multiple choice: organize options and answers with agreed Markdown/marker patterns; save and preview auto-recognizes as multiple choice—no template switch.
5. The study interface displays and accepts answers by parsed type—for example cloze with **Show Answer** or **Type Answer**, multiple choice with select then **Confirm Answer**.

> Note: This matches Obsidian Markdown editing—you change content patterns; the plugin recognizes types. Standard formats and medical examples for all three are in `We-01g 卡片题型`.

## Study Hints: Official Obsidian Footnotes
Hints in memory study follow official Obsidian footnote syntax—not a separate hint field.

1. Write footnotes in card Markdown in official format—for example `[^1]` in body and `[^1]: hint text here` at the end.
2. In study preview, hover the footnote marker for a hint popup, or click to jump to hint content.
3. Hints and question live in the same Markdown; editing matches footnotes in Obsidian notes.

> Note: To give yourself a clue when recall stalls, add official footnote hints—no extra hint syntax to learn.

## Image Mask
Use this for atlases, anatomy diagrams, etc. where you hide a region, recall, then reveal.

1. Put an image in the card first.
2. While editing, place the cursor on the image line and use editor menu **Weave Image Mask**, or command palette **Edit Image Mask**, to add mask regions.
3. On supported image files, right-click **Weave Image Mask** also works.
4. In memory study, masked images hide regions first; **Show Answer** reveals masks.
5. During study you can click individual masks to reveal or cover again as needed.

> Note: Image masks suit atlas localization and structure ID; text cloze still prefers highlight symbols—they serve different purposes.

## Auto-Play Audio
Use this for word cards and other cards with pronunciation during review.

1. When card content includes audio (e.g. word pronunciation), open **Auto-play Media** in memory study **More** on the right.
2. Choose when to play: on card switch or when showing answer.
3. Choose scope: first only or all.
4. Good for English words and pronunciation follow-along; especially common with word cards added via fingertip translation.

> Note: Auto-play changes listening timing—it does not replace rating. Turn off **Auto-play Media** when you do not want audio.

## Basic Flow for One Card
The core of memory study is this loop.

1. Read the current card front or stem and recall first—do not rush to reveal the answer.
2. When ready, click **Show Answer** at the bottom. For multiple choice and cloze in **Type Answer** mode, the button may read **Confirm Answer**.
3. After reveal, rate with one of four keys by recall quality:
   - **Again**: not remembered—comes back soon.
   - **Hard**: barely recalled, still difficult.
   - **Good**: normal recall—most common choice.
   - **Easy**: very easy—interval stretches longer.
4. Each rating key often shows predicted interval, e.g. minutes or days, to help choose.
5. After rating, the next card appears automatically until the session queue ends.

> Note: Ratings have no absolute standard. Use **Good** as baseline: clearly harder → Hard or Again; clearly too easy → Easy.

## Common Bottom Actions After Revealing Answer
Besides rating, two actions are common after the answer shows.

1. **Return to Preview**: hide the answer and go back to preview only—does not rate this card.
2. **Undo**: undo the last rating; button may show remaining undo count when available.

> Note: Return to Preview suits revealing too early and wanting another recall attempt; Undo suits mis-pressed rating keys.

## Cloze and Multiple Choice Differences During Study
After content is parsed, the first bottom step differs slightly by type.

1. Plain Q&A: usually **Show Answer** then rate.
2. Multiple choice: select options, **Confirm Answer**, then rate.
3. Cloze can switch answer mode:
   - **Show Answer**: reveal cloze content then rate.
   - **Type Answer**: type your answer, confirm, then rate.
4. Switch answer mode in the bottom bar or more settings as needed.

> Note: You do not pick a template during study—how you wrote in edit is how study presents. What sets the next review time is still the four ratings.

## Modify Current Card During Study
Mid-session you can handle the current card without leaving the whole session.

1. **Edit**: open official edit to change card Markdown; keep familiar Obsidian patterns and compatible plugins, then return to preview and continue.
2. **Reminder**: set a review reminder for the current card.
3. **Priority**: adjust to Low, Medium, High, Urgent, etc.
4. **Deck**: change the current card’s deck membership.
5. **View**: open fuller card information.
6. **Delete**: delete the current card. With direct delete enabled, action is more immediate—use carefully.

> Note: Edit, deck change, and priority change the card itself; rating changes its review schedule. If you turn Q&A into cloze by adding highlights, save and preview re-identifies the type from new content.

## Recycle Card
Use this when you do not want to delete yet but do not want the card in the current study queue.

1. Find **Recycle Card** in more settings.
2. After applying, the current card gets a recycle tag and leaves the current study queue.
3. Recycle tags support `#回收` or `#recycle`.
4. The card is not lost. Remove the recycle tag from content later to study again.

> Note: Recycle is not delete. Delete removes the card; recycle temporarily removes it from the queue for later edit or study.

## Return to Source Document
When a card has trace info, study can jump back to original context.

1. Expand source-related info at the top.
2. Via source document / source block entries, jump to note, PDF, EPUB, etc.
3. Some source block text and advanced trace capabilities may be advanced features.

> Note: Reviewing the card face is the main line; returning to source is support. When the card face fails, checking the source document is often more effective.

## More Settings
In **More** on the right, adjust session behavior.

1. Auto-play media: whether to auto-play audio/video in cards, when, and first only vs. all. Details in **Auto-Play Audio** above.
2. Card order: sequential or shuffled study.
3. Option order: sequential or shuffled multiple-choice options.
4. Show study timer: whether to show time on current card, etc.
5. Timeout pause, show content tags, show answer-mode switch, enable direct delete, etc. can also be toggled here.

> Note: These settings affect study experience—they do not replace rating. Day to day, **Show Answer** and the four rating keys matter most.

## After Finishing the Session
When the session queue completes, memory study ends and returns to Deck Study flow.

1. If cards were actually reviewed, a study achievement settlement modal usually appears.
2. Settlement may show reviewed count, new cards learned, study duration, retention rate, etc.
3. Click **Got it** to finish.
4. If exam question groups exist, settlement may offer continuing to an exam group for a test—that is optional, not required for memory study.

> Note: Closing study mid-way without effective review usually skips settlement.

## What to Do When “Done for Today”
If clicking a deck prompts that today is finished, or no cards are due, the deck is not broken.

1. **Finished for today**: today’s study quota or due tasks for that deck are complete.
2. **No due cards**: the deck has cards but none are scheduled for review yet.
3. **Deck is empty**: no learnable cards yet—create or import cards first.
4. Use **Study Ahead** if needed, or open deck analysis to decide whether to add more new cards.

> Note: Memory study advances by due dates and limits—not every open lets you finish the entire deck. Use **Study Ahead** in the deck menu to study early.
