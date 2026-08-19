Obsidian Weave does not have separate “Q&A template,” “cloze template,” or “multiple-choice template” switches. Question types are parsed dynamically from specific patterns in card Markdown when saving and previewing. Below are common question types and related capabilities, with standard medical examples.

> Note: Change the writing pattern to change the question type. Presentation differences in the study interface are covered in `We-02c 记忆学习界面`. In this tutorial, cloze symbols, Anki numbered clozes, word markers, etc. are always shown in code blocks so plugins like Dataview do not mis-parse `==` or `::` as query syntax.

## Q&A (Question and Answer)
This type suits standard memory cards where you see the question first, then recall the answer.

1. Write the stem on the front and the answer on the back; separate with `---div---`.
2. Front and back can use official Obsidian Markdown—images, formulas, lists, footnotes, etc.
3. After save and preview, study shows the front first; click **Show Answer** to see the back.

Standard example:

```markdown
Between which heart chambers is the mitral valve located? What does it mainly prevent?

---div---

Between the left atrium and left ventricle. It closes during systole to prevent backflow from the left ventricle into the left atrium.
```

![[QQ_1786423499965.png]]


Another example with a footnote hint:

```markdown
Briefly state the most common cause of acute myocardial infarction.[^1]

---div---

Rupture of an atherosclerotic plaque in the coronary arteries with secondary thrombosis, causing acute coronary occlusion.

[^1]: Think: is it a vessel problem or a conduction problem?
```

> Note: Q&A is the most basic format. Cloze and multiple choice build on Markdown content with extra symbols or option structure.

## Multiple Choice
This type suits single- or multi-select quizzes. After writing the agreed structure, save and preview automatically recognize it as multiple choice—no template switch needed.

1. Write the stem first, then options `A.` `B.` `C.` `D.` (or forms like `A、`).
2. Correct answers commonly use either:
   - Parentheses at the end of the stem, e.g. `(B)`, `(AC)`
   - Or an Answer line on the back as in the code block below
3. Use `---div---` to separate explanation; the back can hold rationale.
4. During study, select options first, then **Confirm Answer**, then rate.

Single-choice standard example:

```markdown
Regarding adult CPR, which statement is correct? (B)

A. Compression site is the upper third of the sternum
B. Compression site is the lower half of the sternum, midpoint of the nipple line
C. Compression depth for adults is about 2–3 cm
D. Compression-to-ventilation ratio is fixed at 15:2

---div---

Adult compression site is the lower half of the sternum (near the nipple line midpoint); depth is usually about 5–6 cm; single-rescuer compression-to-ventilation is often 30:2.
```

![[QQ_1786423548856.png]]
Multi-select standard example:

```markdown
Which of the following are common clinical features of acute appendicitis?

A. Migrating right lower quadrant pain
B. Right lower quadrant tenderness and rebound tenderness
C. Large bloody stools with tenesmus
D. May include nausea, vomiting, low-grade fever

---div---

Answer: A,B,D
Typical features include migrating RLQ pain with tenderness and rebound; nausea, vomiting, and low fever may occur. Large bloody stools with tenesmus suggest other lower GI disease—not typical appendicitis.
```

> Note: At least a stem and two or more options are needed for multiple-choice parsing. Write answers clearly for automatic checking during study. ^we-q-we-s74v3v
<!-- weave-test-stats: {"v":1,"attempts":1,"correct":0,"accuracy":0,"lastAt":"2026-08-11T06:44:12.362Z","lastMode":"exam"} -->

## Cloze
This type suits hiding keywords in a medical sentence—recall first, then reveal. Default uses Obsidian highlight syntax: wrap hidden words in double equals. Anki-style numbered clozes are also supported. Symbols can be adjusted in plugin settings.

1. Write a complete sentence or paragraph like a note.
2. Add double equals around words to hide.
3. One card can have multiple clozes.
4. Still use `---div---` for extra notes or explanation; study mainly reveals clozes.
5. During study, use **Show Answer** to reveal all at once, or switch to **Type Answer**.

Standard example:

```markdown
Insulin is secreted by pancreatic ==beta cells of the islets of Langerhans== and mainly acts to ==lower blood glucose==.
```

![[QQ_1786423613711.png]]
Example with explanation:

```markdown
The characteristic pathophysiological change in COPD is ==irreversible airflow limitation==.

---div---

Diagnosis often combines smoking history, chronic cough and sputum, and post-bronchodilator FEV1/FVC < 0.70 on spirometry.
```

Multiple cloze example:

```markdown
A nephron includes structures such as the ==glomerulus== and ==renal tubule==. After reabsorption in the ==renal tubule==, filtrate becomes urine for excretion.
```

