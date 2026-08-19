The reader finishes books and keeps excerpts. Spaced-repetition cards, Incremental Reading schedules, and AI splitting are handled by other Weave-family plugins. These integrations do not consume the reader’s own premium license slot, but require the matching plugins installed; AI also needs your own API keys configured. Details below:

## 1. Excerpt to Card
1. Select a passage in the book.
2. On the toolbar, choose **Create card**—content fills Weave Deck’s memory card creation flow.
3. After save, cards can carry reader traces to jump back from study UI.
4. Without Weave Deck installed, the entry is unavailable or prompts missing capability.


## 2. Incremental Reading
If the separate Incremental Reading plugin is installed:

1. From a chapter menu in the TOC, choose **Add to Incremental Reading**.
2. On success, the chapter enters Incremental Reading tasks—not just a reader bookmark.
3. If not installed or service not ready, you are told the feature is unavailable and nothing is written to tasks.


## 3. AI Panel and Selection Search
1. The reader offers selection search, AI panel, and similar entries (Help / tools menu—per UI).
2. Custom AI splitting depends on split features configured on the Weave Deck side.
3. With no split feature available, you are told nothing is configured.
4. AI sends your selection to third-party models you configure—do not send text that must stay private.

> Note: Reader AI is not blocked by **reader premium** alone; without Weave Deck and API keys, the panel cannot help.

## 4. Vocabulary List
Adding selections to the vocabulary list and marking words in body text: see `Er-03b 生词标注与词汇表`. Review still happens in Weave Deck memory study.

## 5. How Licensing Works
1. Reader premium: Timeline, precise bidirectional tracing, paragraph mode, reading lists, etc.—reader activation code, or inherit from activated Weave Deck.
2. Cards / Incremental Reading / AI: Do not separately deduct reader premium slots, but each plugin’s own requirements still apply.
3. Reader only, no Weave Deck: Integration entries lack a host.


## 6. Recommended Combinations
1. **Read and take notes only**: Reader + Markdown / Canvas—Weave Deck optional.
2. **Read and spaced review**: Reader + Weave Deck—highlight to card or collect vocabulary.
3. **Long books chapter by chapter**: Reader + Incremental Reading plugin—send chapters from TOC.
4. **All three**: Install all—reader as entry, the other two as processing layers.
