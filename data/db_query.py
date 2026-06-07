"""Query real data database for charts and report generation."""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "banking_ai_real_data.db"


def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_figure_data(figure_ref):
    """Return list of dicts for a figure from database."""
    conn = connect()
    rows = conn.execute(
        """
        SELECT s.metric_name, s.value, s.value_min, s.value_max, s.unit,
               s.bank_name, s.operational_domain, s.sample_size, s.verbatim_note,
               src.organization, src.report_title, src.url
        FROM statistics s
        JOIN sources src ON s.source_id = src.source_id
        WHERE s.figure_ref = ?
        ORDER BY s.stat_id
        """,
        (figure_ref,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_bank_metrics():
    conn = connect()
    rows = conn.execute(
        """
        SELECT bank_name, metric_name, value, unit, fiscal_year, verbatim_note,
               src.organization, src.report_title
        FROM statistics s
        JOIN sources src ON s.source_id = src.source_id
        WHERE s.category = 'bank_metric' AND s.value IS NOT NULL
        ORDER BY bank_name, s.stat_id
        """
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_rbi_dpi():
    conn = connect()
    rows = conn.execute(
        """
        SELECT metric_name, value, unit, verbatim_note
        FROM statistics s
        JOIN sources src ON s.source_id = src.source_id
        WHERE s.category = 'rbi' AND s.subcategory = 'dpi'
        ORDER BY s.stat_id
        """
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_all_statistics():
    conn = connect()
    rows = conn.execute(
        """
        SELECT s.*, src.organization, src.report_title, src.url
        FROM statistics s
        JOIN sources src ON s.source_id = src.source_id
        ORDER BY s.category, s.stat_id
        """
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def display_value(row):
    """Format value for charts — use single value or midpoint of range."""
    if row.get("value") is not None:
        return float(row["value"])
    if row.get("value_min") is not None and row.get("value_max") is not None:
        return (float(row["value_min"]) + float(row["value_max"])) / 2
    return None


def chart_label(name, max_len=28):
    """Wrap long metric names for charts."""
    name = name.replace("FinServ firms ", "FS: ")
    if len(name) <= max_len:
        return name
    words = name.split()
    lines, current = [], ""
    for w in words:
        if len(current) + len(w) + 1 <= max_len:
            current = (current + " " + w).strip()
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    return "\n".join(lines[:2])


def load_chart_series(figure_ref):
    rows = get_figure_data(figure_ref)
    labels, values, sources = [], [], []
    for r in rows:
        v = display_value(r)
        if v is None:
            continue
        labels.append(chart_label(r["metric_name"]))
        values.append(v)
        sources.append(f"{r['organization']} ({r['report_title'][:30]}...)")
    return labels, values, sources
