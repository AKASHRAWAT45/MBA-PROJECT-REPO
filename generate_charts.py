#!/usr/bin/env python3
"""Generate charts ONLY from banking_ai_real_data.db — no hardcoded stats."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "data"))
sys.path.insert(0, os.path.dirname(__file__))

from data.seed_database import seed
from data.db_query import (
    get_figure_data, get_bank_metrics, get_rbi_dpi,
    load_chart_series, display_value, chart_label,
)

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "charts")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 10,
})


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved {path}")


def ensure_db():
    db = os.path.join(os.path.dirname(__file__), "data", "banking_ai_real_data.db")
    if not os.path.exists(db):
        seed()
    return db


def fig1():
    labels, values, _ = load_chart_series("Figure 1")
    fig, ax = plt.subplots(figsize=(10, max(5, len(labels) * 0.55)))
    colors = plt.cm.Blues(np.linspace(0.45, 0.85, len(values)))
    bars = ax.barh(labels, values, color=colors, edgecolor="#1a365d", linewidth=0.6)
    ax.set_xlabel("Published Value (%) — Source: Real Data Database")
    ax.set_title("Figure 1. Verified Adoption and Digitization Indicators")
    ax.set_xlim(0, 110)
    for bar, val in zip(bars, values):
        ax.text(val + 1, bar.get_y() + bar.get_height() / 2, f"{val:g}%", va="center", fontsize=9)
    ax.grid(axis="x", alpha=0.3, linestyle="--")
    save(fig, "fig1_adoption_by_area.png")


def fig2():
    rows = get_figure_data("Figure 2")
    labels, values = [], []
    for r in rows:
        v = display_value(r)
        if v is None:
            continue
        lbl = chart_label(r["metric_name"], 35)
        if r.get("value_min") and r.get("value_max"):
            lbl += f"\n(range {r['value_min']}-{r['value_max']}%)"
        labels.append(lbl)
        values.append(v)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(range(len(labels)), values, color="#2b6cb0", edgecolor="#1a365d", width=0.65)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=25, ha="right", fontsize=8)
    ax.set_ylabel("Published Value (%)")
    ax.set_title("Figure 2. Documented Benefits (EY and McKinsey Published Research)")
    save(fig, "fig2_benefits_rating.png")


def fig3():
    """Figure 3: Real EY consumer demand indicators (n=2,030) — no invented severity index."""
    labels, values, _ = load_chart_series("Figure 3")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(labels, values, color="#c53030", edgecolor="#742a2a", width=0.55, alpha=0.85)
    ax.set_ylabel("Published Survey Result (%)")
    ax.set_title("Figure 3. Customer Demand Indicators (EY Survey, n = 2,030)")
    plt.xticks(rotation=15, ha="right")
    save(fig, "fig3_challenges.png")


def fig4():
    labels, values, _ = load_chart_series("Figure 4")
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(values, labels=[l.replace("\n", " ") for l in labels], autopct="%1.0f%%",
           startangle=140, colors=plt.cm.Blues(np.linspace(0.4, 0.85, len(values))),
           wedgeprops={"edgecolor": "white", "linewidth": 1.2}, textprops={"fontsize": 9})
    ax.set_title("Figure 4. Technology Adoption Rates (Deloitte and EY Surveys)")
    save(fig, "fig4_technology_mix.png")


def fig5():
    """Bank disclosed metrics — HDFC digital acquisitions % vs ICICI digital trade %."""
    metrics = get_bank_metrics()
    # Primary comparable: percentage metrics per bank
    pct_metrics = [m for m in metrics if m["unit"] == "percent"]
    fig, ax = plt.subplots(figsize=(9, 5))
    if pct_metrics:
        banks = [m["bank_name"] for m in pct_metrics]
        vals = [m["value"] for m in pct_metrics]
        names = [m["metric_name"][:40] for m in pct_metrics]
        x = range(len(banks))
        ax.bar(x, vals, color="#2b6cb0", edgecolor="#1a365d", width=0.6)
        ax.set_xticks(x)
        ax.set_xticklabels([f"{b}\n({n[:25]}...)" for b, n in zip(banks, names)], fontsize=8)
        ax.set_ylabel("Disclosed Value (%)")
    # Add HDFC WhatsApp as secondary annotation
    lakh_metrics = [m for m in metrics if m["unit"] == "lakh_per_month"]
    note = "; ".join(f"{m['bank_name']}: {m['value']} lakh WhatsApp/mo" for m in lakh_metrics)
    ax.set_title("Figure 5. Bank-Disclosed Digital Operations Metrics (Annual Reports)")
    if note:
        ax.annotate(f"Also from DB: {note}", xy=(0.5, -0.22), xycoords="axes fraction", ha="center", fontsize=8)
    save(fig, "fig5_bank_maturity.png")


def fig6():
    dpi = get_rbi_dpi()
    labels = [d["metric_name"].replace("RBI Digital Payments Index ", "DPI ") for d in dpi]
    values = [d["value"] for d in dpi]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(labels, values, marker="s", linewidth=2.2, color="#276749", markersize=10)
    ax.fill_between(range(len(values)), values, alpha=0.15, color="#276749")
    ax.set_ylabel("RBI Digital Payments Index (Official)")
    ax.set_title("Figure 6. RBI Digital Payments Index — Verified Data Only (No Projections)")
    for i, v in enumerate(values):
        ax.annotate(str(v), (i, v), textcoords="offset points", xytext=(0, 10), ha="center")
    ax.grid(alpha=0.3, linestyle="--")
    save(fig, "fig6_efficiency_trend.png")


def fig7():
    labels, values, _ = load_chart_series("Figure 7")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar([l.replace("\n", " ") for l in labels], values,
           color=["#2b6cb0", "#3182ce", "#4299e1"], edgecolor="#1a365d", width=0.65)
    ax.set_ylabel("Executives Citing Priority (%)")
    ax.set_title("Figure 7. Investment Priorities (Deloitte 2024 Banking Survey)")
    plt.xticks(rotation=15, ha="right")
    save(fig, "fig7_investment_allocation.png")


def fig8_and_9():
    # Roadmap and TOE unchanged — conceptual diagrams, not statistics
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.axis("off")
    phases = [("1. Assess", "Process\nmining", 0.5), ("2. Prioritize", "Business\ncase", 2.5),
              ("3. Pilot", "KPI\ntracking", 4.5), ("4. Scale", "Reuse &\nAPIs", 6.5),
              ("5. Optimize", "Governance\naudit", 8.5)]
    for title, sub, x in phases:
        box = mpatches.FancyBboxPatch((x - 0.7, 1.5), 1.4, 1.0, boxstyle="round,pad=0.05",
                                       facecolor="#ebf8ff", edgecolor="#2b6cb0", linewidth=2)
        ax.add_patch(box)
        ax.text(x, 2.05, title, ha="center", va="center", fontsize=10, fontweight="bold")
        ax.text(x, 0.7, sub, ha="center", va="center", fontsize=9)
    for x in [1.2, 3.2, 5.2, 7.2]:
        ax.annotate("", xy=(x + 0.8, 2.0), xytext=(x + 0.3, 2.0),
                    arrowprops=dict(arrowstyle="->", color="#2b6cb0", lw=2))
    ax.set_title("Figure 8. Phased AI Implementation Roadmap (Framework)", fontsize=12, pad=12)
    save(fig, "fig8_implementation_roadmap.png")

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, 9); ax.set_ylim(0, 5); ax.axis("off")
    ax.text(4.5, 4.6, "TOE Framework", ha="center", fontsize=13, fontweight="bold")
    boxes = [("Technology", ["Legacy systems", "Data quality", "API readiness"], 1.5, "#ebf8ff", "#2b6cb0"),
             ("Organization", ["Leadership", "Skills", "Governance"], 4.5, "#f0fff4", "#276749"),
             ("Environment", ["RBI regulation", "Competition", "FinTech"], 7.5, "#fffaf0", "#c05621")]
    for title, items, x, fc, ec in boxes:
        rect = mpatches.FancyBboxPatch((x - 1.2, 1.2), 2.4, 2.8, boxstyle="round,pad=0.05", facecolor=fc, edgecolor=ec, linewidth=2)
        ax.add_patch(rect)
        ax.text(x, 3.5, title, ha="center", fontsize=11, fontweight="bold")
        for i, item in enumerate(items):
            ax.text(x, 2.9 - i * 0.5, item, ha="center", fontsize=9)
    ax.set_title("Figure 9. TOE Framework (Conceptual Diagram)", fontsize=12, y=0.02)
    save(fig, "fig9_toe_framework.png")


def db_table_images():
    """Render database registry tables as static PNG images for report appendix."""
    import sqlite3

    db = os.path.join(os.path.dirname(__file__), "data", "banking_ai_real_data.db")
    if not os.path.exists(db):
        seed()
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row

    sources = conn.execute(
        "SELECT source_id, organization, report_title, publication_year FROM sources ORDER BY source_id"
    ).fetchall()
    stats = conn.execute(
        """
        SELECT s.stat_id, s.metric_name, s.value, s.value_min, s.value_max, s.unit,
               s.figure_ref, src.organization
        FROM statistics s JOIN sources src ON s.source_id = src.source_id
        ORDER BY s.stat_id
        """
    ).fetchall()
    conn.close()

    def render_table(title, headers, rows, filename, col_widths=None):
        fig_h = max(4, 0.35 * (len(rows) + 2))
        fig, ax = plt.subplots(figsize=(12, fig_h))
        ax.axis("off")
        ax.set_title(title, fontsize=11, fontweight="bold", pad=12)
        table_data = [headers] + rows
        tbl = ax.table(cellText=table_data, loc="center", cellLoc="left", colWidths=col_widths)
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(7)
        tbl.scale(1, 1.2)
        for (r, c), cell in tbl.get_celld().items():
            if r == 0:
                cell.set_facecolor("#e2e8f0")
                cell.set_text_props(fontweight="bold")
            cell.set_edgecolor("#333333")
        save(fig, filename)

    src_rows = [
        [str(r["source_id"]), r["organization"], (r["report_title"] or "")[:55], str(r["publication_year"] or "")]
        for r in sources
    ]
    render_table(
        "Table 9. Verified Secondary Data Sources Registry",
        ["ID", "Organization", "Report Title", "Year"],
        src_rows,
        "table_db_sources.png",
        col_widths=[0.06, 0.22, 0.58, 0.08],
    )

    stat_rows = []
    for r in stats:
        val = r["value"]
        if val is None and r["value_min"] and r["value_max"]:
            val_str = f"{r['value_min']}-{r['value_max']}"
        elif val is not None:
            val_str = str(val)
        else:
            val_str = "—"
        stat_rows.append([
            str(r["stat_id"]),
            (r["metric_name"] or "")[:42],
            val_str,
            r["unit"] or "",
            r["figure_ref"] or "",
            (r["organization"] or "")[:18],
        ])

    render_table(
        "Table 10. Verified Statistics Registry (36 Metrics)",
        ["ID", "Metric", "Value", "Unit", "Figure", "Source"],
        stat_rows,
        "table_db_statistics.png",
        col_widths=[0.05, 0.34, 0.1, 0.1, 0.1, 0.18],
    )


if __name__ == "__main__":
    ensure_db()
    fig1(); fig2(); fig3(); fig4(); fig5(); fig6(); fig7(); fig8_and_9()
    db_table_images()
    print("All charts and database table images generated from real data database.")
