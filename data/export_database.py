#!/usr/bin/env python3
"""Export real data database to CSV files for transparency and Excel use."""

import csv
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "banking_ai_real_data.db"
EXPORT_DIR = Path(__file__).parent / "exports"


def export():
    EXPORT_DIR.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    for table, filename in [
        ("sources", "01_sources.csv"),
        ("statistics", "02_statistics.csv"),
        ("qualitative_findings", "03_qualitative_findings.csv"),
    ]:
        rows = conn.execute(f"SELECT * FROM {table}").fetchall()
        if not rows:
            continue
        path = EXPORT_DIR / filename
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys())
            w.writeheader()
            w.writerows([dict(r) for r in rows])
        print(f"Exported {path} ({len(rows)} rows)")

    # Joined export for report use
    joined = conn.execute(
        """
        SELECT s.stat_id, s.category, s.metric_name, s.value, s.value_min, s.value_max,
               s.unit, s.bank_name, s.fiscal_year, s.operational_domain, s.sample_size,
               s.figure_ref, src.organization, src.report_title, src.url
        FROM statistics s JOIN sources src ON s.source_id = src.source_id
        ORDER BY s.stat_id
        """
    ).fetchall()
    path = EXPORT_DIR / "04_statistics_with_sources.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=joined[0].keys())
        w.writeheader()
        w.writerows([dict(r) for r in joined])
    print(f"Exported {path} ({len(joined)} rows)")

    conn.close()
    print(f"\nAll CSV exports in: {EXPORT_DIR}")


if __name__ == "__main__":
    export()
