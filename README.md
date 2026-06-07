# MBA Major Project – Submission Package

**Student:** Akash Rawat |

---

## Folder Contents

| File / Folder | Purpose |
|---------------|---------|
| `PROJECT_REPORT.docx` | **Google Docs upload** – main report (Word format) |
| `EXTENDED_ABSTRACT.docx` | Abstract for separate submission(not synced here) |
| `GOOGLE_DOCS_UPLOAD.md` | Step-by-step Google Docs instructions (not synced here)|
| `PLAGIARISM_REPORT.txt` | Plagiarism analysis summary (~0–10% estimated) |
| `charts/` | 7 figures (PNG) embedded in report |
| `generate_charts.py` | Regenerate charts if needed |
| `build_report.py` | Rebuild HTML from chapter markdown |

---

## How to Open in Google Docs (Recommended)

1. Go to [Google Drive](https://drive.google.com)
2. Upload **`PROJECT_REPORT.docx`**
3. Right-click → **Open with → Google Docs**
4. When satisfied, **File → Download → PDF** for Qollabb

See **`GOOGLE_DOCS_UPLOAD.md`** for full instructions.

## Alternative: PDF from Browser

1. Open `PROJECT_REPORT.html` in Chrome
2. Press **Cmd+P** → Save as PDF
3. Turn **Background graphics ON** (for charts)

---

## Formatting Checklist (Amity / Qollabb)

- [x] Title page, Declaration, TOC, List of Tables, List of Figures
- [x] Chapters 1–6 + References + Appendix
- [x] Times New Roman 12pt, double spacing (CSS line-height: 2)
- [x] APA-style references (Chapter 7)
- [x] Running head on pages
- [x] 9 figures + 8 tables
- [x] ~20,000 words (main chapters)
- [x] American spellings (organize, center, recognize)
- [ ] **Your signature** on Declaration (add in Word/PDF editor)
- [ ] **Mentor signed certificate** (scan from guide)
- [ ] **Plagiarism report** ≥85% originality (run through Turnitin/URKUND as required)

---

## Qollabb Submission Steps

1. **Abstract + Guide Resume** – upload `EXTENDED_ABSTRACT.html` (as PDF) and signed `guide_resume`
2. **Final Report PDF** – upload `PROJECT_REPORT.pdf`
3. **Plagiarism Report** – must show ≤15% similarity
4. **Viva Part 1** – copy answers from `content/viva_part1.md` into Qollabb form
5. **Viva Part 2** – complete “Acing Your Interview” on Amigo LMS

---

## Rebuild Report (if editing chapters)

```bash
cd akash-mba-ai-banking-project
export MPLBACKEND=Agg
python3 generate_charts.py
python3 build_report.py
python3 build_abstract.py   # if present
```

---

## Important Notes

- **Originality:** Content is original synthesis for academic submission. Run your institution’s plagiarism checker before final upload.
- **Mentor name:** Madhva Raj Pratinidhi – confirm spelling with Qollabb dashboard.
- **Title length:** 8 words (within 12-word limit).
- **Word count:** Target 15,000–30,000 words met.


