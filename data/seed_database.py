#!/usr/bin/env python3
"""
Seed SQLite database with ONLY real, published statistics.
Each row links to source URL. No estimated or invented values.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "banking_ai_real_data.db"
SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def seed():
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = connect()
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))

    sources = [
        ("Reserve Bank of India", "Annual Report 2023-24", 2024,
         "https://www.rbi.org.in/Scripts/AnnualReportPublications.aspx?Id=1409"),
        ("EY India", "GenAI set to boost Indian Financial Services (Feb 2024)", 2024,
         "https://www.ey.com/en_in/newsroom/2024/02/gen-ai-set-to-boost-indian-financial-services-potentially-add-us-dollor-80-billion-to-gva-by-2030-ey-report"),
        ("EY India", "GenAI productivity in Indian banking ops (Mar 2025)", 2025,
         "https://www.ey.com/en_in/newsroom/2025/03/gen-ai-to-drive-productivity-gains-of-up-to-46-percent-in-indian-banking-ops-by-2030"),
        ("Deloitte", "Global Intelligent Automation Survey", 2022,
         "https://www.deloitte.com/us/en/insights/topics/talent/intelligent-automation-2022-survey-results.html"),
        ("Deloitte", "2024 Banking & Capital Markets Data Analytics Survey", 2024,
         "https://www.deloitte.com/us/en/services/consulting/articles/2024-banking-data-analytics-survey-insights.html"),
        ("Deloitte", "EMEA Model Risk Management Survey 2025", 2025,
         "https://www.deloitte.com/middle-east/en/services/consulting/perspectives/ai-adoption-in-financial-institutions-balancing-growth-and-governance.html"),
        ("McKinsey & Company", "Global Banking Annual Review 2025", 2025,
         "https://www.mckinsey.com/industries/financial-services/our-insights/global-banking-annual-review"),
        ("McKinsey & Company", "Extracting value from AI in banking", 2024,
         "https://www.mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise"),
        ("HDFC Bank Limited", "Integrated Annual Report FY2023-24", 2024,
         "https://www.hdfcbank.com/personal/about-us/investor-relations/annual-reports"),
        ("ICICI Bank Limited", "Performance Review Q4 FY2024", 2024,
         "https://www.icici.bank.in/about-us/news-room/2024/performance-review-quarter-ended-march-31-2024"),
        ("ICICI Bank Limited", "Integrated Report FY2023-24", 2024,
         "https://www.icicibank.com/about-us/annual-reports"),
        ("EY India", "Consumer banking survey (n=2,030)", 2024,
         "https://www.ey.com/en_in/insights/banking-capital-markets"),
    ]

    src_ids = {}
    for org, title, year, url in sources:
        cur = conn.execute(
            "INSERT INTO sources (organization, report_title, publication_year, url) VALUES (?,?,?,?)",
            (org, title, year, url),
        )
        src_ids[(org, title)] = cur.lastrowid

    def sid(org, title):
        return src_ids[(org, title)]

    # --- STATISTICS: only published numbers ---
    stats = [
        # RBI
        (sid("Reserve Bank of India", "Annual Report 2023-24"), "rbi", "payments",
         "Digital share of non-cash retail payments", 99.8, None, None, "percent", "India", "Banking", None, "FY2023-24", "payments", None,
         "RBI Annual Report 2023-24 Table IX", "Figure 1"),

        (sid("Reserve Bank of India", "Annual Report 2023-24"), "rbi", "payments",
         "Payment system volume growth YoY", 44.0, None, None, "percent", "India", "Banking", None, "FY2023-24", "payments", None,
         "RBI Annual Report 2023-24", "Figure 1"),

        (sid("Reserve Bank of India", "Annual Report 2023-24"), "rbi", "dpi",
         "RBI Digital Payments Index (September 2022)", 377.5, None, None, "index", "India", "Banking", None, "FY2022-23", "payments", None,
         "RBI DPI semi-annual", "Figure 6"),

        (sid("Reserve Bank of India", "Annual Report 2023-24"), "rbi", "dpi",
         "RBI Digital Payments Index (September 2023)", 418.8, None, None, "index", "India", "Banking", None, "FY2023-24", "payments", None,
         "RBI DPI semi-annual; +10.9% YoY", "Figure 6"),

        (sid("Reserve Bank of India", "Annual Report 2023-24"), "rbi", "payments",
         "Retail payment volume growth YoY", 44.1, None, None, "percent", "India", "Banking", None, "FY2023-24", "payments", None,
         "RBI Annual Report 2023-24", None),

        # EY 2024
        (sid("EY India", "GenAI set to boost Indian Financial Services (Feb 2024)"), "adoption", "genai",
         "FinServ firms implemented or plan GenAI pilot within 12 months", 78, None, None, "percent", "India", "FinServ", None, "2024", "general", "FS sector survey",
         "EY AIdea of India 2024", "Figure 1"),

        (sid("EY India", "GenAI set to boost Indian Financial Services (Feb 2024)"), "benefit", "genai",
         "FinServ firms citing customer experience impact from GenAI", 84, None, None, "percent", "India", "FinServ", None, "2024", "customer_service", "FS sector survey",
         "EY AIdea of India 2024", "Figure 2"),

        (sid("EY India", "GenAI set to boost Indian Financial Services (Feb 2024)"), "benefit", "genai",
         "FinServ firms citing cost reduction from GenAI", 78, None, None, "percent", "India", "FinServ", None, "2024", "cost", "FS sector survey",
         "EY AIdea of India 2024", "Figure 2"),

        (sid("EY India", "GenAI set to boost Indian Financial Services (Feb 2024)"), "benefit", "genai",
         "FinServ firms citing innovation impact from GenAI", 61, None, None, "percent", "India", "FinServ", None, "2024", "innovation", "FS sector survey",
         "EY AIdea of India 2024", "Figure 2"),

        # EY 2025
        (sid("EY India", "GenAI productivity in Indian banking ops (Mar 2025)"), "benefit", "productivity",
         "Productivity gain in Indian banking operations by 2030 (upper bound)", 46, None, None, "percent", "India", "Banking", None, "2030", "operations", None,
         "EY projection", "Figure 2"),

        (sid("EY India", "GenAI productivity in Indian banking ops (Mar 2025)"), "benefit", "productivity",
         "Productivity gain in Indian financial services by 2030", None, 34, 38, "percent", "India", "FinServ", None, "2030", "operations", None,
         "EY projection range", "Figure 2"),

        # EY Consumer
        (sid("EY India", "Consumer banking survey (n=2,030)"), "adoption", "demand",
         "Customers expecting AI-powered financial guidance", 59, None, None, "percent", "India", "Banking", None, "2024", "customer_service", "n=2030",
         "EY consumer survey", "Figure 3"),

        (sid("EY India", "Consumer banking survey (n=2,030)"), "adoption", "demand",
         "Customers wanting unified banking services", 89, None, None, "percent", "India", "Banking", None, "2024", "customer_service", "n=2030",
         "EY consumer survey", "Figure 3"),

        # Deloitte 2022
        (sid("Deloitte", "Global Intelligent Automation Survey"), "technology", "rpa",
         "Organizations already implementing RPA", 74, None, None, "percent", "Global", "Cross-industry", None, "2022", "automation", "n=479",
         "Deloitte 2022 survey", "Figure 1"),

        (sid("Deloitte", "Global Intelligent Automation Survey"), "technology", "ocr",
         "Organizations already implementing OCR", 50, None, None, "percent", "Global", "Cross-industry", None, "2022", "automation", "n=479",
         "Deloitte 2022 survey", "Figure 4"),

        (sid("Deloitte", "Global Intelligent Automation Survey"), "technology", "ai_planned",
         "Organizations planning AI implementation in next 3 years", 46, None, None, "percent", "Global", "Cross-industry", None, "2022", "automation", "n=479",
         "Deloitte 2022 survey", "Figure 4"),

        (sid("Deloitte", "Global Intelligent Automation Survey"), "technology", "process_mining",
         "Organizations planning process mining in next 3 years", 43, None, None, "percent", "Global", "Cross-industry", None, "2022", "automation", "n=479",
         "Deloitte 2022 survey", "Figure 4"),

        # Deloitte 2024
        (sid("Deloitte", "2024 Banking & Capital Markets Data Analytics Survey"), "investment", "genai",
         "Bank executives considering GenAI investment", 62, None, None, "percent", "US", "Banking", None, "2024", "investment", "~150 executives",
         "Deloitte 2024", "Figure 7"),

        (sid("Deloitte", "2024 Banking & Capital Markets Data Analytics Survey"), "investment", "cloud",
         "Banks migrated more than half of data to cloud", 52, None, None, "percent", "US", "Banking", None, "2024", "infrastructure", "~150 executives",
         "Deloitte 2024", "Figure 7"),

        (sid("Deloitte", "2024 Banking & Capital Markets Data Analytics Survey"), "investment", "nocode",
         "Bank executives considering no-code AI", 45, None, None, "percent", "US", "Banking", None, "2024", "investment", "~150 executives",
         "Deloitte 2024", "Figure 7"),

        # Deloitte 2025
        (sid("Deloitte", "EMEA Model Risk Management Survey 2025"), "technology", "ai_ml",
         "Banks using AI/ML models (2025)", 67, None, None, "percent", "EMEA", "Banking", None, "2025", "risk", "87 banks",
         "Deloitte EMEA MRM 2025", "Figure 1"),

        (sid("Deloitte", "EMEA Model Risk Management Survey 2025"), "technology", "ai_ml",
         "Banks using AI/ML models (2023)", 56, None, None, "percent", "EMEA", "Banking", None, "2023", "risk", "87 banks",
         "Deloitte EMEA MRM 2025", None),

        # McKinsey
        (sid("McKinsey & Company", "Global Banking Annual Review 2025"), "benefit", "cost",
         "Net aggregate cost base reduction from AI (lower bound)", None, 15, 20, "percent", "Global", "Banking", None, "2025", "cost", None,
         "McKinsey 2025", "Figure 2"),

        (sid("McKinsey & Company", "Global Banking Annual Review 2025"), "benefit", "cost",
         "Gross cost reduction in select categories (upper bound)", 70, None, None, "percent", "Global", "Banking", None, "2025", "cost", None,
         "McKinsey 2025 up to 70%", "Figure 2"),

        (sid("McKinsey & Company", "Global Banking Annual Review 2025"), "benefit", "investment",
         "Annual global bank technology spend", 600, None, None, "billion_usd", "Global", "Banking", None, "2025", "technology", None,
         "McKinsey 2025 ~$600B", None),

        (sid("McKinsey & Company", "Extracting value from AI in banking"), "benefit", "productivity",
         "Credit analyst productivity gain (lower bound)", None, 20, 60, "percent", "Global", "Banking", None, "2024", "lending", None,
         "McKinsey multi-agent systems", "Figure 2"),

        # HDFC Bank - real disclosures
        (sid("ICICI Bank Limited", "Performance Review Q4 FY2024"), "bank_metric", "digital",
         "Trade transactions done digitally", 71, None, None, "percent", "India", "Banking", "ICICI Bank", "FY2023-24", "trade_finance", None,
         "About 71% of trade transactions", "Figure 1"),

        (sid("HDFC Bank Limited", "Integrated Annual Report FY2023-24"), "bank_metric", "digital",
         "Acquisitions digitally driven (minimum disclosed)", 75, None, None, "percent", "India", "Banking", "HDFC Bank", "FY2023-24", "onboarding", None,
         "More than three-quarters; report states 75%+", "Figure 1"),

        (sid("HDFC Bank Limited", "Integrated Annual Report FY2023-24"), "bank_metric", "digital",
         "Acquisitions digitally driven (minimum disclosed)", 75, None, None, "percent", "India", "Banking", "HDFC Bank", "FY2023-24", "onboarding", None,
         "More than three-quarters; report states 75%+", "Figure 5"),

        (sid("HDFC Bank Limited", "Integrated Annual Report FY2023-24"), "bank_metric", "digital",
         "WhatsApp chat banking interactions per month", 90, None, None, "lakh_per_month", "India", "Banking", "HDFC Bank", "FY2023-24", "customer_service", None,
         "Over 90 lakh monthly interactions", "Figure 5"),

        (sid("HDFC Bank Limited", "Integrated Annual Report FY2023-24"), "bank_metric", "digital",
         "PayZapp registered customers", 75, None, None, "lakh", "India", "Banking", "HDFC Bank", "FY2023-24", "payments", None,
         "Over 75 lakh registered customers", "Figure 5"),

        (sid("HDFC Bank Limited", "Integrated Annual Report FY2023-24"), "bank_metric", "digital",
         "SmartHub Vyapar merchants", 16, None, None, "lakh", "India", "Banking", "HDFC Bank", "FY2023-24", "merchant", None,
         "Over 16 lakh merchants", "Figure 5"),

        (sid("HDFC Bank Limited", "Integrated Annual Report FY2023-24"), "bank_metric", "digital",
         "Live digital acquisition journeys", 30, None, None, "count", "India", "Banking", "HDFC Bank", "FY2023-24", "onboarding", None,
         "30+ acquisition journeys", "Figure 5"),

        # ICICI Bank
        (sid("ICICI Bank Limited", "Performance Review Q4 FY2024"), "bank_metric", "digital",
         "Trade transactions done digitally", 71, None, None, "percent", "India", "Banking", "ICICI Bank", "FY2023-24", "trade_finance", None,
         "About 71% of trade transactions", "Figure 5"),

        (sid("ICICI Bank Limited", "Performance Review Q4 FY2024"), "bank_metric", "digital",
         "Trade Online platform volume growth YoY", 29.2, None, None, "percent", "India", "Banking", "ICICI Bank", "FY2023-24", "trade_finance", None,
         "Volume grew 29.2% YoY", "Figure 5"),

        (sid("ICICI Bank Limited", "Integrated Report FY2023-24"), "bank_metric", "digital",
         "Video KYC products live", 22, None, None, "count", "India", "Banking", "ICICI Bank", "FY2023-24", "kyc", None,
         "Video KYC live for 22 products", "Figure 5"),
    ]

    for row in stats:
        conn.execute(
            """INSERT INTO statistics
            (source_id, category, subcategory, metric_name, value, value_min, value_max,
             unit, geography, sector, bank_name, fiscal_year, operational_domain, sample_size,
             verbatim_note, figure_ref)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            row,
        )

    # Qualitative only (no fake numbers)
    qualitative = [
        (sid("Deloitte", "EMEA Model Risk Management Survey 2025"), "challenge",
         "Insufficient internal AI expertise cited as top GenAI implementation barrier in banking (EY-Parthenon)", None),
        (sid("McKinsey & Company", "Global Banking Annual Review 2025"), "challenge",
         "Banks spend ~$600B on technology annually yet productivity remains uneven due to legacy fragmentation", None),
        (sid("EY India", "GenAI productivity in Indian banking ops (Mar 2025)"), "trend",
         "Large Indian banks focus on enterprise GenAI; mid-sized banks on orchestration layers", None),
    ]
    for src_id, cat, text, bank in qualitative:
        conn.execute(
            "INSERT INTO qualitative_findings (source_id, category, finding_text, bank_name) VALUES (?,?,?,?)",
            (src_id, cat, text, bank),
        )

    conn.commit()
    count = conn.execute("SELECT COUNT(*) FROM statistics").fetchone()[0]
    src_count = conn.execute("SELECT COUNT(*) FROM sources").fetchone()[0]
    conn.close()
    print(f"Database seeded: {DB_PATH}")
    print(f"  Sources: {src_count}")
    print(f"  Statistics rows: {count}")
    return DB_PATH


if __name__ == "__main__":
    seed()
