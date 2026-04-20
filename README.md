# Tai Po Wang Fuk Court Citizen Archive — Registry & Preservation Risk Assessment

A structured registry and preservation risk assessment of 21 citizen-led digital archives documenting the **Wang Fuk Court fire (Tai Po, Hong Kong, 26 November 2025)**.

Prepared as a case study for the **International Council on Archives (ICA)** on distributed, volunteer-maintained crisis archives.

---

## What is this?

In the weeks following the Wang Fuk Court fire, Hong Kong citizens created dozens of ad-hoc digital archives: Google Sheets for missing-persons check-in, GitHub repositories for independent fire-dynamics investigation, Notion pages aggregating aid resources, Threads and Instagram hashtag ecosystems, Vercel-hosted mutual aid apps, and memorial websites. These archives are:

- **Distributed** — no single custodian
- **Anonymous or pseudonymous** — most curators chose not to disclose identity
- **Technically fragile** — hosted on free-tier platforms, custom domains, or ephemeral services
- **Ethically complex** — some contain missing-persons data or first-hand victim accounts
- **Politically sensitive** — documenting a contested event in post-2025 Hong Kong

This repository provides a **cleaned metadata registry** of 21 such archives, a **preservation risk assessment** across six risk dimensions, and a **methodology** intended to be reusable for similar crisis-archive case studies. The scope is limited to **citizen-created archives only**; institutional media (e.g., CNA documentary) and open-infrastructure repositories (e.g., Wikimedia Commons) are excluded.

---

## Repository contents

```
.
├── README.md                      You are here
├── LICENSE                        CC BY 4.0 (metadata) + MIT (code)
├── CITATION.cff                   How to cite this work
├── CHANGELOG.md                   Version history
│
├── data/                          The cleaned registry
│   ├── registry.xlsx              Full workbook (registry + vocab + cleaning log)
│   ├── registry.csv               Flat CSV export (bilingual descriptions)
│   ├── registry.json              JSON export (bilingual descriptions)
│   ├── vocab_dc_type.csv          Controlled vocabulary: DCMI Type
│   ├── vocab_status.csv           Controlled vocabulary: status
│   ├── vocab_date_certainty.csv   Controlled vocabulary: date certainty
│   ├── vocab_anonymity.csv        Controlled vocabulary: creator anonymity
│   └── hashtags.csv               Individual hashtags aggregated in WFC-020/021
│
├── risk_assessment/               Preservation risk assessment
│   ├── risk_assessment.xlsx       Full workbook (framework + scoring + mitigation)
│   ├── scoring_matrix.csv         Per-record scores on 6 risk dimensions
│   └── mitigation_actions.csv     Action plan per record
│
├── docs/                          Methodology and rationale
│   ├── methodology.md             How the study was conducted
│   ├── schema.md                  Dublin Core application profile
│   ├── cleaning_log.md            Data cleaning audit trail
│   └── ethics.md                  Ethical framework and decisions
│
└── scripts/
    └── validate.py                Integrity check script
```

---

## Quick statistics

| | |
|---|---|
| Records in registry | 21 (citizen archives only) |
| Excluded | Institutional media (CNA documentary) and open-infrastructure repositories (Wikimedia Commons) |
| Metadata schema | Dublin Core (simple) + `dcx_` extensions |
| Date format | EDTF / ISO 8601 (`uuuu` = unknown year) |
| Descriptions | Bilingual: original language + [EN] English translation |
| Risk assessment dimensions | 6 (R1–R6) |
| High-risk records requiring urgent action | 3 |
| Records requiring ethical review before preservation | 3 |

---

## Risk summary

Full assessment in `risk_assessment/`. The six risk dimensions are:

| Code | Risk category |
|---|---|
| R1 | Link rot / URL decay |
| R2 | Platform dependency |
| R3 | Custodial abandonment |
| R4 | Format obsolescence |
| R5 | Legal / political risk |
| R6 | Ethical / privacy risk |

**Top-line findings:**

1. **Custodial abandonment (R3) is the dominant risk pattern** — citizen archives lack institutional handoff mechanisms.
2. **Three records** (WFC-015, WFC-016, WFC-019) **require ethical review** before any technical preservation action; they contain missing-persons data or aggregated victim accounts.
3. **Format obsolescence (R4) is the least severe category** — contradicting the traditional digital preservation emphasis on formats; the real crisis is hosting and custodianship.
4. **GitHub and open-infrastructure records** (Wikimedia Commons, institutional broadcasters) are systematically safer, suggesting a preservation pathway: migrate citizen archives to open infrastructure.
5. **Legal / political risk has an elevated baseline** across the entire registry; no record is politically neutral in the post-2025 Hong Kong context.

---

## How to use this repository

**As a case study reference:**
Read `docs/methodology.md` first, then browse `data/registry.xlsx` and `risk_assessment/risk_assessment.xlsx`.

**For data reuse:**
The CSV and JSON exports in `data/` are licensed CC BY 4.0. Cite using `CITATION.cff`.

**To adapt the methodology for another crisis archive:**
The framework in `risk_assessment/risk_assessment.xlsx` → `framework` sheet is reusable. `docs/methodology.md` describes the workflow step by step.

---

## Ethical commitments

This project follows principles from the **SAA Core Values Statement** (Society of American Archivists), the **Protocols for Native American Archival Materials** (adapted for crisis-affected communities), and the **IFLA Statement on Privacy in the Library Environment**.

Specific commitments:

- **No creator de-anonymisation.** Anonymous curators remain anonymous in this registry. Pseudonymous handles are retained only where the curator had already publicly self-disclosed on their own platform.
- **Ethical risk is a first-class preservation risk.** Missing-persons data and aggregated victim accounts trigger mandatory ethical review before any technical capture.
- **Aggregation harm is recognised.** Individually public posts, when collected and archived together, create new exposure not consented to at the moment of posting.
- **No data was scraped or mirrored in producing this assessment.** Only metadata describing the resources was collected.

See `docs/ethics.md` for full discussion.

---

## Citation

If you use this registry or methodology, please cite using `CITATION.cff`. Short form:

> Tai Po Wang Fuk Court Citizen Archive Registry and Preservation Risk Assessment. 2026. ICA Case Study.

---

## Licence

- **Metadata and documentation** (registry, risk assessment, docs): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code** (scripts/): [MIT](https://opensource.org/licenses/MIT)

See `LICENSE` for full text.

---

## Acknowledgements

To the citizen archivists of Tai Po, Hong Kong, who built these resources in the days after the fire. This registry exists to help ensure their work is not lost.
