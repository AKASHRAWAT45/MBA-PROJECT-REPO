# Viva Summary Report
## Artificial Intelligence and Automation in Banking Operations Management

**Student:** Akash Rawat  
**Enrollment No.:** A9920124013426(el)  
**Program:** MBA, Amity University Online (Jul 2024 – Jul 2026, Sem IV)  
**Industry Partner:** Adhiita Consultancy Services, Noida  
**Guide / Mentor:** Madhva Raj Pratinidhi  
**Submission Year:** 2025

---

# PART A — PROJECT OVERVIEW (What Is This Project?)

## A1. One-Minute Elevator Pitch

This MBA major project studies **how Artificial Intelligence (AI) and automation are transforming banking operations management** in India. It examines adoption levels, documented benefits, implementation challenges, future trends, and practical recommendations for banks and consultancy advisors.

The project uses **verified secondary data only** — from RBI, EY India, McKinsey, Deloitte, and annual reports of five major Indian banks (HDFC, ICICI, Axis, SBI, Kotak). **No primary survey was conducted.** All statistics are stored in a traceable SQLite database with source URLs.

## A2. Why This Topic Was Chosen

| Reason | Explanation |
|--------|-------------|
| Industry relevance | Banks process billions of digital transactions; AI/automation is no longer optional |
| Operations management core | Covers KYC, payments, lending, fraud, compliance — core OM domains |
| Indian context | UPI, RBI supervision, and digital lending make India a high-growth case study |
| Consultancy alignment | Adhiita Consultancy Services advises banks on digital transformation |
| Academic gap | Literature exists globally, but integrated Indian evidence-based synthesis was needed |

## A3. Research Problem (In Simple Words)

Banks are spending heavily on technology, but **operations outcomes remain uneven** — legacy systems, data silos, talent gaps, and weak governance limit value from AI and automation. This project answers: *What does published evidence show about adoption, benefits, challenges, and the path forward for banking operations?*

## A4. Research Objectives

1. **Analyze** the current state of AI/automation in banking operations (India + global benchmarks)
2. **Assess** documented benefits and challenges from industry/regulatory research
3. **Explore** future trends in efficiency, customer service, and risk management
4. **Recommend** actionable strategies for banks and consultancy advisors

## A5. Hypotheses Tested

| Hypothesis | Statement | Result |
|------------|-----------|--------|
| **H1** | Banks with higher disclosed digital operations maturity show stronger automation outcomes | **Supported** — HDFC/ICICI publish stronger numeric disclosures than SBI/Axis/Kotak |
| **H2** | Banks combining process reengineering with automation achieve better outcomes than technology overlay alone | **Partially supported** — iLens, STP, API Factory cases show platform-based approach |

## A6. Theoretical Framework

**TOE Framework (Technology–Organization–Environment)** — Figure 9 in the report:

- **Technology:** Legacy systems, data quality, APIs, AI/ML platforms
- **Organization:** Leadership, skills, governance, change management
- **Environment:** RBI regulation, competition, FinTech pressure, customer demand

AI/automation adoption depends on all three layers — not technology alone.

---

# PART B — WHAT IS IN THE PROJECT REPORT?

## B1. Report Structure (~16,000+ Words)

| Section | Content |
|---------|---------|
| Title Page | University, title, student, guide, industry partner |
| Declaration | Original work statement |
| Table of Contents | All chapters listed |
| List of Tables | 8 tables |
| List of Figures | 9 figures |
| **Chapter 1** | Introduction — background, definitions, scope, significance |
| **Chapter 2** | Literature Review — global/Indian trends, academic & industry sources, TOE framework |
| **Chapter 3** | Research Objectives & Methodology — design, data, sampling, tools, ethics |
| **Chapter 4** | Data Analysis & Results — tables, interpretation, all charts |
| **Chapter 5** | Findings & Conclusion — 10 major findings, 5 conclusions |
| **Chapter 6** | Recommendations & Limitations — 15 recommendations, 10 limitations |
| **Chapter 7** | References — APA 7th edition |
| **Appendix** | Data extraction template, case protocol, database schema, DATA_SOURCES |

## B2. Tables in the Report

