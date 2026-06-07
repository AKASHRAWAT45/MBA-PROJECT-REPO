"""
Verified secondary data — loaded from banking_ai_real_data.db.
Legacy import path preserved for scripts that still reference verified_data.py.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from db_query import get_figure_data, load_chart_series, display_value, get_bank_metrics, get_rbi_dpi

DB_PATH = Path(__file__).parent / "banking_ai_real_data.db"


def _ensure_db():
    if not DB_PATH.exists():
        from seed_database import seed
        seed()


def _series(figure_ref):
    _ensure_db()
    labels, values, sources = load_chart_series(figure_ref)
    return labels, values, sources


_ensure_db()
FIG1_LABELS, FIG1_VALUES, FIG1_SOURCES = _series("Figure 1")
FIG2_LABELS, FIG2_VALUES, _ = _series("Figure 2")
FIG3_LABELS, FIG3_VALUES, _ = _series("Figure 3")
FIG4_LABELS, FIG4_VALUES, _ = _series("Figure 4")
FIG7_LABELS, FIG7_VALUES, _ = _series("Figure 7")

FIG2_NOTE = "Loaded from database; ranges use value_min/value_max where applicable"

# Bank metrics and RBI DPI from database
BANK_METRICS = get_bank_metrics()
RBI_DPI = get_rbi_dpi()

# Deprecated — do not use subjective index scores
FIG5_LABELS = []
FIG5_VALUES = []
FIG5_NOTE = "Replaced by bank-disclosed metrics in database (category=bank_metric)"

FIG3_NOTE = "EY consumer demand indicators (n=2,030) — real published survey data"
FIG6_LABELS = [d["metric_name"] for d in RBI_DPI]
FIG6_VALUES = [d["value"] for d in RBI_DPI]
FIG6_NOTE = "RBI verified DPI only — no projections"
