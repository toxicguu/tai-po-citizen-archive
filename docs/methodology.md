# Methodology

This document describes the workflow used to produce the cleaned registry and preservation risk assessment in this repository. It is intended to be reusable for similar crisis-archive case studies.

---

## 1. Scope and research question

**Event:** Wang Fuk Court fire, Tai Po, Hong Kong, 26 November 2025.

**Research question:** What is the preservation status of citizen-led digital archives documenting the Wang Fuk Court fire, and what preservation actions are required to prevent their loss?

**Scope:** 21 digital archives identified by the case study author through community outreach, public search, and social media discovery between late 2025 and early 2026. Records include: GitHub repositories, Notion pages, Google Sheets and Forms, Vercel-hosted web apps, custom-domain websites, a StoryMap, a Google Calendar, a Google Drive folder, and two social media hashtag ecosystems.

**Out of scope:** Professional media archives, government records, and personal archives not made public.

---

## 2. Workflow overview

The study proceeded in three phases, each producing a discrete deliverable:

```
Phase 1 — Data cleaning         →  data/registry.xlsx
Phase 2 — Risk assessment       →  risk_assessment/risk_assessment.xlsx
Phase 3 — Repository packaging  →  this repository
```

---

## 3. Phase 1 — Data cleaning

### 3.1 Source assessment

The source spreadsheet was inspected without modification. Initial inventory revealed:
- A `Database` sheet with 19 real records plus stray notes and a trailing curator memo
- A `Back Up` sheet with approximately 10 additional records (social media hashtags, a documentary, a photo repository)
- A `Controlled Vocab` sheet containing only keyword hashtags

### 3.2 Structural decisions

Three structural decisions were taken before any field-level cleaning:

1. **Merge, with consolidation.** Entries from the `Back Up` sheet were merged into a single unified registry. The 15 individual hashtag entries (8 Threads + 7 Instagram) were consolidated into 2 "ecosystem" records (WFC-020, WFC-021) to avoid treating each hashtag as a separate archive; individual hashtags are retained in `hashtags.csv` for granular reference.

2. **Schema migration.** Original columns (`Name`, `Type`, `Purpose`, `Description`, `Content`, `Status`, `Creator Type`, `Date Created`, `Date Last updated`, `Plateform`, `Notes`, `URL`) were mapped to a **Dublin Core application profile** with `dcx_` extensions for locally defined elements. Full schema in `schema.md`.

3. **Faceted splitting.** The original `Type` column conflated content genre, format, and hosting platform. It was split into three orthogonal facets: `dc_type` (DCMI Type vocabulary), `dc_format` (genre/format), and `dcx_platform` (hosting). This follows Ranganathan's faceted classification principle.

### 3.3 Field-level cleaning

| Problem | Resolution |
|---|---|
| Column header `Name ` (trailing space) | Normalised to snake_case |
| Column header `Plateform` (misspelled) | Renamed to `dcx_platform` |
| Dates in 6+ formats (`2025-12-01 00:00:00`, `Dec 6, 2025`, `February 15, 2026`, `unknown`, `/`, `auto-update`, blanks) | All normalised to EDTF / ISO 8601. Unknown year = `uuuu`. `auto-update` recoded as `dcx_date_certainty = ongoing`. |
| `unknown` encoded four ways (`unknown`, `/`, blank, `NaN`) | Unified: missing values = empty string; uncertain dates = `uuuu`; anonymised creators = `[anonymous]` with explicit `dcx_creator_anonymity` facet |
| `Status` value `Stop` | Recoded as `inactive`; `ongoing` added for crowdsourced / auto-updating resources |
| Creator column mixing anonymised labels and real handles | Separated via `dcx_creator_anonymity` facet (named / pseudonymous / anonymous_individual / anonymous_group / institutional) |
| No stable identifier | Assigned local persistent identifiers `WFC-001` through `WFC-023` |

### 3.4 Preservation of original intent

Every cleaning decision was logged in the `cleaning_log` sheet with date, category, and rationale. The log serves as an audit trail enabling future reviewers to understand and, if needed, reverse transformations. See `cleaning_log.md` for the full log.

---

## 4. Phase 2 — Risk assessment

### 4.1 Framework selection

Three established digital preservation risk frameworks were considered:

- **DPC Rapid Assessment Model (DPC RAM)** — organisation-level capability maturity model
- **NDSA Levels of Digital Preservation** — 5 functional areas × 4 levels
- **DRAMBORA** — repository audit method based on risk

None was a direct fit: DPC RAM and DRAMBORA assume an institutional custodian, which is precisely what citizen archives lack. NDSA Levels assumes an active preservation programme, which these archives do not have.