| Table | Title | Key Data |
|-------|-------|----------|
| Table 1 | RBI Payment System Indicators | 99.8% digital payments, DPI 418.8 |
| Table 2 | AI/Automation Adoption Indicators | 78% GenAI, 74% RPA, 67% AI/ML |
| Table 3 | Bank-Disclosed Digital Metrics | HDFC 75%+, ICICI 71% trade digital |
| Table 4 | Benefit Indicators | EY 84% CX, McKinsey 15–20% cost reduction |
| Table 5 | Operational Impact Metrics | 30-min loan approval, 29.2% trade growth |
| Table 6 | Implementation Challenges | AI expertise, legacy, data quality |
| Table 7 | Opportunity Mapping | Domain-wise AI opportunities |
| Table 8 | Implementation Priority Matrix | Leadership action priorities |

## B3. Figures (Charts & Diagrams)

| Figure | What It Shows | Data Source |
|--------|---------------|-------------|
| Figure 1 | Adoption & digitization indicators | RBI, EY, Deloitte, HDFC, ICICI |
| Figure 2 | Documented benefits | EY 2024/2025, McKinsey 2025 |
| Figure 3 | Customer demand indicators | EY consumer survey (n=2,030) |
| Figure 4 | Technology mix (RPA, OCR, AI, GenAI) | Deloitte 2022, EY 2024 |
| Figure 5 | Bank-disclosed digital metrics | HDFC & ICICI annual reports |
| Figure 6 | RBI Digital Payments Index | RBI verified: 377.5 → 418.8 |
| Figure 7 | Investment priorities | Deloitte 2024 banking survey |
| Figure 8 | Phased implementation roadmap | Framework diagram |
| Figure 9 | TOE framework | Conceptual diagram (Chapter 2) |

## B4. Project Files (Supporting Assets)

| File | Purpose |
|------|---------|
| `PROJECT_REPORT.docx` | Full Word report with embedded charts |
| `PROJECT_REPORT.html` | HTML version of full report |
| `EXTENDED_ABSTRACT.docx` | Short abstract for submission |
| `data/banking_ai_real_data.db` | SQLite database — 36 stats, 12 sources |
| `data/exports/*.csv` | Transparent CSV exports of all data |
| `generate_charts.py` | Regenerates all charts from database |
| `content/DATA_SOURCES.md` | Full citation list for every statistic |

---

# PART C — WHAT RESEARCH WAS DONE?

## C1. Research Design

**Type:** Descriptive–Exploratory Secondary Research + Comparative Case Analysis  
**Approach:** Non-experimental; no variables manipulated  
**Philosophy:** Positivist — relies on published measurable data  

## C2. Three-Phase Research Process

### Phase 1 — Industry & Regulatory Data Collection
- Extracted statistics from RBI Annual Report 2023-24
- Reviewed EY India GenAI reports (Feb 2024, Mar 2025)
- Reviewed McKinsey Global Banking Review 2025
- Reviewed Deloitte surveys (2022, 2024, 2025)
- Stored every statistic in SQLite database with source URL

### Phase 2 — Bank Case Study Analysis
- **Sample:** 5 banks — HDFC, ICICI, Axis, SBI, Kotak (purposive sampling)
- **Method:** Structured coding of annual reports FY2023-24
- **Extracted:** Digital acquisition %, channel volumes, platform names, trade digital %

### Phase 3 — Verification & Triangulation
- Cross-checked each figure against original source PDF/URL
- Preferred RBI/company source when industry surveys conflicted
- Regenerated all charts from database to ensure text–table–figure consistency

## C3. Data Summary

| Item | Detail |
|------|--------|
| Total statistics in database | 36 |
| Published sources | 12 |
| Banks analyzed | 5 (HDFC, ICICI, Axis, SBI, Kotak) |
| Primary survey | **None** |
| Data type | 100% secondary, publicly available |
| Geographic focus | India (with global industry benchmarks) |

## C4. Key Verified Statistics (Must Know for Viva)

