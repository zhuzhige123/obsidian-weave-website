Batch parsing in the Obsidian Weave main interface is for notes that already contain multiple cards in a fixed format—you split them by rules, preview first, then import to a deck. It does not call a large model; it reads Markdown using parse templates (delimiters or regex) you configure in the plugin and organizes matches into cards pending confirmation. It suits AI chat exports, standardized card drafts, and notes split by divider lines. Here is a detailed guide:

## Open Parse Preview

The batch parsing entry is the **Parse Preview** sub-view on the **AI Card Generation** page. It shares the same main interface as AI Card Generation but the workflows are independent.

1. Open the plugin main interface and use the top-left menu to switch to **AI Card Generation**.
    
2. Switch to **Parse Preview**. On desktop, use the left-side buttons; on mobile, you can also enter via the blue dot in the top colored dots.
    
3. After entering, the top bar shows **File/Folder** and **Parse Template**; the main action in the top-right is **Start Parsing**.
    

> Note: “Batch parsing” in everyday speech usually means **Parse Preview → select → import** on this page. It is not the same path as AI generation in `We-01h AI制卡` and does not require AI service configuration.

## Before You Start

Before parsing, you need at least one parse template and Markdown source files that match the layout.

1. Confirm at least one parse template is saved in the plugin; if the list is empty, create or import presets in **Parse Preview Settings** first.
    
2. Prepare Markdown notes whose structure matches the chosen template—for example `<->` card splits, `---div---` front/back splits, or a Q/A regex layout.
    
3. If you have not created memory decks yet, create one in **Deck Study** first for easier import later.
    

> Note: Parse success depends mainly on **note layout** matching **template rules**, not AI availability. Wrong layout may cause parse failure or empty results.

## Parse Preview Settings

Delimiters, regex templates, batch scan scope, and similar options are managed in **Parse Preview Settings**.

1. While on **Parse Preview**, click the top-left menu and choose **Parse Preview Settings**.
    
2. Under **Symbols and Delimiters**, view or adjust global symbols such as card-range separators and front/back separators; these participate in some template split logic.
    
3. Under **Regex Parse Templates**, create, edit, copy, or delete templates; the plugin also includes official example templates you can import by name and tweak.
    
4. When editing a template, use **Test Parse** with sample Markdown before saving to verify rules match; you can also view official example documents to compare with your note format.
    
5. For folder batch scanning, configure excluded folders, max files per batch, and other batch options in settings.
    

> Note: Parse Preview settings may be an advanced feature. If opening them prompts activation, follow the plugin guidance. With built-in templates available, you can usually select one directly and enter settings only when needed.

## Choose Source File or Folder

Parse Preview supports a single note or a folder whose Markdown files are read in batch.

1. Click **File/Folder** in the top bar.
    
2. Choose **Select File** to search and pick a Markdown file from the vault, or **Select Folder** to specify a scan scope.
    
3. For folders, the plugin recursively reads Markdown files, subject to excluded directories and per-batch file limits in settings.
    
4. After selection, the toolbar shows the current source; the plugin remembers your last choice.
    

> Note: AI Card Generation mode usually handles a single note; Parse Preview supports **whole-folder batch reading**. Selected files are recorded as card source documents but usually not at block-level precision.

## Choose Parse Template

Before each parse, specify a template rule in the top bar.

1. Click **Parse Template** in the top bar and choose one saved preset.
    
2. If the list is empty, create a template in **Parse Preview Settings** first, then return here to select it.
    
3. Different templates use different split methods—delimiter split, regex match, etc.; pick the one that best matches your note structure.
    

> Note: The template name appears beside the preview title so you can confirm which rule set is active.

## Start Parsing

After source and template are ready, start parsing.

1. Confirm a source file or folder and a parse template are selected.
    
2. Click **Start Parsing** in the top-right.
    
3. During parsing, the interface stays on Parse Preview; when done, split results appear in the preview list.
    
4. After a successful single-file parse, you usually see how many cards were parsed; in folder mode, how many files were processed is also summarized.
    
5. If some files fail, the notice may include failure count or reasons; successfully parsed cards still enter preview.
    

> Note: If the folder has no parseable Markdown, or layout does not match the template so nothing splits out, the interface warns of failure or empty results. Check that template and note examples align.

## Preview and Select Cards

After parsing, check front/back and tags in the preview area before deciding what to import.

1. The main preview shows front and back; you can view content like a normal study card.
    
2. The preview title shows a source summary—often the filename for a single file, or something like “Folder · N files · M cards · template name” for folder batch.
    
3. For multi-file batch results, switching cards may show the source filename for the current entry.
    
4. The bottom index bar switches cards; tap to jump, long-press to select or deselect.
    
5. Parsed cards are selected by default; deselect unwanted ones via long-press on the index bar or use **Select All / Deselect All**.
    

> Note: The preview area only changes **whether to import**—it does not rewrite source notes. If a card structure is abnormal, import may warn or fail; deselect that card first.

## Import to Deck

After confirming, write selected cards to the target deck.

1. Choose **Target Deck** at the bottom of the preview area.
    
2. Confirm the import button shows the current selected count.
    
3. Click **Import N Cards** to save.
    
4. On success, a summary appears; imported cards are removed from the pending selection.
    

> Note: You need at least one selected card and a valid deck before import. Parse results do not use AI Card Generation **History** recovery; to import again, re-parse or keep the current preview state.

## Sidebar Mode and Follow Active Document

When Parse Preview is in an Obsidian sidebar, source selection works slightly differently.

1. After dragging the plugin main interface to a sidebar, the layout switches to a narrow-column-friendly view.
    
2. The top file entry can switch to **Follow Active Document**, using the Markdown open in the main area as a single-file source.
    
3. When enabled, as you switch notes in the content area, Parse Preview follows the currently open Markdown; when disabled, you manually select files again.
    
4. If the current source is a **folder** batch, it does not follow a single active document—the folder remains the source.
    

> Note: Follow Active Document suits “parse a single card draft while organizing”; for processing a whole directory at once, use **Select Folder**.

## Difference from AI Card Generation

The same page also has an **AI Card Generation** sub-view—they are easy to confuse. Use this guide to choose:

| Comparison | Parse Preview (batch parsing) | AI Card Generation |
|--------|----------------------|---------|
| Uses large model | No | Yes |
| Main dependency | Parse template and note layout | AI config, model, prompts |
| Typical input | Single file or folder | Single note |
| Typical use | Material already in quasi-card structure | Messy material needing understanding and rewriting |
| Study before import | No **Study Now** filter | Supported |

> Note: If notes do not yet have a stable layout, prefer `We-01h AI制卡`; if they are standardized card drafts, AI export results, or divider-split documents, prefer Parse Preview in this article.

## Relation to Legacy Command Palette Entries

Earlier versions had commands like “Batch parse current file” in the Obsidian command palette. The current main path is unified on this page’s **Parse Preview**: choose source and template, preview, then import.

1. If you prefer “look first, then decide whether to import,” use the Parse Preview flow described here.
    
2. If other tutorials or old notes still mention command palette batch parsing, treat **AI Card Generation → Parse Preview** in the current app as authoritative.
    

> Note: Parse rules come from the same template system; what changed is the entry point and whether preview confirmation is required. Card format rules are in `We-01g 卡片题型`.
