Weave Deck supports viewing study data for one or more memory decks in the deck analysis chart modal. Switch among deck profile, retention rate, study calibration, card counts, review timing, tag difficulty, and load forecast charts. Here is a detailed guide:

## Open Deck Analysis
Use this to enter from Deck Study and view study and review data for a memory deck.

1. Open the plugin main interface, enter **Deck Study**, and switch to memory decks.
2. Open the menu on the target deck card and choose **Deck Analysis**.
3. The **Deck Analysis** modal opens—**Deck Profile** usually shows first by default.

> Note: Some chart capabilities may be advanced features. If an entry shows locked, follow plugin guidance.

## Top Filters and Scope
Adjust analysis scope at the top of the modal; charts update with filter results.

1. **Deck**: view the current deck only, or multi-select other decks for comparison; supports select all and deselect all.
2. **Range**: quick picks for last 7, 14, 30, 60, 90 days, or custom start/end dates.
3. On the **Load Forecast** tab, range becomes future forecast days—e.g. next 7 days, 14 days.
4. **Data Source** can switch between the current deck and a more global data scope for comparison.
5. On desktop, scroll the mouse wheel on quick range controls to change day count quickly.

> Note: Set deck first, then time range—for clearer reading. Ranges too large or too small can distort trends.

## Deck Profile
This chart gives a one-glance overview of deck status in the current range.

1. Radar chart with five axes: retention, digestion rate, study ease, review punctuality, answer quality.
2. Higher is better on all five axes.
3. Below, metric explanations supplement the chart—predicted recall rate, mastered count, on-time percentage, pass rate, etc.

> Note: Profile suits overview. If one axis is clearly low, switch to the corresponding detail chart.

## Retention Rate
This chart observes whether memory is holding as expected.

1. View average predicted recall rate, actual pass rate, and compare to target retention.
2. Horizontal axis spans days; vertical axis is recall/retention percentage.
3. If no usable retention data exists in the current range, it shows no data for this dimension.

> Note: Predicted recall is theoretical estimate; actual pass rate comes from review results. Comparing both helps judge whether intervals are too loose or too tight.

## Study Calibration
This chart checks review rating performance and whether scheduling is too loose or too tight.

1. View Again rate and pass rate (Hard / Good / Easy) over time.
2. High Again rate often means intervals are too long or material is inherently difficult.
3. Pass rate can be compared to target retention to judge current scheduling tightness.
4. Without review records in the selected time range, calibration curves cannot be drawn.

## Card Counts
This chart observes how deck size and mastery progress change.

1. View daily counts of new, learning, due, and mastered cards.
2. Also view mastery rate trend.
3. Good for judging whether you are digesting old cards or still piling up new ones.

## Review Timing
This chart observes whether reviews were early, on time, or late.

1. Daily share of early, on-time, and late reviews.
2. High on-time share usually means review rhythm is keeping up.
3. When late reviews dominate, combine with load forecast to check if recent load was too heavy.
4. Without review timing samples in the current range, it shows no data.

## Tag Difficulty
This chart views card difficulty distribution by tag.

1. Horizontal or corresponding dimension shows difficulty with related card counts.
2. Find which tags hold harder content needing split or stronger review.
3. Without tagged difficulty data in the current range, the chart prompts adding tags to cards first.

> Note: This chart depends on card tags. More consistent tagging makes thematic difficulty views more useful.

## Load Forecast
This chart estimates review pressure for upcoming periods.

1. Switch forecast range for upcoming days.
2. Chart shows daily load and can compare to daily capacity.
3. Load may show as low, normal, high, or overloaded.
4. Good before adding many new cards to see whether the next few days will be overwhelmed by reviews.

> Note: Load forecast looks at **future incoming reviews**—unlike most other tabs that look at history.

## Common Empty States
When data is insufficient, the analysis window explains why instead of drawing blank charts.

1. No analyzable cards: no memory cards in current deck scope, or no usable data after filtering.
2. No data for this dimension: insufficient samples for the current tab—no review records, no timing samples, no tag difficulty data, etc.
3. For empty states, widen or narrow time range, confirm deck selection, or accumulate more review history first.

> Note: Deck analysis builds on real review and card data. For new decks or little review history, profile and counts are often more meaningful than calibration or timing first.
