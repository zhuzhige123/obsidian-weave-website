Weave Deck **exam question groups** organize existing multiple-choice and answerable cloze questions into question banks for timed tests, wrong-question review, and accuracy analysis. Groups mainly store question references and test data; card body text stays in memory decks. Good for drill, mock exams, and stage assessment—complementing **memory decks** focused on spaced repetition. Here is a detailed guide:

## Relationship Between Exam Question Groups and Memory Decks

Understanding the split helps you pick the right entry and avoid accidental data loss.

1. **Memory decks** store card body text, review progress, and deck membership—for everyday memory study and FSRS review.
    
2. **Exam question groups** store question indexes, attempt counts, accuracy, wrong-book status, and other exam-oriented data—for grouped practice and statistics.
    
3. Each question in a group is usually a **reference** to a card in a memory deck—not a separate copy of the body text.
    
4. Therefore: **Remove from exam question group** only removes group records and test data—the card in the memory deck remains; **Delete card** removes it from both memory deck and exam question group.
    

> Note: Memory decks focus on “learn and remember”; exam question groups focus on “can you answer, how stable.” Use both—for example memory review first, then mock exam in a group.

## Enter Exam Question Group Mode

Exam question groups are not a separate top-level page—you enter via data source or filter switch in **Deck Study** and **Card Management**.

### Deck Study Interface

1. Open the plugin main interface and enter **Deck Study**.
    
2. Use top colored dots to switch from **Memory Decks** to **Exam Question Groups**.
    
3. After switching, the main area shows exam question group cards—not memory deck cards.
    
4. The top-left create entry becomes **Create Exam Question Group**.
    

### Card Management Interface

1. Open the plugin main interface and enter **Card Management**.
    
2. Use the top-left menu or top data source button to switch from **Memory Decks** to **Exam Question Groups**.
    
3. After switching, table, grid, and kanban show question cards under each group—not all memory cards.
    

> Note: Exam question groups may be an advanced feature. If switching prompts activation, follow plugin guidance. When inactive, the interface may show **Exam Question Groups (Advanced)**.

## Create and Edit Exam Question Groups

### Create New Exam Question Group

1. In **Deck Study** with **Exam Question Groups** filter active, open the top-left menu and choose **Create Exam Question Group**.
    
2. Enter group name; add tags as needed for later grouping and study route filtering.
    
3. After save, the new group appears in Deck Study.
    
4. A new group may start empty—add qualifying questions from Card Management or other entries.
    

### Edit and Delete

1. Open the menu on a group card and choose **Edit Deck** or **Edit**.
    
2. Change group name, tags, etc.; within one tag group you usually pick at most one tag for columnizing and filtering.
    
3. Delete asks for confirmation; group data cannot be recovered after delete, but **does not automatically delete** card body text in memory decks.
    

> Note: Group card appearance (e.g. **Default**, **Elegant Chinese Style**) follows **Deck Card Style** in plugin settings—the same visual theme as memory decks.

## Question Inclusion Rules

Not every memory card can enter an exam question group—the plugin filters by question type rules.

1. **Multiple choice**: cards parseable as multiple-choice structure can be included directly.
    
2. **Cloze**: only clozes with `#input` tag in content count as answerable fill-in-blank and can be included.
    
3. Plain Q&A, clozes without `#input`, and content not recognizable as multiple choice usually **cannot** join exam question groups.
    
4. During batch add, the interface may report skipped count; qualifying cards still import normally.
    

> Note: To include a cloze in an exam question group, add `#input` to the card body first. Card type rules are in `We-01g 卡片题型`.

## How to Add Questions to Exam Question Groups

### Batch Add from Card Management

The most common path when you already have many multiple-choice cards.

1. In **Card Management**, switch data source back to **Memory Decks**, find and select multiple-choice or answerable cloze cards to include.
    
2. Open the batch menu and find the entry related to **Referenced by the following exam question groups**.
    
3. Choose an existing exam question group or create a new one.
    
4. After confirm, qualifying cards join the group; card body in memory decks stays unchanged.
    

### Create Exam Question Group from Selection

Create a group while adding currently selected cards in one step.

1. Multi-select qualifying cards in Card Management.
    
2. Use batch menu **Create Exam Question Group**.
    