| Statistic | Value | Source |
|-----------|-------|--------|
| Digital share of non-cash retail payments | **99.8%** | RBI AR 2023-24 |
| RBI Digital Payments Index (Sep 2023) | **418.8** (+10.9% YoY) | RBI AR 2023-24 |
| FinServ firms with GenAI pilot/plan | **78%** | EY India, Feb 2024 |
| FinServ citing customer experience impact | **84%** | EY India, Feb 2024 |
| Organizations implementing RPA | **74%** | Deloitte, 2022 |
| Banks using AI/ML models | **67%** | Deloitte EMEA, 2025 |
| Productivity gain in Indian banking ops by 2030 | **Up to 46%** | EY India, Mar 2025 |
| Net cost base reduction from AI | **15–20%** | McKinsey, 2025 |
| HDFC digitally driven acquisitions | **75%+** | HDFC IAR FY2024 |
| HDFC WhatsApp chat banking/month | **90 lakh** | HDFC IAR FY2024 |
| ICICI digital trade transactions | **71%** | ICICI Q4 FY2024 Review |
| Customers expecting AI financial guidance | **59%** | EY consumer survey, n=2,030 |
| Customers wanting unified services | **89%** | EY consumer survey, n=2,030 |

## C5. Major Findings (Top 10)

1. India operates at **near-universal digital payment volume** (99.8%)
2. **GenAI and RPA adoption is mainstream** in financial services (78%, 74%)
3. **HDFC and ICICI lead** on quantifiable digital disclosures
4. **Productivity/cost benefits are substantial** (15–46% range in industry research)
5. **Legacy systems and AI talent** are top barriers
6. **RBI DPI confirms** national digitization trend (377.5 → 418.8)
7. **Customer expectations** drive AI investment pressure (59%, 89%)
8. **H1 supported** — higher disclosed maturity correlates with stronger metrics
9. **H2 partially supported** — platform-based automation shows better outcomes
10. **Consultancy implication** — use verified benchmarks, not vendor hype

## C6. Top Recommendations (Summary)

1. Operations-led AI steering committee  
2. Process mining before automation purchase  
3. Invest in data foundation alongside pilots  
4. Phased roadmap: Assess → Prioritize → Pilot → Scale → Optimize  
5. Human-in-the-loop for credit, fraud, AML decisions  
6. AI governance aligned with RBI expectations  
7. Workforce upskilling programs  
8. Vendor evaluation standards  
9. Benchmark annually against EY/McKinsey/RBI metrics  
10. Partner with consultancies for independent review  

## C7. Limitations (Be Honest in Viva)

1. Secondary data only — no primary survey/interviews  
2. Not all banks publish comparable numeric metrics  
3. Some surveys are global/US-based, not purely Indian  
4. EY 2030 figures are **projections**, not achieved results  
5. Five banks only — regional/cooperative banks not covered  
6. Banks disclose positive metrics selectively  
7. No access to proprietary internal KPIs  

---

# PART D — COMPREHENSIVE VIVA QUESTIONS & ANSWERS

---

## SECTION 1: BASIC INTRODUCTION QUESTIONS

### Q1. What is your project about?
**Answer:** My project is titled *"Artificial Intelligence and Automation in Banking Operations Management."* It examines how AI and automation technologies are being applied across banking operational domains — including KYC, payments, lending, fraud monitoring, customer service, and compliance. The study uses verified secondary data from RBI, EY, McKinsey, Deloitte, and five Indian bank annual reports to analyze adoption levels, benefits, challenges, and recommendations.

### Q2. Why did you choose this topic?
**Answer:** Banking operations are under pressure from digital payment volumes (99.8% digital per RBI), customer expectations for AI-enabled services, and competition from FinTechs. As an MBA student associated with Adhiita Consultancy Services, this topic directly connects operations management theory with a live industry problem my mentor organization advises on. It is timely, data-rich, and academically relevant.

### Q3. What is the industry partner's role?
**Answer:** Adhiita Consultancy Services, Noida, is the industry partner. The project aligns with their advisory work on banking digital transformation. Findings and recommendations — especially benchmarking using EY/McKinsey/RBI data — can guide how they advise bank clients on AI and automation strategy.

### Q4. What is the word count of your report?
**Answer:** Approximately 16,000+ words, within Amity's required range of 15,000–30,000 words for major projects.

### Q5. How many chapters does your report have?
**Answer:** Seven chapters plus appendix: Introduction, Literature Review, Methodology, Data Analysis, Findings, Recommendations/Limitations, References, and Appendix with data sources and instruments.

---

## SECTION 2: OBJECTIVES, PROBLEM & SCOPE

