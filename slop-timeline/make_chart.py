#!/usr/bin/env python3
"""Build a reproducible chart of the rise of 'slop' (the AI sense) in online
discourse since 2022.

Two panels:
  1. GDELT DOC 2.0 API: share of English-language online news articles
     mentioning 'AI slop'.
  2. Hacker News (Algolia API): stories and comments mentioning 'AI slop',
     per 10,000 HN items.

Run with:
    python3 make_chart.py

Writes slop_timeline.csv, slop_timeline.png, slop_timeline.svg and prints a
table of yearly means to stdout.
"""

from __future__ import annotations

import calendar
import csv
import datetime as dt
import io
import sys
import time
import urllib.parse
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import requests

HERE = Path(__file__).resolve().parent

GDELT_URL = "https://api.gdeltproject.org/api/v2/doc/doc"
HN_URL = "https://hn.algolia.com/api/v1/search_by_date"

START_DATE = dt.datetime(2022, 1, 1, tzinfo=dt.timezone.utc)
RUN_DATE = dt.datetime.now(dt.timezone.utc)

GDELT_QUERIES = {
    "news_ai_slop_pct": '"AI slop" sourcelang:english',
    "news_slop_ai_context_pct": 'slop (AI OR "artificial intelligence") sourcelang:english',
}

HN_PHRASE_QUERY = '"ai slop"'
HN_WORD_QUERY = "slop"

GDELT_SLEEP_S = 1.0
HN_SLEEP_S = 0.5
RETRY_ATTEMPTS = 3  # first try + two retries
RETRY_WAIT_S = 2.0

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "slop-timeline-chart/1.0 (research script)"})

# Crude, transparent keyword heuristic for classifying whether a HN hit that
# contains the bare word 'slop' is plausibly about AI-generated content.
# This is not a language model judgement; see README.md for the caveat.
AI_KEYWORDS = [
    " ai ", " ai.", " ai,", " ai)", "(ai ", "a.i.", "artificial intelligence",
    "llm", "gpt", "chatgpt", "genai", "gen-ai", "gen ai", "generative",
    "openai", "anthropic", "claude", "gemini", "copilot", "midjourney",
    "stable diffusion", "machine learning", "neural network", "chatbot",
    "language model", "diffusion model",
]


def epoch(d: dt.datetime) -> int:
    return calendar.timegm(d.utctimetuple())


def month_starts(start: dt.datetime, end: dt.datetime) -> list[dt.datetime]:
    months = []
    cur = dt.datetime(start.year, start.month, 1, tzinfo=dt.timezone.utc)
    while cur <= end:
        months.append(cur)
        if cur.month == 12:
            cur = dt.datetime(cur.year + 1, 1, 1, tzinfo=dt.timezone.utc)
        else:
            cur = dt.datetime(cur.year, cur.month + 1, 1, tzinfo=dt.timezone.utc)
    return months


def next_month(d: dt.datetime) -> dt.datetime:
    if d.month == 12:
        return dt.datetime(d.year + 1, 1, 1, tzinfo=dt.timezone.utc)
    return dt.datetime(d.year, d.month + 1, 1, tzinfo=dt.timezone.utc)


def fetch_with_retries(fetch_fn, label: str):
    last_exc = None
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            return fetch_fn()
        except Exception as exc:  # noqa: BLE001 - report and retry deliberately
            last_exc = exc
            print(f"  [warn] {label}: attempt {attempt}/{RETRY_ATTEMPTS} failed: {exc}",
                  file=sys.stderr)
            if attempt < RETRY_ATTEMPTS:
                # Back off harder on rate limiting (HTTP 429) than on other errors.
                status = getattr(getattr(exc, "response", None), "status_code", None)
                wait = RETRY_WAIT_S * (5 ** attempt) if status == 429 else RETRY_WAIT_S * attempt
                print(f"  [warn] {label}: waiting {wait:.0f}s before retrying", file=sys.stderr)
                time.sleep(wait)
    print(f"  [error] {label}: giving up after {RETRY_ATTEMPTS} attempts.", file=sys.stderr)
    raise RuntimeError(f"{label} failed after {RETRY_ATTEMPTS} attempts") from last_exc


# --------------------------------------------------------------------------
# GDELT DOC 2.0 API
# --------------------------------------------------------------------------

def fetch_gdelt_timeline(query: str, start: dt.datetime, end: dt.datetime) -> pd.DataFrame:
    params = {
        "query": query,
        "mode": "timelinevol",
        "startdatetime": start.strftime("%Y%m%d%H%M%S"),
        "enddatetime": end.strftime("%Y%m%d%H%M%S"),
        "format": "csv",
    }

    def do_fetch():
        resp = SESSION.get(GDELT_URL, params=params, timeout=60)
        resp.raise_for_status()
        text = resp.text
        if not text.strip():
            raise ValueError("empty response body")
        return text

    text = fetch_with_retries(do_fetch, f"GDELT query {query!r}")
    df = pd.read_csv(io.StringIO(text))
    df.columns = [c.strip().lower() for c in df.columns]
    date_col = next(c for c in df.columns if "date" in c)
    value_col = next(c for c in df.columns if "value" in c)
    df = df.rename(columns={date_col: "date", value_col: "value"})
    df["date"] = pd.to_datetime(df["date"], utc=True)
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df[["date", "value"]].dropna()


