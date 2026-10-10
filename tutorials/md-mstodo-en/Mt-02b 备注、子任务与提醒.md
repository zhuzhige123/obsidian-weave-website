Indented paragraphs under a task become the To Do body; one level of sub-checkboxes becomes To Do steps. Reminders and “today” use comment markers plus optional time segments. Details below:

## 1. Note block (To Do body)
Under the task, write paragraphs indented **more than the task**, that are not checkbox list items:

```markdown
- [ ] Prepare meeting #mtd-sync 📅 2026-06-21

      Bring last week’s data
      Confirm the projector
```

1. These merge into the To Do task body.
2. Keep note vs subtask structure clear; deep nesting is not synced.

## 2. Subtasks (To Do steps)
Only **one** nesting level is supported (matching To Do Steps):

```markdown
- [ ] Prepare meeting #mtd-sync
  - [ ] Print agenda
  - [x] Send invite
```

1. Children sync as checklist steps with two-way checked state.
2. Child lines get `<!-- mtd:step=… -->`.
3. Grandchildren are **not** synced to To Do.

## 3. Reminders
1. Use inline `⏰` and/or `reminder=` inside the mtd comment.
2. Command palette offers reminder commands (`HH:MM` or `YYYY-MM-DD HH:MM`).
3. Syncs to To Do reminder on/off and time.

> Note: Follow the command prompt for formats; invalid input is rejected.

## 4. “My Day” substitute (myday)
1. Microsoft Graph has **no** My Day read/write API.
2. Use **Add to today (due + myday)** or a `myday` marker in the comment.
3. Effect is approximately **due today + reminder**, not the literal My Day list.

## 5. Notes and backlinks together
1. If backlinks in notes are enabled, the plugin may append an `obsidian://mtd-sync…` section at the end of the To Do body.
2. On pull, that section is stripped so it does not pollute vault notes (per current logic).
3. Inbound route headers (`[[Note]]` / `page:` + `---`) can be removed from To Do after capture via settings.