3. Enter group name and tags and confirm creation.
    
4. Selected cards are written as question references into the new group.
    

### Link When Importing from AI Card Generation

When using **Study Now → Exam Study Mode** in AI Card Generation preview, or specifying an exam question group during import:

1. Kept cards are written to the memory deck first;
    
2. Then qualifying questions such as multiple choice are linked to the chosen exam question group.
    

> Note: AI Card Generation flow is in `We-01h AI制卡`. Parse Preview import with an exam question group follows the same **memory deck + group reference** logic.

### Pair with Memory Deck

When a memory deck and exam question group are used as a pair, establish pairing on the memory deck.

1. In the memory deck menu, choose **Pair Exam Question Group**.
    
2. Pick the target exam question group from the list; paired groups show corresponding status.
    
3. After pairing, starting an exam from that memory deck can prioritize the paired group.
    

> Note: Group tree display follows memory deck hierarchy—pairing helps **study deck** and **exam question group** align structurally.

## Group Management in Deck Study

After switching to **Exam Question Groups**, Deck Study shows group-level cards—not individual questions.

### Group Card Information

Each exam question group card usually shows:

1. **Total questions**: count in the group.
    
2. **Practiced**: questions tested at least once.
    
3. **Accuracy**: overall performance from test data.
    
4. **Total errors** or wrong-question related stats.
    

### Start Exam

1. Click the group card or choose start study / start exam from its menu.
    
2. If an unfinished exam session exists, you may be asked **Resume**, **Restart**, or **Cancel**.
    
3. With no unfinished session, **Exam Mode Configuration** opens; confirm to enter the exam interface.
    
4. Empty groups cannot start an exam; empty state usually prompts adding questions from multiple-choice cards in Card Management first.
    

### Group Analysis and Kanban

1. From the group card menu, choose **Analysis** for mastery trend, EWMA, and other exam-oriented charts.
    
2. In kanban view, groups can columnize by accuracy—e.g. **Not practiced**, **>90%**, **>75%**, **<60%**—to find weak groups.
    
3. Tag and tag group organization for group columns can be adjusted in kanban-related settings.
    

> Note: Deck Study page manages **group entry**; question body and per-question test data are easier to inspect in Card Management under **Exam Question Groups** data source.

## Exam Question Group View in Card Management

After switching Card Management data source to **Exam Question Groups**, you see a **question-level** card list.

### Views and Fields

1. **Table view** auto-switches to group-specific column presets—e.g. **Minimal**, **Exam**, **All**.
    
2. Compared to memory decks, extra columns often include **Exam Question Group**, **Question Type**, **Accuracy**, **Attempts**, **Last Test**, **Error Level**, etc.
    
3. **Grid view** still supports fixed, masonry, and timeline layouts; accuracy can show in card property badges.
    
4. **Kanban view** often defaults to **Status** grouping; also question type, priority, deck, tags, etc.
    

### Exam Question Group Search

Under **Exam Question Groups** data source, top search supports property prefixes beyond keywords, e.g.:

1. `type:` search by question type.
    
2. `accuracy:` by accuracy—high, medium, low, or numeric values.
    
3. `attempts:` by attempt count.
    
4. `error:` by wrong-question level—high frequency, common, mild, etc.
    

> Note: Syntax follows Obsidian search design. After filtering, batch remove group references, add tags, or edit questions in the current view.

## Start Exam and Exam Mode Configuration

Before each formal exam you can configure question count, source, and rules.

### Step 1: Core Configuration

1. **Question count**: default (all), 20, 30, 50, or all.
    
2. **Question source**: all questions, not practiced, wrong book, bookmarked.
    
3. **Time limit**: unlimited, or 15 / 30 / 60 minutes, etc.
    
4. Interface shows **Estimated count** and **Estimated duration** to confirm scope.
    

### Step 2: Advanced Options

1. **Question type distribution**: adjust single-choice, multi-select, fill-in, short-answer ratios.
    
2. **Difficulty distribution**: adjust easy, medium, hard ratios.
    
3. **Random question order**, **Random option order**: shuffle questions and options.
    
4. **Auto-save progress**: resume unfinished sessions after interruption.
    
5. **Pure exam mode**: hide toolbar and instant right/wrong feedback; keep submit button; after submit go directly to next question—closer to real exam experience.
    

