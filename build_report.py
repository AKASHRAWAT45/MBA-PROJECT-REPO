#!/usr/bin/env python3
"""Build complete MBA project HTML report from markdown content files."""

import os
import re
from pathlib import Path

BASE = Path(__file__).parent
CONTENT = BASE / "content"
CHARTS = BASE / "charts"
OUT = BASE / "PROJECT_REPORT.html"

STUDENT = "Akash Rawat"
ENROLLMENT = "A9920124013426(el)"
GUIDE = "Madhva Raj Pratinidhi"
TITLE = "Artificial Intelligence and Automation in Banking Operations Management"
ORG = "Adhiita Consultancy Services, Noida"
PROGRAM = "Master of Business Administration"
UNIVERSITY = "Amity University Online, Noida, Uttar Pradesh"
SESSION = "Jul 2024 – Jul 2026, Semester IV"
RUNNING_HEAD = "AI AND AUTOMATION IN BANKING OPERATIONS"
YEAR = "2025"


def read_md(name):
    p = CONTENT / name
    if p.exists():
        return p.read_text(encoding="utf-8")
    return ""


def md_to_html(text):
    if not text.strip():
        return ""
    lines = text.split("\n")
    html = []
    in_table = False
    in_list = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith("## "):
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith("### "):
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f'<h3>{line[4:]}</h3>')
        elif line.strip().startswith("|") and "|" in line.strip()[1:]:
            if not in_table:
                if in_list:
                    html.append("</ul>")
                    in_list = False
                html.append('<table class="data-table">')
                in_table = True
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                i += 1
                continue
            tag = "th" if not any("<td>" in h for h in html[-3:]) and html[-1].endswith("<table class=\"data-table\">") else "td"
            if html[-1].endswith('<table class="data-table">'):
                html.append("<thead><tr>" + "".join(f"<th>{c}</th>" for c in cells) + "</tr></thead><tbody>")
            else:
                html.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
        elif line.strip().startswith("- "):
            if in_table:
                html.append("</tbody></table>")
                in_table = False
            if not in_list:
                html.append("<ul>")
                in_list = True
            html.append(f"<li>{inline_fmt(line.strip()[2:])}</li>")
        elif re.match(r"^\d+\.\s", line.strip()):
            if in_table:
                html.append("</tbody></table>")
                in_table = False
            if not in_list:
                html.append("<ul>")
                in_list = True
            item_text = re.sub(r"^\d+\.\s", "", line.strip())
            html.append(f"<li>{inline_fmt(item_text)}</li>")
        elif line.strip() == "":
            if in_table:
                html.append("</tbody></table>")
                in_table = False
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append("")
        else:
            if in_table:
                html.append("</tbody></table>")
                in_table = False
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f"<p>{inline_fmt(line.strip())}</p>")
        i += 1
    if in_table:
        html.append("</tbody></table>")
    if in_list:
        html.append("</ul>")
    return "\n".join(html)


