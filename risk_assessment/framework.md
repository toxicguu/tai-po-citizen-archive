# Risk Assessment Framework

This is the Markdown version of the `framework` sheet in `risk_assessment.xlsx`, provided for readability on GitHub.

## Scoring

Each record is scored on **six risk dimensions** (R1–R6). Each dimension is scored on two axes:

- **Likelihood** (1–5): how probable the risk is
- **Impact** (1–5): how severe the consequence would be

Risk score per dimension = Likelihood × Impact (range 1–25).
Total risk score per record = sum of six dimensions (range 6–150).

## Bands

| Band | Total score | Action horizon |
|---|---|---|
| LOW | < 60 | Monitor; document citation |
| MEDIUM | 60–89 | Mitigation within 12 months |
| HIGH | ≥ 90 | Urgent action within 30 days |

Additionally, any single-dimension score ≥16 triggers attention regardless of total.

---

## R1 — Link rot / URL decay

| Score | Likelihood | Impact |
|---|---|---|
| 1 | URL on institutional / open-infra platform | Loss of URL inconsequential — content mirrored |
| 2 | Stable custom domain, well-maintained | Minor access disruption |
| 3 | Custom domain, uncertain renewal | Content findable via search but hard |
| 4 | Free-tier hosting or unclear domain | Content effectively lost unless pre-archived |
| 5 | No canonical URL / already ephemeral | Complete loss of access |

## R2 — Platform dependency

| Score | Likelihood | Impact |
|---|---|---|
| 1 | Open infrastructure (Wikimedia, Internet Archive, Zenodo) | Platform failure essentially impossible |
| 2 | GitHub, Google Workspace, major cloud | Migration path available |
| 3 | Mainstream SaaS (Notion, Airtable) | Export possible but manual |
| 4 | Free-tier specialty platform | Content format locked to platform |
| 5 | Ephemeral / experimental platform | Content unrecoverable if platform dies |

## R3 — Custodial abandonment

| Score | Likelihood | Impact |
|---|---|---|
| 1 | Institutional curator (NGO / broadcaster / university) | Institution continues maintenance |
| 2 | Named active curator with stated plans | Curator responds to preservation outreach |
| 3 | Active but anonymous or uncertain curator | Outreach may succeed |
| 4 | Sporadic updates or silent curator | Likely unreachable for cooperation |
| 5 | Explicitly stopped or abandoned | No curator action possible |

## R4 — Format obsolescence

| Score | Likelihood | Impact |
|---|---|---|
| 1 | Open, widely-supported format (HTML, PDF/A, TXT, CSV, JPEG) | Readable indefinitely |
| 2 | Standard formats (DOCX, XLSX, MP4) | Tool support stable for decades |
| 3 | Platform-native export (Notion HTML, Google Sheets) | Readable but some feature loss |
| 4 | Specialist format (FDS, proprietary GIS, AI-generated code) | Requires specialist tools |
| 5 | Undocumented or interface-only content | Cannot be preserved as data |

## R5 — Legal / political risk

| Score | Likelihood | Impact |
|---|---|---|
| 1 | Neutral content, no political valence | No takedown risk |
| 2 | Community support content, apolitical | Very low takedown risk |
| 3 | Community coordination, implicitly political | Platform moderation possible |
| 4 | Accountability / transparency content | Targeted takedown plausible |
| 5 | Investigative or victim-voice aggregation | High risk of legal or state pressure |

## R6 — Ethical / privacy risk

| Score | Likelihood | Impact |
|---|---|---|
| 1 | Fully public, consented, institutional content | No subject harm possible |
| 2 | Public content, no identifiable individuals | Minimal privacy implications |
| 3 | Named volunteers / curators | Creator identification possible |
| 4 | First-hand victim accounts (public but sensitive) | Re-exposure harm through aggregation |
| 5 | Missing-persons data or identifiable victim information | Serious harm potential to vulnerable subjects |