def gdelt_monthly_means() -> pd.DataFrame:
    series = {}
    query_items = list(GDELT_QUERIES.items())
    for i, (col, query) in enumerate(query_items):
        print(f"[GDELT] fetching {col!r}: {query}")
        daily = fetch_gdelt_timeline(query, START_DATE, RUN_DATE)
        monthly = daily.set_index("date")["value"].resample("MS").mean()
        series[col] = monthly
        if i < len(query_items) - 1:
            time.sleep(GDELT_SLEEP_S)
    out = pd.DataFrame(series)
    out.index.name = "month"
    return out


# --------------------------------------------------------------------------
# Hacker News (Algolia)
# --------------------------------------------------------------------------

def hn_count(query: str | None, month_start: dt.datetime, month_end: dt.datetime,
             advanced_syntax: bool = False) -> int:
    params = {
        "tags": "(story,comment)",
        "numericFilters": f"created_at_i>={epoch(month_start)},created_at_i<{epoch(month_end)}",
        "hitsPerPage": 0,
    }
    if query:
        params["query"] = query
    if advanced_syntax:
        params["advancedSyntax"] = 1

    def do_fetch():
        resp = SESSION.get(HN_URL, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()

    label = f"HN query {query!r} for {month_start:%Y-%m}"
    data = fetch_with_retries(do_fetch, label)
    time.sleep(HN_SLEEP_S)
    return int(data["nbHits"])


def hn_samples(query: str, month_start: dt.datetime, month_end: dt.datetime,
               n: int = 20) -> list[dict]:
    params = {
        "query": query,
        "tags": "(story,comment)",
        "numericFilters": f"created_at_i>={epoch(month_start)},created_at_i<{epoch(month_end)}",
        "hitsPerPage": n,
    }

    def do_fetch():
        resp = SESSION.get(HN_URL, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()

    label = f"HN sample {query!r} for {month_start:%Y-%m}"
    data = fetch_with_retries(do_fetch, label)
    time.sleep(HN_SLEEP_S)
    return data.get("hits", [])


def looks_ai_related(hit: dict) -> bool:
    text = " ".join(
        str(hit.get(f) or "") for f in ("title", "story_text", "comment_text")
    ).lower()
    text = f" {text} "
    return any(kw in text for kw in AI_KEYWORDS)


def hn_monthly_counts(months: list[dt.datetime]) -> pd.DataFrame:
    rows = []
    for m in months:
        m_end = next_month(m)
        print(f"[HN] counting items for {m:%Y-%m}")
        phrase_n = hn_count(HN_PHRASE_QUERY, m, m_end, advanced_syntax=True)
        word_n = hn_count(HN_WORD_QUERY, m, m_end)
        total_n = hn_count(None, m, m_end)
        rows.append({
            "month": m,
            "hn_ai_slop_phrase_n": phrase_n,
            "hn_slop_word_n": word_n,
            "hn_total_items_n": total_n,
        })
    df = pd.DataFrame(rows).set_index("month")
    df["hn_ai_slop_phrase_per_10k"] = df["hn_ai_slop_phrase_n"] / df["hn_total_items_n"] * 10_000
    df["hn_slop_word_per_10k"] = df["hn_slop_word_n"] / df["hn_total_items_n"] * 10_000
    return df


def check_bare_slop_noise(hn_monthly: pd.DataFrame) -> tuple[float, dict]:
    """Sample the bare 'slop' word in one busy and one quiet month and report
    the share of hits that look AI-related, by simple keyword heuristic."""
    nonzero = hn_monthly[hn_monthly["hn_slop_word_n"] > 0]
    if nonzero.empty:
        return 0.0, {}
    busy_month = nonzero["hn_slop_word_n"].idxmax()
    quiet_month = nonzero["hn_slop_word_n"].idxmin()

    report = {}
    total_hits = 0
    total_ai = 0
    for label, month in (("busy", busy_month), ("quiet", quiet_month)):
        m_end = next_month(month)
        print(f"[HN] sampling bare 'slop' hits for {label} month {month:%Y-%m}")
        hits = hn_samples(HN_WORD_QUERY, month, m_end, n=20)
        ai_hits = sum(1 for h in hits if looks_ai_related(h))
        report[label] = {
            "month": month.strftime("%Y-%m"),
            "n_sampled": len(hits),
            "n_ai_related": ai_hits,
            "share_ai_related": (ai_hits / len(hits)) if hits else 0.0,
            "titles": [h.get("title") or (h.get("comment_text") or "")[:80] for h in hits],
        }
        total_hits += len(hits)
        total_ai += ai_hits

    overall_share = (total_ai / total_hits) if total_hits else 0.0
    return overall_share, report


# --------------------------------------------------------------------------
# Plotting
# --------------------------------------------------------------------------

ANNOTATIONS = [
    # (date, label, note) - dates flagged as 'to verify' in the README.
    (dt.date(2024, 5, 8), "Willison: 'Slop'", "to verify"),
    (dt.date(2024, 11, 1), "Oxford WOTY shortlist", "to verify"),
    (dt.date(2025, 12, 1), "Merriam-Webster WOTY", "to verify"),
]


def style_axes(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", color="#dddddd", linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)


def add_annotations(ax, ymax):
    for event_date, label, _ in ANNOTATIONS:
        ax.axvline(event_date, color="#999999", linewidth=0.8, linestyle="--", zorder=1)
        ax.annotate(
            label,
            xy=(event_date, ymax),
            xytext=(3, -3),
            textcoords="offset points",
            fontsize=7,
            color="#666666",
            rotation=90,
            va="top",
            ha="left",
        )


def plot_chart(combined: pd.DataFrame, keep_bare_slop: bool, out_stem: Path):
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(8, 4.5), dpi=200, sharex=True,
        gridspec_kw={"hspace": 0.35},
    )

    x = combined.index.to_pydatetime()

    ax1.plot(x, combined["news_ai_slop_pct"], marker="o", markersize=2.5,
              linewidth=1.2, label="'AI slop' (exact phrase)")
    ax1.plot(x, combined["news_slop_ai_context_pct"], marker="o", markersize=2.5,
              linewidth=1.2, label="'slop' near AI/artificial intelligence")
    ax1.set_title(
        "Online news: share of English-language articles mentioning AI slop (%)",
        fontsize=10, loc="left",
    )
    ax1.legend(fontsize=7, frameon=False, loc="upper left")
    style_axes(ax1)

    ax2.plot(x, combined["hn_ai_slop_phrase_per_10k"], marker="o", markersize=2.5,
              linewidth=1.2, color="#1b9e77", label="'ai slop' (phrase)")
    if keep_bare_slop:
        ax2.plot(x, combined["hn_slop_word_per_10k"], marker="o", markersize=2.5,
                  linewidth=1.2, color="#d95f02", label="'slop' (any sense)")
    ax2.set_title(
        "Hacker News: items mentioning AI slop, per 10,000",
        fontsize=10, loc="left",
    )
    ax2.legend(fontsize=7, frameon=False, loc="upper left")
    style_axes(ax2)

    ymax1 = combined[["news_ai_slop_pct", "news_slop_ai_context_pct"]].max().max()
    cols2 = ["hn_ai_slop_phrase_per_10k"] + (["hn_slop_word_per_10k"] if keep_bare_slop else [])
    ymax2 = combined[cols2].max().max()
    add_annotations(ax1, ymax1 * 1.02 if pd.notna(ymax1) else 1)
    add_annotations(ax2, ymax2 * 1.02 if pd.notna(ymax2) else 1)

    ax2.xaxis.set_major_locator(mdates.YearLocator())
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax2.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=(4, 7, 10)))

    fig.text(
        0.01, 0.01,
        "Sources: GDELT DOC 2.0 API; Hacker News via Algolia",
        fontsize=7, color="#888888",
    )
    fig.subplots_adjust(left=0.08, right=0.98, top=0.92, bottom=0.12)

    fig.savefig(out_stem.with_suffix(".png"))
    fig.savefig(out_stem.with_suffix(".svg"))
    plt.close(fig)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    months = month_starts(START_DATE, RUN_DATE)

    print("== Fetching GDELT DOC 2.0 daily timelines and aggregating to monthly means ==")
    gdelt_monthly = gdelt_monthly_means()

    print("== Fetching Hacker News monthly counts via Algolia ==")
    hn_monthly = hn_monthly_counts(months)

    print("== Checking noise in the bare 'slop' HN series ==")
    bare_slop_share, sample_report = check_bare_slop_noise(hn_monthly)
    keep_bare_slop = bare_slop_share >= 0.5
    print(f"  bare 'slop' AI-related share across samples: {bare_slop_share:.0%} "
          f"({'keeping' if keep_bare_slop else 'DROPPING'} the series)")

    combined = gdelt_monthly.join(hn_monthly, how="outer").sort_index()
    combined.index.name = "month"

    csv_path = HERE / "slop_timeline.csv"
    combined_out = combined.copy()
    combined_out.index = combined_out.index.strftime("%Y-%m")
    combined_out.to_csv(csv_path, index=True)
    print(f"Wrote {csv_path}")

    plot_chart(combined, keep_bare_slop, HERE / "slop_timeline")
    print(f"Wrote {HERE / 'slop_timeline.png'} and {HERE / 'slop_timeline.svg'}")

    # Yearly means table for a sanity check.
    yearly = combined.copy()
    yearly["year"] = yearly.index.year
    yearly_means = yearly.groupby("year").mean(numeric_only=True)
    print("\n== Yearly means ==")
    print(yearly_means.round(4).to_string())

    return {
        "keep_bare_slop": keep_bare_slop,
        "bare_slop_share": bare_slop_share,
        "sample_report": sample_report,
        "run_date": RUN_DATE,
    }


if __name__ == "__main__":
    main()
