AI Card Generation in the Obsidian Weave main interface is for handing a study note to a large language model and automatically splitting it into multiple memory card drafts. Results go to a preview area first—you can review each card and choose what to import. It suits longer material that needs understanding and summarization before card creation. Here is a detailed guide:

## Open AI Card Generation

AI Card Generation is a separate page in the plugin main interface—not the same as “select text and create a card” in the editor.

1. Open the plugin main interface and use the top-left menu to switch to **AI Card Generation**.
    
2. After entering, the top bar is the toolbar, the middle is the preview area, and the bottom is for switching cards, choosing a target deck, and importing.
    
3. If you are on another sub-view on the same page, switch back to **AI Card Generation**. On desktop, use the left-side buttons; on mobile, you can also enter via the red dot in the top colored dots.
    

> Note: This page focuses on generating cards with a large model. If your notes are already written in a fixed format and you want rule-based splitting and preview, that is a different workflow on the same page and is not covered here.

## Before You Start

Before generating, configure AI services and prepare Markdown notes as input.

1. Open plugin settings, go to **AI Services**, and enter API keys and related info for your provider.
    
2. Confirm you have Markdown notes in your vault with non-empty body text.
    
3. If you have not created any memory decks yet, create one in **Deck Study** first for easier import later.
    

> Note: Without an API key, **Start Generation** may be disabled or prompt you to configure settings first. This is separate from whether Parse Preview needs a parse template.

## Choose Source Notes

AI Card Generation takes a single Markdown note as input and sends its body to the model.

1. Click **File List** in the top bar, search your vault, and select a Markdown file.
    
2. After selection, the toolbar shows the current filename; the plugin remembers your last choice for next time.
    
3. If the recently selected file was moved or deleted, the interface may warn that the file does not exist—just select again.
    

> Note: In AI Card Generation mode you choose a **single note**, not a whole folder batch. The selected file is recorded as the card source document, but usually not at block-level precision.

## Sidebar Mode and Follow Active Document

When AI Card Generation is in an Obsidian sidebar, file selection works slightly differently.

1. After dragging the plugin main interface to a sidebar, the layout switches to a narrow-column-friendly view.
    
2. The top file entry becomes a **Follow Active Document** toggle instead of a full vault file list.
    
3. When enabled, as you switch notes, PDFs, EPUBs, etc. in the main content area, AI Card Generation automatically follows the currently open Markdown as the source note.
    
4. When disabled, you return to manually specifying the source file.
    

> Note: Follow Active Document suits “read and create cards as you go.” For a fixed long document you generate from repeatedly, manually selecting the file in the main content area works better.

## AI Card Generation Settings

Prompts, generation count, question-type ratios, and similar parameters live in **AI Card Generation Settings**.

1. Click the top-left menu and choose **AI Card Generation Settings**.
    
2. Under **Prompts**, choose a built-in system prompt, a user prompt file in the fixed directory, or create/edit custom prompts.
    
3. Under **Card Generation Settings**, adjust generation count, difficulty level, Q&A / cloze / multiple-choice ratios, token limits, and other advanced options.
    
4. Click **Save and Apply** after changes; settings apply to the next generation, and the plugin remembers your usual choices.
    

> Note: Actual card count is capped by the configured limit and may not equal source paragraph count. Question-type ratios must sum to 100% or you cannot save.

## Choose Model and Start Generation

After configuration, confirm the model in the top bar and start generation.

1. Click **AI Model** in the top bar and choose provider and model.
    
2. Confirm the source note is loaded and the current provider has an API key configured in settings.
    
3. Click **Start Generation** in the top-right.
    
4. During generation, the preview area adds cards one by one with progress shown; the top button becomes **Cancel Generation** so you can stop anytime.
    
5. After completion, the top bar may show token usage for this run.
    

> Note: For rate limits, network errors, or insufficient balance, the interface or a notice explains the failure. Retry later, reduce card count, switch models, or check AI service settings.

## Preview and Select Cards

After generation, review content in the preview area before deciding what to import.

1. The main preview shows front and back of the current card; you can reveal the answer like a normal study card.
    
2. The bottom index bar switches cards; tap a number to jump, long-press to select or deselect.
    
3. Newly generated cards are selected by default; deselect unwanted ones via long-press on the index bar or use **Select All / Deselect All**.
    
4. Cards that appear during generation can also be previewed and adjusted while generation continues.
    

> Note: The preview area only changes **whether to import**—it does not rewrite source notes. If a card has format issues, import may warn or fail; deselect that card first.

## Import to Deck

After confirming, write selected cards to the target deck.

1. Choose **Target Deck** at the bottom of the preview area.
    
2. Confirm the import button in the bottom-right shows the current selected count.
    
3. Click **Import N Cards** to save.
    
4. On success, a summary appears; imported cards are removed from the pending selection so you can continue with the rest.
    

> Note: You need at least one selected card and a valid deck before import. If the target deck does not exist, choose again.

## Study Now: Filter Before Import

To review AI cards one by one like a review session before deciding what to keep, use **Study Now**.

1. After generation, click **Study Now** at the bottom of the preview area.
    
2. Choose **Memory Study Mode** or **Exam Study Mode**:
    
    - Memory mode: for Q&A, cloze, and other standard memory cards.
        
    - Exam mode: for filtering multiple-choice from results and linking to exam question groups.
        
3. In the temporary study interface, view cards one by one; completing a rating means **Keep**, deleting means **Discard**.
    
4. After processing all cards, a summary shows kept vs. discarded counts and lets you choose whether to formally import kept cards.
    
5. To review again, return to continue studying; to skip import, end without importing.
    

> Note: **Study Now** suits large batches where you want practice before import. If you are confident in the preview, skip this and import directly from the preview selection.

## History

AI Card Generation keeps recent generation sessions for context recovery.

1. Click **History** in the top bar to view the last 5 generation records.
    
2. Each record usually includes source filename, prompt file, and card count.
    
3. Click a record to restore that run’s source content, settings, and preview results for comparison, supplemental import, or re-selection.
    
4. With no history, the entry may be empty or disabled.
    

> Note: History is stored locally and covers only a limited recent count—not unlimited cloud backup. Parse Preview does not use the same AI generation history.

## Difference from Editor Card Creation

The plugin also has editor-side abilities like “create card from selected text” for quick single-segment cards.

1. AI Card Generation main interface: whole notes, batch preview, unified import.
    
2. Editor selection / segment card creation: current selection only, shorter flow, different interface.
    

> Note: Both can be used together—for example, AI Card Generation for long documents, then segment creation for local additions. Card format rules are in `We-01g 卡片题型`.
