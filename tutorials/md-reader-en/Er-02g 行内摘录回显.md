Callout blocks suit full excerpts, but nested lists often look awkward. Inline excerpts write `quote text + color emoji + source link` on a normal list line and can still re-highlight in the reader body. Good for chapter → excerpt → thought outlines. Details below:

![[Er-02g-inline-excerpt-blue.gif]]

## 1. vs Callout Blocks
1. **Callouts** (`[!EPUB]`): full excerpts, line styles, thought divider. See `Er-02a 摘录笔记工作流` and `Er-02b 高亮、想法与样式标注`.
2. **Inline excerpts**: live in `-` / `1.` lists for outline notes.
3. You can mix both in one book. When both exist at the same place, the callout wins for re-highlight.

> Note: Inline excerpts do not parse the `---div---` thought section. Put thoughts on the next list level, or use a callout.

## 2. What Echoes, What Does Not
The reader only paints **color-marked excerpts** into the body, so casual reference links do not flood the page.

1. **Echoes**: a color emoji sits right before a source link that carries book location (e.g. `cfi=`).
2. **Does not echo**: source link only, no color emoji—treated as a plain reference.
3. Settings can toggle **Inline excerpt echo** (on by default). Turning it off stops inline echo; callouts are unchanged. See `Er-04b 阅读器设置与数据同步`.

> Note: A lone 🔴, or a link to a normal webpage, never echoes.

## 3. How to Write It
Recommended: quote text first, color emoji immediately before the link. Nest under a chapter heading if you like:

```note
## Letter to the Class, Art Students League of New York
- I planned my death carefully; unlike my life, which meandered along from one thing to another, despite my feeble attempts to control it. My life had a tendency to spread, to get flabby, to scroll and festoon like the frame of a baroque mirror, which came from following the line of least resistance. I wanted my death, by contrast, to be neat and simple, understated, even a little severe, like a Quaker church or the basic black dress with a single strand of pearls much praised by fashion magazines when I was fifteen. No trumpets, no megaphones, no spangles, no loose ends, this time. The trick was to disappear without a trace, leaving behind me the shadow of a corpse, a shadow everyone would mistake for solid reality. At first I thought I'd managed it.🔴 [P6](obsidian://…)
- The artist starts with an opinion; he organizes the materials to the expression of that opinion.🔴 [P11](obsidian://…)
- No feature should be drawn except in its relation to the others. There is a dominating movement through all the features. There is sequence in their relationship. There is sequence in the leading lines of the features with the movements of the body. This spirit of related movement is very important in the drawing or painting of hair. Hair is beautiful in itself, this should not be forgotten, but it is the last position of importance it takes in the make-up of a portrait. The hair must draw the grace and dignity—perhaps the brains—of the head. The lights on the hair must be used to stress the construction, to vitalize, accentuate and continue movement. The outline of the hair over the face must be used as a principal agent for the drawing of the forms of the forehead and temples, and must at the same time partake of the general movement of the shoulders and of the whole body. The hair is to be used as a great drawing medium. It is to be rendered according to its nature, but it is not to be copied. Think well on this; it is very important.🟣 [P12](obsidian://…)
```

Obsidian colored-highlight syntax also works, with the link right after:

```note
- ==🟣The most vital things in the look of a face or of a landscape endure only for a moment. Work should be done from memory. The memory is of that vital movement. During that moment there is a correlation of the factors of that look. This correlation does not continue. New arrangements, greater or less, replace them as mood changes. The special order has to be retained in memory—that special look, and that order which was its expression. Memory must hold it. All work done from the subject thereafter must be no more than data-gathering. The subject is now in another mood. A new series of relations has been established. These may confound. The memory of that special look must be held, and the “subject” can now only serve as an indifferent manikin of its former self. The picture must not become a patchwork of parts of various moods. The original mood must be held to.== [P13](obsidian://…)
```

Colors map to the reader’s five tones:

1. 🟡 / 🟠 → yellow
2. 🟢 → green
3. 🔵 → blue
4. 🔴 → red
5. 🟣 → purple

## 4. Write with Insert
With automation on, color chips still write callouts; **Insert** writes the current **Selection copy format** into the note.

1. Open the target Markdown note and place the cursor in the list.
2. Turn on top-bar **Automation**.
3. In settings, set **Selection copy format** to **Copy text with MD link** (or text with page link).
4. Select body text and tap **Insert** on the toolbar.
5. The note should get text + color emoji + link (default yellow 🟡). You can also use blue 🔵; after save, the reader echoes that color.

> Note: With automation off, **Copy** goes to the clipboard without a color emoji by default, so it will not echo as an inline excerpt. To echo, add an emoji before the link after pasting, or use Insert as above.

## 5. When Re-Highlight Does Not Appear
1. Confirm **Inline excerpt echo** is on.
2. Confirm a color emoji sits before a plugin source link.
3. Confirm content was saved to a Vault file, not clipboard only.
4. Close and reopen the reader; if still missing, use **Rebuild highlight index** in settings.
5. Bidirectional jump and precise positioning: `Er-02d 双向溯源与正文回显`.