### Q6. What are your research objectives?
**Answer:** Four objectives: (1) Analyze current AI/automation state in banking operations; (2) Assess documented benefits and challenges; (3) Explore future trends in efficiency, customer service, and risk; (4) Provide actionable recommendations for banks and consultancy advisors.

### Q7. What is your research problem?
**Answer:** Despite heavy technology spending (~$600 billion globally per McKinsey), banks lack integrated evidence-based understanding of how AI and automation affect operations outcomes. Uncoordinated initiatives, legacy constraints, and governance gaps limit value realization and increase operational risk.

### Q8. What operational domains does your study cover?
**Answer:** Customer onboarding/KYC/AML, payments and reconciliation, lending operations, customer service, fraud and financial crime, and risk/compliance operations — the core middle and back-office domains of banking operations management.

### Q9. What is the difference between AI and automation in banking?
**Answer:** **Automation** executes predefined rule-based tasks with minimal human intervention (RPA, workflow, STP). **AI** involves systems that learn, reason, or adapt — machine learning for fraud detection, NLP for customer queries, GenAI for document summarization. Intelligent automation combines both.

### Q10. What is the scope and delimitation of your study?
**Answer:** Scope: Indian banking with global industry benchmarks; secondary data 2022–2025; five major banks. Delimitations: No primary survey; no proprietary bank data; no trading/investment banking front office; five banks only.

---

## SECTION 3: METHODOLOGY QUESTIONS

### Q11. What research design did you use?
**Answer:** Descriptive–exploratory secondary research design with comparative case analysis. It is non-experimental — I analyzed existing published data rather than collecting primary responses or manipulating variables.

### Q12. Did you conduct a survey? How many respondents?
**Answer:** **No primary survey was conducted.** An earlier draft incorrectly referenced a 52-respondent survey — that was removed. All data comes from published RBI reports, industry surveys by EY/McKinsey/Deloitte, and bank annual reports. This is stated transparently in Chapter 3.

### Q13. Why did you use secondary data instead of primary research?
**Answer:** Three reasons: (1) Authoritative sources (RBI, Big Four consulting) already publish robust statistics; (2) MBA timeline and access constraints make bank executive interviews difficult without institutional support; (3) Secondary design is academically valid for descriptive-exploratory MBA projects when sources are verified and cited. Future research could add primary interviews.

### Q14. What sampling technique did you use for banks?
**Answer:** **Purposive (judgment) sampling.** I selected HDFC, ICICI, Axis, SBI, and Kotak based on market significance, sector representation (private + public), and depth of public disclosure in annual reports.

### Q15. What data collection instruments did you use?
**Answer:** Two instruments: (A) Case Study Analysis Protocol — for coding bank annual reports; (B) Secondary Data Extraction Sheet — for recording each statistic with source, value, unit, and citation. Both are in Appendix B. Data is stored in `banking_ai_real_data.db`.

### Q16. What tools did you use for analysis?
**Answer:** Microsoft Excel for compilation; thematic coding for case narratives; SQLite database as single source of truth; Python/matplotlib (`generate_charts.py`) for chart generation from database; document triangulation for verification.

### Q17. What is the real data database you mention?
**Answer:** `data/banking_ai_real_data.db` is a SQLite database containing 36 verified statistics from 12 published sources. Each row has the metric name, value, unit, bank name (if applicable), and a linked source URL. Charts regenerate from this database — no hardcoded invented numbers. CSV exports are in `data/exports/`.

### Q18. How did you ensure validity and reliability?
**Answer:** **Validity:** Every statistic traced to published source with APA citation. **Reliability:** Triangulation across RBI, industry surveys, and bank disclosures. **Transparency:** Database and CSV exports allow any examiner to verify numbers. **Limitation acknowledged:** Secondary data may reflect reporting optimism.

### Q19. What ethical considerations did you follow?
**Answer:** Only publicly available documents used; no confidential data accessed; no fabricated primary research claimed; all sources cited per APA 7th edition; no plagiarism — all statistics attributed to original publishers.

---

## SECTION 4: DATA, STATISTICS & ANALYSIS

### Q20. What are your most important statistics?
**Answer:** RBI: 99.8% digital payments, DPI 418.8. EY: 78% GenAI adoption, 84% CX impact, up to 46% productivity by 2030. Deloitte: 74% RPA, 67% AI/ML. McKinsey: 15–20% net cost reduction. HDFC: 75%+ digital acquisitions, 90 lakh WhatsApp/month. ICICI: 71% digital trade.

