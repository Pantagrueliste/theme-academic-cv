# The rise of 'AI slop' in online news

A small, reproducible chart showing the share of English-language online
news articles that mention 'AI slop' since 2022, using the GDELT DOC 2.0
API.

## What this measures

The chart shows the daily-to-monthly mean of GDELT's `timelinevol` metric:
the percentage of all English-language news articles GDELT monitors that
match a given query on a given day, averaged to a monthly figure.

Two lines are plotted:

- `news_ai_slop_pct`: articles matching the exact phrase `"AI slop"`.
- `news_slop_ai_context_pct`: articles matching `slop` in the same article
  as `AI` or `"artificial intelligence"` (a broader net than the exact
  phrase).

Exact GDELT queries used (both restricted to `sourcelang:english`):

```
"AI slop" sourcelang:english
slop (AI OR "artificial intelligence") sourcelang:english
```

## What this does not measure

This is a measure of **news coverage share**, not of general usage of the
word. It does not capture:

- Social media, forums, or blogs (GDELT indexes news outlets).
- Non-English coverage.
- The volume of AI-generated 'slop' content itself, only how often the
  term is used to describe it in the press.

An earlier version of this chart also included a Hacker News (Algolia)
panel of forum mentions. That panel was dropped: the point of this chart
is to show the media-wide trend, not a single forum's discussion of it,
and a bug in the HN total-item denominator made that panel's normalised
counts unreliable. The GDELT news panel is unaffected by that issue.

## Files

- `make_chart.py` - the script that fetches the data, builds the CSV, and
  renders the chart.
- `slop_timeline.csv` - one row per month, columns `news_ai_slop_pct` and
  `news_slop_ai_context_pct`.
- `slop_timeline.png` / `slop_timeline.svg` - the rendered chart
  (1600x900 at 200 dpi).

## Annotations (to verify)

The chart marks three dates with thin vertical lines. These dates should
be checked against primary sources before being relied on for anything
beyond illustration:

- 8 May 2024: Simon Willison's post 'Slop is the new name for unwanted
  AI-generated content'.
- November 2024: the Oxford Word of the Year 2024 shortlist, which
  included 'slop'.
- December 2025: Merriam-Webster naming 'slop' its Word of the Year 2025.

## Regenerating

```
python3 make_chart.py
```

Requires Python 3 with `requests`, `pandas`, and `matplotlib` installed.
The script fetches from `api.gdeltproject.org`, waits at least one second
between the two GDELT requests, retries a failed request twice with an
exponential back-off (longer on HTTP 429), and reports clearly if a fetch
still fails after that.

Run date of the version in this repository: 2026-09-19.