Click **Start Exam** after confirm; configuration applies to this session.

> Note: Pure exam mode suits formal mock exams; for daily drill with instant explanation, leave it off.

## Exam Study Interface

After entering an exam, the interface follows **answer question → submit → next question → hand in**.

### Header and Progress

1. Top shows progress, e.g. **Study Progress 3 / 20**.
    
2. With a time limit, remaining time shows with pause/resume; time up auto-submits.
    
3. Statistics area, question navigation, and side toolbar can expand or collapse.
    

### Answering and Feedback

1. Multiple choice: select options then **Submit Answer**; outside pure exam mode, instant feedback may show correct, wrong, or missed selections.
    
2. Fill-in: answer in input area then submit; system scores or records per rules.
    
3. Short answer: write your answer; without auto-scoring standard, answer is recorded and reference answer shown.
    
4. After submit, view **Answer Explanation** (usually not instant in pure exam mode).
    
5. Bottom button cycles **Submit Answer**, **Next Question**, **Complete Test**; some modes support **Undo**.
    

### Question Navigation and Side Tools

1. **Question navigation** grid shows current, correct, wrong, unanswered—jump quickly by number.
    
2. Side or vertical toolbar also supports:
    
    - Edit question;
        
    - **Remove from exam question group** or **Delete card**;
        
    - Bookmark / unbookmark;
        
    - Set importance (Low / Medium / High / Very High);
        
    - Adjust question order, option order, navigation column count;
        
    - View card info and test data;
        
    - With trace info, locate source document, PDF, EPUB, or block reference.
        

> Note: **Delete card** in the exam interface removes the card from memory deck and exam question group permanently—cannot undo. To exit group practice only, use **Remove from exam question group**.

## Post-Exam Results and Session Resume

### Test Complete Page

1. After all questions or time-up submit, **Test Complete** page opens.
    
2. Usually shows **Score**, **Correct**, **Duration**, **Accuracy**, etc.
    
3. With multiple test records, history trend charts may show accuracy or score changes.
    

### Unfinished Sessions

1. With auto-save progress enabled, re-entering the same group may prompt an unfinished session.
    
2. Choose **Resume** to continue last progress, or **Restart** to clear session progress and answer again.
    

> Note: Resume restores **current exam session** progress—it does not rewrite card body in memory decks.

## Remove from Group vs. Permanent Delete

These two operations confuse easily—choose by intent:

| Operation | When to use | Effect on memory deck |
|------|----------|------------------|
| Remove from exam question group | Question no longer in this group’s practice | Card body kept |
| Delete card | Question gone for good | Card deleted |

1. **Remove from exam question group** is available in exam study, Card Management batch actions, or question menus.
    
2. After remove, test data and wrong-book records for that question in this group clear; you can still review the card in memory decks.
    
3. If source cards were deleted but group still has dangling references, check and repair **Exam question group dangling references** in plugin **Data Management**.
    

## Connection with Memory Study

Exam question groups connect to memory study at several points.

1. After memory study completes, the celebration page bottom may offer **Choose exam question group** to test what you just reviewed.
    
2. From memory deck context, **Pair exam question group** quickly finds the corresponding group.
    
3. In Card Management table, **Deck** column is the memory deck; **Exam Question Group** column shows which groups reference the question.
    

> Note: If the current memory deck has no paired available exam group, one-click exam from memory path may prompt pairing first or manual group selection.

## Suggested Usage Paths

Combine by study stage:

1. **Memory first, test later**: create and review in memory decks, batch-add multiple choice to exam question groups, mock exam periodically.
    
2. **Create and group while importing**: link to target exam question group when importing via `We-01h AI制卡` or `We-01i 批量解析`.
    
3. **Wrong-question review**: in exam mode configuration choose **Wrong book** source to redo mistakes.
    
4. **Stage assessment**: enable time limit and pure exam mode to simulate formal exam rhythm.
    

## Further Reading

- Memory deck entry and deck card operations: `We-02a 牌组学习界面`
- Memory study and rating: `We-02c 记忆学习界面`
- Card types and `#input` cloze: `We-01g 卡片题型`
- AI card generation and exam mode import: `We-01h AI制卡`