### Q21. Explain Figure 1.
**Answer:** Figure 1 shows verified adoption and digitization indicators from the real data database — including RBI 99.8% digital payments, EY 78% GenAI, Deloitte 74% RPA, 67% AI/ML, ICICI 71% digital trade, HDFC 75%+ digital acquisitions, and EY 59% customer AI expectation. All values come from published sources, not invented survey data.

### Q22. Explain Figure 5 — how did you compare banks?
**Answer:** Figure 5 shows **only bank-disclosed metrics** from annual reports — not subjective index scores. It compares percentage-based disclosures like HDFC's 75%+ digitally driven acquisitions versus ICICI's 71% digital trade transactions. Non-percentage metrics (90 lakh WhatsApp, merchant counts) appear in Table 3. I did not assign my own maturity scores.

### Q23. Explain Figure 6 — RBI Digital Payments Index.
**Answer:** Figure 6 plots only two **RBI-verified** DPI values: 377.5 (September 2022) and 418.8 (September 2023), a 10.9% year-on-year increase. No projected or estimated future values are included — only official RBI data.

### Q24. What does Figure 3 show if it's not about challenges?
**Answer:** Figure 3 shows **EY consumer demand indicators** from their survey of 2,030 customers: 59% expect AI-powered financial guidance and 89% want unified banking services. These are demand-side pressure metrics — not invented challenge severity scores. Implementation challenges are discussed qualitatively in Table 6 using EY-Parthenon and Deloitte research.

### Q25. What is the TOE framework (Figure 9)?
**Answer:** Technology-Organization-Environment framework explains AI adoption through three factors: **Technology** (legacy systems, data, APIs), **Organization** (leadership, skills, governance), and **Environment** (RBI regulation, competition, customer demand). Adoption fails if any layer is weak — technology alone is insufficient.

### Q26. How did you test H1 and H2?
**Answer:** **H1:** Compared disclosed digital metrics across five banks — HDFC and ICICI publish stronger numeric evidence (75%+, 71%, 90 lakh WhatsApp) than SBI/Axis/Kotak whose disclosures are more qualitative. **H2:** Reviewed annual report narratives — HDFC (STP, API Factory) and ICICI (iLens platform) describe process redesign alongside technology, supporting partial acceptance of H2.

---

## SECTION 5: FINDINGS & CONCLUSIONS

### Q27. What are your three most important findings?
**Answer:** (1) India is overwhelmingly digital at the payment layer (99.8% RBI) — back-office must catch up; (2) AI/automation adoption is mainstream (78% GenAI, 74% RPA) with documented 15–46% productivity potential; (3) Top barriers are AI talent shortage and legacy integration, not lack of technology availability.

### Q28. What conclusions did you draw?
**Answer:** Five conclusions: (1) Transformation is real and evidenced by regulatory/industry data; (2) Benefits require concurrent investment in talent, data, and governance; (3) Secondary methodology is honest and appropriate for MBA scope; (4) Banks need phased, governed, process-centric adoption; (5) Every claim in the report is traceable to published sources.

### Q29. Is H1 fully supported?
**Answer:** Yes, with qualification. Banks with richer numeric disclosures (HDFC, ICICI) demonstrate stronger documented digital operations outcomes. The qualification is that SBI's scale makes absolute comparison difficult — YONO serves national scale but numeric comparators are limited in public reports.

### Q30. Is H2 fully supported?
**Answer:** Partially. ICICI's iLens and HDFC's STP/API Factory evidence supports platform-based process redesign. However, full proof would require internal process metrics unavailable in public reports — so I state partial support, not full confirmation.

---

## SECTION 6: RECOMMENDATIONS & PRACTICAL APPLICATION

### Q31. What is your top recommendation for banks?
**Answer:** Establish an **operations-led AI steering committee** and conduct **process mining before buying automation tools**. Technology purchases should follow process understanding — not precede it. Automating broken processes only accelerates defects.

### Q32. What is the phased implementation roadmap?
**Answer:** Five phases from Figure 8: (1) **Assess** — process mining; (2) **Prioritize** — business case and impact-feasibility matrix; (3) **Pilot** — KPI tracking on limited scope; (4) **Scale** — reuse components and APIs; (5) **Optimize** — governance audit and continuous improvement.