A **hybrid framework** was therefore constructed:
- Risk categories drawn from the **DCC (Digital Curation Centre)** and **Library of Congress NDIIPP** taxonomies
- **Likelihood × impact scoring** from classic risk management (both scored 1–5, producing a risk score 1–25 per dimension)
- **Per-record assessment** rather than organisation-level
- **Ethical risk as a first-class dimension** alongside technical risk (see `ethics.md`)

### 4.2 Six risk dimensions

| Code | Category | Focus |
|---|---|---|
| R1 | Link rot | Will the URL resolve in 1, 5, 10 years? |
| R2 | Platform dependency | Will the hosting platform still exist and support the resource? |
| R3 | Custodial abandonment | Will there still be a curator maintaining it? |
| R4 | Format obsolescence | Will the content format remain readable? |
| R5 | Legal / political risk | Is the resource vulnerable to takedown or censorship? |
| R6 | Ethical / privacy risk | Could preservation cause harm to creators or data subjects? |

Full rubrics (what each 1–5 score means per dimension) are in the `framework` sheet of `risk_assessment.xlsx`.

### 4.3 Scoring procedure

Each record was scored on all six dimensions by the case study author, based on:
- Publicly observable characteristics of the resource (hosting platform, custom domain, update frequency)
- Stated custodian information (institutional / named / pseudonymous / anonymous)
- Content sensitivity (does it contain identifiable victim information?)
- General post-2025 Hong Kong context for R5

Scoring is **necessarily subjective** — this is acknowledged as a methodological limitation. Mitigation: rationales are documented in the `rationale` column of the `scoring_matrix` sheet so that future reviewers can challenge individual scores.

### 4.4 Aggregation and banding

Total risk score per record = sum of six dimension scores (range 6–150).

Banding thresholds:
- **LOW** < 60
- **MEDIUM** 60–89
- **HIGH** ≥ 90

Additionally, any record scoring ≥16 on a single dimension is flagged for attention regardless of aggregate.

### 4.5 Mitigation planning

For every record, concrete actions were specified at one of six priority levels:
- **URGENT** — within 30 days
- **SHORT-TERM** — within 6 months
- **LONG-TERM** — 6+ months
- **ONGOING** — continuous monitoring
- **ETHICAL** — flags an ethical consideration, not a technical action
- **RECOMMENDED** — optional action

Actions draw on established web archiving and digital preservation tools: Internet Archive Wayback Machine, Browsertrix / Webrecorder for WARC capture, Software Heritage for code repositories, Zenodo for DOI deposit, and the `.ics` / GeoJSON / Markdown export paths for platform-specific content.

---

## 5. Phase 3 — Repository packaging

The repository was structured to serve three audiences:

1. **Case study examiners** — `README.md` provides executive summary; `docs/` provides methodology and rationale
2. **Other researchers reusing the data** — `data/` provides CSV and JSON exports licensed CC BY 4.0
3. **Archivists adapting the methodology to other crisis events** — `risk_assessment/risk_assessment.xlsx` → `framework` sheet is reusable; this methodology document describes the workflow

Dual licensing (CC BY 4.0 for metadata and documentation, MIT for code) follows standard practice for research data repositories.

---

## 6. Limitations

- **Sampling.** The 23 records are not a complete census of Wang Fuk Court citizen archives. They are those known to the case study author at time of cleaning.
- **Subjective scoring.** Risk scores reflect the author's judgment, documented in rationales. Inter-rater reliability was not tested.
- **Point-in-time snapshot.** The assessment reflects the state of archives on 2026-04-13. Link rot and custodial abandonment will continue to change.
- **Language.** Most records are in Cantonese / Traditional Chinese. Description fields retain original language; alternative titles provide English.
- **No direct capture performed.** This study assesses risk; it does not itself preserve the archives. Preservation actions are recommendations for institutional actors.

---

## 7. Reuse

The methodology, framework, and schema in this repository are explicitly designed for reuse in other crisis-archive case studies. To adapt:

1. Replace the 23 records in the registry with records from your case
2. Adjust the DCMI Type and format vocabularies if your material differs
3. Re-score each record using the framework rubric in `framework` sheet — rubrics are event-independent
4. Adjust the R5 (legal / political) baseline to reflect the political context of your case
5. Update the ethics document (`docs/ethics.md`) to reflect the specific vulnerabilities of your subject community

---

## 8. References

- Dublin Core Metadata Initiative. *DCMI Metadata Terms.* https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
- Library of Congress. *Extended Date/Time Format (EDTF) Specification.* https://www.loc.gov/standards/datetime/
- Society of American Archivists. *Core Values Statement and Code of Ethics.*
- Digital Preservation Coalition. *Rapid Assessment Model (DPC RAM).*
- National Digital Stewardship Alliance. *Levels of Digital Preservation.*
- Digital Curation Centre. *Curation Lifecycle Model.*
- International Council on Archives. *Universal Declaration on Archives.*
- IFLA. *Statement on Privacy in the Library Environment.*