def inline_fmt(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


def combine_chapter(main, *expansions):
    parts = [read_md(main)]
    for e in expansions:
        parts.append(read_md(e))
    return "\n\n".join(p for p in parts if p)


def fig(name, num, caption):
    return f"""
<figure class="figure">
<img src="charts/{name}" alt="Figure {num}" style="max-width:100%;height:auto;"/>
<figcaption><strong>Figure {num}.</strong> {caption}</figcaption>
</figure>
"""


def table_img(name, table_num, caption):
    return f"""
<figure class="figure">
<img src="charts/{name}" alt="Table {table_num}" style="max-width:100%;height:auto;"/>
<figcaption><strong>Table {table_num}.</strong> {caption}</figcaption>
</figure>
"""


LIST_OF_TABLES = [
    "Table 1. RBI-Reported Payment System and Digital Indicators (FY 2023-24)",
    "Table 2. Published AI and Automation Adoption Indicators",
    "Table 3. Verified Bank-Disclosed Digital Operations Metrics (FY2023-24)",
    "Table 4. Published Benefit Indicators from Industry Research",
    "Table 5. Verified Operational Impact Metrics",
    "Table 6. Published Implementation Challenge Indicators",
    "Table 7. Operational Domain Opportunity Mapping (Evidence-Based)",
    "Table 8. Implementation Priority Matrix for Bank Leadership",
    "Table 9. Verified Secondary Data Sources Registry (12 Published Sources)",
    "Table 10. Verified Statistics Registry with Source Cross-References (36 Metrics)",
]

LIST_OF_FIGURES = [
    "Verified AI, Automation and Digitization Indicators (RBI, EY, Deloitte, Bank ARs)",
    "Documented Benefits from EY and McKinsey Published Research",
    "Customer Demand Indicators — EY Consumer Survey (n = 2,030, 2024). Source: EY India.",
    "Technology Adoption Rates from Deloitte and EY Surveys",
    "Bank-Disclosed Digital Operations Metrics (Annual Reports)",
    "RBI Digital Payments Index — Verified Data Only",
    "Investment Priorities — Deloitte 2024 Banking Survey",
    "Phased AI and Automation Implementation Roadmap for Banking Operations",
    "TOE Framework Applied to Banking AI and Automation Adoption",
]


CSS = """
@page { margin: 1in; }
* { box-sizing: border-box; }
body {
  font-family: "Times New Roman", Times, serif;
  font-size: 12pt;
  line-height: 2;
  color: #000;
  max-width: 8.5in;
  margin: 0 auto;
  padding: 0 0.5in;
}
.running-head {
  font-size: 10pt;
  text-align: left;
  border-bottom: 1px solid #ccc;
  padding: 8px 0;
  margin-bottom: 24px;
}
.page-break { page-break-before: always; }
.title-page { text-align: center; padding-top: 2in; min-height: 10in; }
.title-page h1 { font-size: 16pt; margin: 2em 0; line-height: 1.6; }
.title-page p { font-size: 14pt; line-height: 2; margin: 0.5em 0; }
h1 { font-size: 14pt; font-weight: bold; margin-top: 1.5em; }
h2 { font-size: 13pt; font-weight: bold; margin-top: 1.2em; }
h3 { font-size: 12pt; font-weight: bold; margin-top: 1em; }
p { text-align: justify; margin: 0 0 0.5em 0; text-indent: 0.5in; }
h1 + p, h2 + p, h3 + p, .no-indent p, .title-page p, figcaption, li { text-indent: 0; }
ul, ol { margin: 0.5em 0 0.5em 1in; }
li { margin-bottom: 0.3em; }
.data-table { width: 100%; border-collapse: collapse; margin: 1em 0; font-size: 11pt; line-height: 1.4; }
.data-table th, .data-table td { border: 1px solid #333; padding: 6px 8px; text-align: left; }
.data-table th { background: #f0f0f0; font-weight: bold; }
.figure { margin: 1.5em 0; text-align: center; page-break-inside: avoid; }
figcaption { font-size: 11pt; line-height: 1.5; margin-top: 0.5em; text-align: left; padding: 0 0.5in; }
.toc { line-height: 2; }
.toc a { color: #000; text-decoration: none; }
.highlight { background: #fff3cd; padding: 2px 4px; }
.declaration { margin-top: 2in; line-height: 2; }
@media print {
  .page-break { page-break-before: always; }
  body { padding: 0; }
}
"""


def page_section(content, running_head=True):
    rh = f'<div class="running-head">{RUNNING_HEAD}</div>\n' if running_head else ""
    return f'<div class="page-break">\n{rh}{content}\n</div>\n'


def build():
    ch1 = combine_chapter(
        "chapter1.md", "chapter1_expansion.md", "chapter1_expansion2.md",
        "chapter1_expansion3.md", "chapter1_expansion4.md",
    )
    ch2 = combine_chapter(
        "chapter2.md", "chapter2_expansion.md", "chapter2_expansion2.md",
        "chapter2_expansion3.md", "chapter2_expansion4.md",
    )
    ch3 = combine_chapter(
        "chapter3.md", "chapter3_expansion.md", "chapter3_expansion2.md",
        "chapter3_expansion3.md",
    )
    ch4_before_figures = combine_chapter(
        "chapter4.md", "chapter4_expansion.md", "chapter4_expansion2.md",
        "chapter4_supplement.md",
    )
    ch4_after_figures = combine_chapter(
        "chapter4_expansion3.md", "chapter4_expansion4.md", "chapter4_expansion5.md",
    )
    ch5 = combine_chapter("chapter5.md", "chapter5_expansion.md", "chapter5_expansion2.md")
    ch6 = combine_chapter("chapter6.md", "chapter6_expansion.md", "chapter6_expansion2.md")
    refs = read_md("references.md")
    appendix = read_md("appendix.md") + "\n\n" + read_md("appendix_d.md") + "\n\n" + read_md("DATA_SOURCES.md")

    ch4_html = md_to_html(ch4_before_figures)
    ch4_html += fig("fig1_adoption_by_area.png", 1, "Verified AI, Automation and Digitization Indicators (RBI, EY, Deloitte, Bank ARs)")
    ch4_html += fig("fig2_benefits_rating.png", 2, "Documented Benefits from EY and McKinsey Published Research")
    ch4_html += fig("fig3_challenges.png", 3, "Customer Demand Indicators — EY Consumer Survey (n = 2,030, 2024). Source: EY India.")
    ch4_html += fig("fig4_technology_mix.png", 4, "Technology Adoption Rates from Deloitte and EY Surveys")
    ch4_html += fig("fig5_bank_maturity.png", 5, "Bank-Disclosed Digital Operations Metrics (Annual Reports)")
    ch4_html += fig("fig6_efficiency_trend.png", 6, "RBI Digital Payments Index — Verified Data Only")
    ch4_html += fig("fig7_investment_allocation.png", 7, "Investment Priorities — Deloitte 2024 Banking Survey")
    ch4_html += fig("fig8_implementation_roadmap.png", 8, "Phased AI and Automation Implementation Roadmap for Banking Operations")
    ch4_html += md_to_html(ch4_after_figures)

    ch2_html = md_to_html(ch2) + fig("fig9_toe_framework.png", 9, "TOE Framework Applied to Banking AI and Automation Adoption")

    db_appendix = """
<h2>Appendix E: Verified Secondary Data Registry (Database Snapshot)</h2>
<p>A structured secondary data registry was maintained during research to trace every statistic in this report to its published source. The tables below are static image snapshots of the registry (not dynamically loaded) for submission transparency.</p>
""" + table_img("table_db_sources.png", 9, "Verified Secondary Data Sources Registry (12 Published Sources)") + table_img(
        "table_db_statistics.png", 10, "Verified Statistics Registry with Source Cross-References (36 Metrics)"
    )

    appendix_html = md_to_html(appendix) + db_appendix

    tables_list = "".join(
        f"<p>{t} .......................................................... {38 + i}</p>" for i, t in enumerate(LIST_OF_TABLES)
    )
    figures_list = "".join(
        f"<p>Figure {i + 1}. {cap} .......................................................... {38 + i * 2}</p>"
        for i, cap in enumerate(LIST_OF_FIGURES)
    )

    declaration = f"""<h1>Declaration</h1>
<div class="no-indent declaration">
<p>I, <strong>{STUDENT}</strong>, a student pursuing <strong>{PROGRAM}, Semester IV</strong> at <strong>{UNIVERSITY}</strong>, hereby declare that the project work entitled <strong>&quot;{TITLE}&quot;</strong> has been prepared by me during the academic year <strong>{YEAR}</strong> under the guidance of <strong>{GUIDE}</strong>. I assert that this project is a piece of original bona-fide work done by me. It is the outcome of my own effort and that it has not been submitted to any other university for the award of any degree.</p>
<p style="margin-top:3em;">Signature of Student: _________________________</p>
<p>Date: _________________________</p>
</div>"""

    toc = """<h1>Table of Contents</h1>
<div class="toc no-indent">
<p>Chapter 1: Introduction to the Topic .......................................................... 1</p>
<p>Chapter 2: Review of Literature ................................................................. 12</p>
<p>Chapter 3: Research Objectives and Methodology ........................................ 28</p>
<p>Chapter 4: Data Analysis, Results, and Interpretation ................................ 38</p>
<p>Chapter 5: Findings and Conclusion ............................................................ 58</p>
<p>Chapter 6: Recommendations and Limitations of the Study ........................... 66</p>
<p>Chapter 7: Bibliography / References ........................................................ 76</p>
<p>Appendix .................................................................................................... 80</p>
</div>"""

    title_page = f"""<div class="title-page page-break">
<p><strong>{UNIVERSITY}</strong></p>
<p>In partial fulfillment of the requirement for the award of degree of</p>
<p><strong>Master of Business Administration (MBA)</strong></p>
<p style="margin-top:2em;"><strong>TITLE:</strong></p>
<h1>{TITLE}</h1>
<p><strong>Industry Partner:</strong> {ORG}</p>
<p style="margin-top:2em;"><strong>Guide Details:</strong></p>
<p><strong>Name of Mentor:</strong> {GUIDE}</p>
<p style="margin-top:2em;"><strong>Submitted By:</strong></p>
<p><strong>Name of the Student:</strong> {STUDENT}</p>
<p><strong>Enrollment No:</strong> {ENROLLMENT}</p>
<p><strong>Session:</strong> {SESSION}</p>
</div>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<title>{TITLE} - {STUDENT}</title>
<style>{CSS}</style>
</head>
<body>

{title_page}
{page_section(declaration)}
{page_section(toc)}
{page_section(f'<h1>List of Tables</h1><div class="no-indent">{tables_list}</div>')}
{page_section(f'<h1>List of Figures</h1><div class="no-indent">{figures_list}</div>')}
{page_section(md_to_html(ch1))}
{page_section(ch2_html)}
{page_section(md_to_html(ch3))}
{page_section(ch4_html)}
{page_section(md_to_html(ch5))}
{page_section(md_to_html(ch6))}
{page_section(md_to_html(refs))}
{page_section(appendix_html)}

</body>
</html>
"""
    html = html.replace("<div", "<div").replace("</div>", "</div>")

    OUT.write_text(html, encoding="utf-8")
    word_count = len(re.sub(r"<[^>]+>", " ", html).split())
    print(f"Report written to {OUT}")
    print(f"Approximate word count: {word_count}")
    print(f"Title words: {len(TITLE.split())} (max 12)")


if __name__ == "__main__":
    build()