### Q33. How can Adhiita Consultancy use your findings?
**Answer:** Advisors can cite RBI statistics for digitization urgency, EY/McKinsey for productivity business cases, and HDFC/ICICI disclosures for client benchmarking. The real data database provides a reusable evidence base for client presentations — replacing generic technology advocacy with cited numbers.

### Q34. What is human-in-the-loop and why recommend it?
**Answer:** Human-in-the-loop means keeping human review for high-impact automated decisions — credit denial, fraud account freezing, AML escalation. Fully autonomous decisions in these domains increase conduct and legal risk. RBI expectations and model risk management require explainability and auditability.

### Q35. What AI governance do you recommend?
**Answer:** Model inventories, validation documentation, bias testing for credit/customer models, incident response for model failure, vendor audit access, and alignment with RBI supervisory expectations on model risk — as reflected in Deloitte EMEA 2025 survey findings on AI/ML model usage (67% of banks).

---

## SECTION 7: LIMITATIONS, CRITICAL & TRICK QUESTIONS

### Q36. What are the limitations of your study?
**Answer:** Ten limitations including: secondary data only; incomplete cross-bank numeric comparability; mixed geographic samples (US Deloitte vs India EY); EY 2030 figures are projections; five banks only; selective bank disclosure; no proprietary KPI access; English source bias; MBA scope constraints. All are documented in Chapter 6.

### Q37. Examiner may ask: "Did you fabricate any data?"
**Answer:** **No.** An earlier draft incorrectly included a fabricated 52-respondent survey and invented index scores — that was identified and fully removed. The submitted report uses only verified secondary data stored in `banking_ai_real_data.db` with source URLs. Every statistic can be verified against RBI, EY, McKinsey, Deloitte, or bank annual reports. This correction is documented in DATA_AUDIT_REPORT.md.

### Q38. Why should we trust your statistics?
**Answer:** Three reasons: (1) Each statistic links to a published source URL in the database; (2) CSV exports (`data/exports/04_statistics_with_sources.csv`) show full traceability; (3) Charts regenerate from the database via Python — if a source value changes, updating the database updates all figures consistently.

### Q39. Some Deloitte data is from US executives — is that valid for an Indian study?
**Answer:** I acknowledge this as Limitation 4. US Deloitte banking survey data (62% GenAI consideration) is used as a global industry benchmark, not as an India-specific claim. India-specific claims come from RBI and EY India. I state this geographic mix explicitly and interpret US data cautiously.

### Q40. EY says 46% productivity by 2030 — is that achieved?
**Answer:** **No — it is a projection/forecast**, not a realized outcome. I clearly label EY 2025 and McKinsey figures as industry forecasts in Chapter 4 and Limitation 9. Near-term conservative benchmark is McKinsey's 15–20% net cost reduction; 46% represents longer-horizon GenAI potential.

### Q41. Why only five banks?
**Answer:** Purposive sampling based on market leadership and disclosure quality within MBA scope. Five banks represent private sector leaders (HDFC, ICICI, Kotak, Axis) and public sector scale (SBI). Regional and cooperative banks are acknowledged as a gap for future research.

### Q42. What is the difference between your project and a consulting white paper?
**Answer:** My project follows academic structure — literature review, stated methodology, hypotheses, limitations, APA references, and ethical transparency about data sources. A white paper typically advocates a solution without methodological rigor. I triangulate sources and acknowledge what is not known.

### Q43. How is this related to Operations Management — not just IT?
**Answer:** Operations management covers process design, capacity, quality, technology integration, and continuous improvement. AI/automation are **operational levers** affecting cycle time, error rates, cost per transaction, and SLA performance — not merely IT deployments. Recommendations are operations-led (steering committee, process mining, control tower dashboards).

### Q44. What is RPA and where is it used in banking?
**Answer:** Robotic Process Automation — software bots executing repetitive tasks across systems. Deloitte 2022: 74% of organizations already implement RPA. Banking uses: reconciliation, data migration, report generation, KYC document processing. Entry-level automation before AI/ML maturity.

