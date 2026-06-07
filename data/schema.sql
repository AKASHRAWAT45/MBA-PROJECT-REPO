-- Real Data Database Schema
-- Every row must have a published source. No synthetic/estimated values.

CREATE TABLE IF NOT EXISTS sources (
    source_id INTEGER PRIMARY KEY AUTOINCREMENT,
    organization TEXT NOT NULL,
    report_title TEXT NOT NULL,
    publication_year INTEGER,
    url TEXT NOT NULL,
    accessed_date TEXT DEFAULT '2025-05-23'
);

CREATE TABLE IF NOT EXISTS statistics (
    stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id INTEGER NOT NULL REFERENCES sources(source_id),
    category TEXT NOT NULL,          -- rbi, adoption, benefit, investment, bank_metric, technology
    subcategory TEXT,
    metric_name TEXT NOT NULL,
    value REAL,                      -- NULL if qualitative only
    value_min REAL,                  -- for ranges e.g. 15-20%
    value_max REAL,
    unit TEXT NOT NULL,              -- percent, index, lakh_per_month, billion_usd, count
    geography TEXT DEFAULT 'India',
    sector TEXT DEFAULT 'Banking/FinServ',
    bank_name TEXT,
    fiscal_year TEXT,
    operational_domain TEXT,
    sample_size TEXT,
    verbatim_note TEXT,
    figure_ref TEXT,
    FOREIGN KEY (source_id) REFERENCES sources(source_id)
);

CREATE TABLE IF NOT EXISTS qualitative_findings (
    finding_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id INTEGER NOT NULL REFERENCES sources(source_id),
    category TEXT NOT NULL,
    finding_text TEXT NOT NULL,
    bank_name TEXT,
    FOREIGN KEY (source_id) REFERENCES sources(source_id)
);

CREATE INDEX IF NOT EXISTS idx_statistics_category ON statistics(category);
CREATE INDEX IF NOT EXISTS idx_statistics_bank ON statistics(bank_name);
CREATE INDEX IF NOT EXISTS idx_statistics_figure ON statistics(figure_ref);

-- Views for charts (only rows with numeric values from sources)
CREATE VIEW IF NOT EXISTS v_figure1_adoption AS
SELECT metric_name, value, unit, organization, report_title, figure_ref
FROM statistics s JOIN sources src ON s.source_id = src.source_id
WHERE figure_ref = 'Figure 1' AND value IS NOT NULL
ORDER BY stat_id;

CREATE VIEW IF NOT EXISTS v_figure2_benefits AS
SELECT metric_name, value, value_min, value_max, unit, organization, figure_ref
FROM statistics s JOIN sources src ON s.source_id = src.source_id
WHERE figure_ref = 'Figure 2'
ORDER BY stat_id;

CREATE VIEW IF NOT EXISTS v_figure4_technology AS
SELECT metric_name, value, organization, figure_ref
FROM statistics s JOIN sources src ON s.source_id = src.source_id
WHERE figure_ref = 'Figure 4' AND value IS NOT NULL
ORDER BY stat_id;

CREATE VIEW IF NOT EXISTS v_figure5_bank_metrics AS
SELECT bank_name, metric_name, value, unit, organization, fiscal_year
FROM statistics s JOIN sources src ON s.source_id = src.source_id
WHERE figure_ref = 'Figure 5' AND value IS NOT NULL
ORDER BY bank_name, stat_id;

CREATE VIEW IF NOT EXISTS v_figure6_rbi_dpi AS
SELECT metric_name, value, unit, organization
FROM statistics s JOIN sources src ON s.source_id = src.source_id
WHERE figure_ref = 'Figure 6' AND value IS NOT NULL
ORDER BY stat_id;

CREATE VIEW IF NOT EXISTS v_figure7_investment AS
SELECT metric_name, value, organization, figure_ref
FROM statistics s JOIN sources src ON s.source_id = src.source_id
WHERE figure_ref = 'Figure 7' AND value IS NOT NULL
ORDER BY stat_id;