> Note: Cloze does not need a template switch. Add highlights to Q&A content and save/preview to get cloze display. Medical terms, mechanism keywords, dose units, etc. suit cloze well.

## Progressive Cloze
This type suits multiple clozes in the same passage that you want as sub-cards for one-at-a-time practice instead of revealing all at once.

1. Use Anki-compatible numbered cloze syntax: write c1, c2, c3… in the same passage.
2. Number from 1; consecutive numbering is recommended. With two or more numbered clozes, Weave can treat them as progressive cloze and generate corresponding sub-cards.
3. During study, each turn mainly practices one cloze; other positions display by rule to reduce interference.
4. Good for anatomy pathways, physiological mechanisms, drug names and doses—multiple points in one context.

Standard example:

```markdown
Basic pulmonary circulation pathway:
The right ventricle pumps blood into the {{c1::pulmonary artery}}; after gas exchange in the lungs, blood returns via the {{c2::pulmonary veins}} to the {{c3::left atrium}}.
```

Example with hints:

```markdown
The glomerular filtration barrier from inside out:
{{c1::endothelial cells::vascular side}},
{{c2::basement membrane}},
{{c3::podocyte slit membrane::Bowman's space side}}.
```

> Note: Plain cloze (`==`) suits one spot or practicing together on one screen; progressive cloze suits multiple numbers practiced separately. Everyday AI batch card generation often outputs plain cloze; for progressive, explicitly use numbered cloze syntax. ^we-q-we-ufhtlv
<!-- weave-test-stats: {"v":1,"attempts":1,"correct":0,"accuracy":0,"lastAt":"2026-08-11T06:44:05.373Z","lastMode":"exam"} -->

## Word Cards
This type suits English words and medical English terms—pronunciation and meaning—often added via fingertip translation lookup flows.

1. Install fingertip translation from the Obsidian community plugin marketplace.
2. After selecting text for lookup, choose Add to Weave in the popup and specify a deck.
3. Card content includes word-related markers and definition structure; study can auto-play pronunciation.
4. US vs. UK defaults follow fingertip translation plugin settings.
5. In memory study **More**, you can enable auto-play media to play pronunciation when switching cards or showing answers.

Content structure sketch (generated by the add flow—you usually do not hand-write this):

```markdown
myocardial infarction

---div---

::fingertip::myocardial infarction::
/ˌmaɪ.əʊˈkɑː.di.əl ɪnˈfɑːk.ʃən/
Myocardial infarction; heart attack
```

> Note: Full add steps are in `We-01a 新建卡片`. Auto-play during study is in `We-02c 记忆学习界面`.

![[QQ_1786423701008.png]]
## Image Mask
This capability suits atlases, anatomy diagrams, and structure diagrams where you hide a region, recall, then reveal.

1. Put an image in the card first.
2. While editing, place the cursor on the image line and use editor menu **Weave Image Mask**, or command palette **Edit Image Mask**, to add a mask region.
3. On supported image files, right-click **Weave Image Mask** also works.
4. In memory study, masked images hide the region first; **Show Answer** reveals it.
5. During study you can click individual masks to reveal or cover again as needed.

> Note: Image masks suit atlas localization and structure identification; text cloze still prefers highlight or numbered cloze. Use separately by scenario or together on one image card. Study-side details are also in `We-02c 记忆学习界面`.
![[QQ_1786423885405.png]]
## Other Ways to Use Card Content
Because card preview and editing use official Obsidian capabilities, beyond the types above you often combine community plugins for finer material presentation and source tracing.

1. Excalidraw: partial drawings render in cards with trace-back to the drawing region—good for anatomy sketches, mechanism diagrams, surgical step sketches.
2. Video timestamps: cards with timestamped video notes; review can jump to that moment for repeated listening—good for English shadowing, surgical teaching video, lecture replay. Often used with Media Extended and similar plugins.
3. Also PDF++ excerpts and trace-back, mind maps, formulas, components, etc. Without corresponding plugins, Weave’s main Markdown card and review path is unaffected.

> Note: Weave handles memory and testing; reading, drawing, and video context should reuse the Obsidian ecosystem. After material is in cards, study can still jump back to original context.

![[QQ_1786424056485.png]]

## How to Choose
Pick a format by memory goal.

1. Full concept, mechanism, or management principle: use Q&A.
2. Judgment among confusing options: use multiple choice.
3. Key terms in original context: use plain cloze.
4. Multiple points in one passage, practice one at a time: use progressive cloze.
5. English word / term pronunciation and meaning: use the word card flow.
6. Atlas region identification: use image mask.
7. Hand-drawn structure or video clips: use Excalidraw or video timestamp patterns with the relevant community plugins available.

> Note: Question types and capabilities come from content patterns and ecosystem plugins together. You change Markdown and material references; Weave recognizes types and presents them accordingly in preview and study.