### Q45. What is GenAI's role specifically?
**Answer:** Generative AI enables document summarization, customer response drafting, code generation, and agent-assist tools. EY 2024: 78% of FinServ firms implemented or plan GenAI pilot within 12 months. EY 2025: up to 46% banking ops productivity potential by 2030. I recommend internal pilot before customer deployment with data privacy controls.

---

## SECTION 8: FUTURE SCOPE & CLOSING QUESTIONS

### Q46. What future research do you suggest?
**Answer:** (1) Primary interviews with bank operations leaders; (2) Expand to regional/cooperative banks; (3) Longitudinal study tracking actual productivity gains vs projections; (4) Primary customer satisfaction study linked to AI-enabled operations; (5) Cost-benefit case studies with internal bank KPIs under NDA.

### Q47. How would you implement your recommendations in a mid-size bank?
**Answer:** Start with process mining on highest-volume workflows (KYC, reconciliation); establish small operations-led pilot with KPI gates; invest in data quality for one domain before enterprise rollout; use phased roadmap; benchmark against EY/McKinsey annually; partner with consultancy for independent review — as recommended in Chapter 6.

### Q48. What is the RBI's role in your study?
**Answer:** RBI provides the regulatory foundation — 99.8% digital payment statistic proves operational scale; DPI index (418.8) confirms digitization trend; RBI supervision shapes AI governance requirements. RBI data is the most authoritative source in the study.

### Q49. Summarize your project in 30 seconds for the external examiner.
**Answer:** "I studied AI and automation in banking operations using verified data from RBI, EY, McKinsey, Deloitte, and five bank annual reports — no primary survey. India is 99.8% digital at payments; 78% of FinServ firms adopt GenAI; HDFC and ICICI lead on disclosed metrics; top barriers are talent and legacy systems. I recommend operations-led governance, process mining first, phased rollout, and AI governance aligned with RBI. All data is in a traceable database with source citations."

### Q50. Do you have any questions for the panel?
**Answer (optional closing):** "I would welcome guidance on whether primary research with bank operations managers could be pursued as a post-MBA extension of this study, particularly to validate the EY 2030 productivity projections against real operational KPIs."

---

# PART E — QUICK REVISION CHEAT SHEET

## Must-Memorize Numbers
| # | Stat | Source |
|---|------|--------|
| 1 | 99.8% digital payments | RBI 2024 |
| 2 | 418.8 DPI (+10.9% YoY) | RBI 2024 |
| 3 | 78% GenAI adoption/plan | EY 2024 |
| 4 | 84% CX impact from GenAI | EY 2024 |
| 5 | 74% RPA implemented | Deloitte 2022 |
| 6 | 67% banks use AI/ML | Deloitte 2025 |
| 7 | 46% productivity potential (2030) | EY 2025 |
| 8 | 15–20% net cost reduction | McKinsey 2025 |
| 9 | 75%+ HDFC digital acquisitions | HDFC FY2024 |
| 10 | 90 lakh WhatsApp/month | HDFC FY2024 |
| 11 | 71% ICICI digital trade | ICICI FY2024 |
| 12 | 59% customers expect AI guidance | EY n=2,030 |

## Must-Memorize Phrases
- "Secondary data only — no primary survey"
- "36 statistics, 12 sources, SQLite database"
- "HDFC and ICICI — disclosed metrics, not invented scores"
- "TOE framework — Technology, Organization, Environment"
- "Phased roadmap — Assess, Prioritize, Pilot, Scale, Optimize"
- "Human-in-the-loop for credit, fraud, AML"
- "EY 2030 figures are projections, not achieved results"

## Red Flags to Avoid in Viva
| Do NOT Say | Say Instead |
|------------|-------------|
| "I surveyed 52 bank employees" | "I used verified secondary data only" |
| "HDFC scored 92/100 on my index" | "HDFC disclosed 75%+ digital acquisitions per annual report" |
| "Challenge severity was 58%" | "EY cites insufficient AI expertise as top barrier" |
| "I collected primary data" | "I extracted and verified published secondary data" |
| "All data is Indian" | "Mix of RBI/EY India plus global Deloitte/McKinsey benchmarks" |

---

**End of Viva Summary Report**  
*Prepared for Akash Rawat — MBA Major Project Viva Voce Examination*  
*Artificial Intelligence and Automation in Banking Operations Management*  
*Amity University Online | Adhiita Consultancy Services, Noida*
