#!/usr/bin/env python3
"""Build a reproducible chart of the rise of 'slop' (the AI sense) in online
news since 2022, using the GDELT DOC 2.0 API.

Measures the share of English-language online news articles monitored by
GDELT that mention 'AI slop'.

Run with:
    python3 make_chart.py

Writes slop_timeline.csv, slop_timeline.png, slop_timeline.svg and prints a
table of yearly means to stdout.
"""

from __future__ import annotations

import datetime as dt
import io
import sys
import time
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import requests

HERE = Path(__file__).resolve().parent

GDELT_URL = "https://api.gdeltproject.org/api/v2/doc/doc"

START_DATE = dt.datetime(2022, 1, 1, tzinfo=dt.timezone.utc)
RUN_DATE = dt.datetime.now(dt.timezone.utc)

GDELT_QUERIES = {
    "news_ai_slop_pct": '"AI slop" sourcelang:english',
    "news_slop_ai_context_pct": 'slop (AI OR "artificial intelligence") sourcelang:english',
}

GDELT_SLEEP_S = 1.0
RETRY_ATTEMPTS = 3  # first try + two retries
RETRY_WAIT_S = 2.0

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "slop-timeline-chart/1.0 (research script)"})


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
# Plotting
# --------------------------------------------------------------------------

ANNOTATIONS = [
    # (date, label) - dates flagged as 'to verify' in the README.
    (dt.date(2024, 5, 8), "Willison: 'Slop'"),
    (dt.date(2024, 11, 1), "Oxford WOTY shortlist"),
    (dt.date(2025, 12, 1), "Merriam-Webster WOTY"),
]


def style_axes(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", color="#dddddd", linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)


def add_annotations(ax, ymax):
    for event_date, label in ANNOTATIONS:
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


def plot_chart(monthly: pd.DataFrame, out_stem: Path):
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)

    x = monthly.index.to_pydatetime()

    ax.plot(x, monthly["news_ai_slop_pct"], marker="o", markersize=2.5,
            linewidth=1.2, label="'AI slop' (exact phrase)")
    ax.plot(x, monthly["news_slop_ai_context_pct"], marker="o", markersize=2.5,
            linewidth=1.2, label="'slop' near AI/artificial intelligence")
    ax.set_title(
        "Online news: share of English-language articles mentioning AI slop (%)",
        fontsize=11, loc="left",
    )
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.3f%%"))
    style_axes(ax)

    ymax = monthly[["news_ai_slop_pct", "news_slop_ai_context_pct"]].max().max()
    add_annotations(ax, ymax * 1.02 if pd.notna(ymax) else 1)

    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=(4, 7, 10)))

    fig.text(
        0.01, 0.01,
        "Source: GDELT DOC 2.0 API",
        fontsize=7, color="#888888",
    )
    fig.subplots_adjust(left=0.09, right=0.98, top=0.90, bottom=0.14)

    fig.savefig(out_stem.with_suffix(".png"))
    fig.savefig(out_stem.with_suffix(".svg"))
    plt.close(fig)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    print("== Fetching GDELT DOC 2.0 daily timelines and aggregating to monthly means ==")
    gdelt_monthly = gdelt_monthly_means()
    gdelt_monthly.index.name = "month"
    gdelt_monthly = gdelt_monthly.sort_index()

    csv_path = HERE / "slop_timeline.csv"
    out = gdelt_monthly.copy()
    out.index = out.index.strftime("%Y-%m")
    out.to_csv(csv_path, index=True)
    print(f"Wrote {csv_path}")

    plot_chart(gdelt_monthly, HERE / "slop_timeline")
    print(f"Wrote {HERE / 'slop_timeline.png'} and {HERE / 'slop_timeline.svg'}")

    yearly = gdelt_monthly.copy()
    yearly["year"] = yearly.index.year
    yearly_means = yearly.groupby("year").mean(numeric_only=True)
    print("\n== Yearly means ==")
    print(yearly_means.round(5).to_string())

    return {"run_date": RUN_DATE}


if __name__ == "__main__":
    main()
