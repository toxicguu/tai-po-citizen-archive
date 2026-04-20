# Ethics

This document sets out the ethical framework applied throughout the production of this registry and risk assessment, and records specific ethical decisions made during cleaning and assessment.

---

## 1. Framework

This project draws on three professional ethical frameworks, adapted for the specific context of citizen-led crisis archives in post-2025 Hong Kong:

1. **SAA Core Values Statement and Code of Ethics** (Society of American Archivists) — particularly the principles of *Responsible Custody*, *Social Responsibility*, and *Access and Use*.

2. **Protocols for Native American Archival Materials** — while this project does not concern Indigenous materials, the Protocols' principles of *community consent*, *harm avoidance*, and *respect for the source community's own decisions about access* translate directly to crisis-affected communities.

3. **IFLA Statement on Privacy in the Library Environment** — particularly the principle that aggregation of individually public data can create new privacy harms.

---

## 2. Core commitments

### 2.1 No de-anonymisation

Anonymous curators remain anonymous. This commitment holds even where:
- Technical means exist to identify them (e.g., WHOIS records, cross-platform correlation)
- Identification would be academically interesting
- Other researchers have already identified them

**Pseudonymous handles are retained only where the curator has publicly self-disclosed the handle on their own platform.** The act of self-disclosure on one's own page is not the same as consent to indexing in an external registry, but it is the closest signal of consent available in a context where direct consultation is often impossible.

### 2.2 Ethical risk is a first-class preservation risk

The risk assessment framework in this repository treats *ethical / privacy risk (R6)* as one of six equal risk dimensions — not as a separate consideration to be addressed after technical preservation planning.

This is a deliberate methodological choice. Traditional digital preservation risk frameworks (DRAMBORA, DPC RAM, NDSA Levels) focus on technical risks and address ethics in separate governance documents. For crisis archives documenting vulnerable communities, this separation is dangerous: it frames preservation as something to be done first and ethically reviewed later, when in fact some resources should not be technically preserved at all.

### 2.3 Recognition of aggregation harm

Content that is individually public does not give consent to collective aggregation. A Threads post by a survivor, visible to anyone searching the hashtag at the moment of posting, is not the same resource as that post captured, indexed, and cross-referenced within a research archive.

This is the principle of **contextual integrity** (Helen Nissenbaum's framing): information flows are appropriate only when they match the norms of the context in which the information was originally disclosed. A grieving survivor posting to a hashtag for community solidarity did not consent to that post appearing in a case study downloaded by international researchers in 2027.

### 2.4 No data capture in producing this assessment

This study *describes* archives; it does not *preserve* them. No content was scraped, mirrored, or captured during the production of this registry. Only metadata describing the resources was collected.

Preservation recommendations in the `mitigation_actions` sheet are *recommendations for institutional actors* with appropriate ethical review processes, not actions that have been performed.

---

## 3. Specific ethical decisions

### 3.1 Records flagged for mandatory ethical review

Three records (R6 score = 25/25) require ethical review before any technical preservation action:

| ID | Resource | Concern |
|---|---|---|
| **WFC-015** | 宏福苑報平安 (Google Sheet) | Crowdsourced missing-persons dataset. May contain identifiable personal data about survivors and deceased. |
| **WFC-016** | 尋親庇護中心即時名單 (Vercel app) | Real-time missing-persons directory. Same concerns as WFC-015. |
| **WFC-019** | 宏福苑 Threads Back Up (Google Drive) | Aggregated first-hand accounts from survivors. Individual posts were public; aggregation creates new exposure. Curator (@hkbackupper) is pseudonymous and high-profile target. |

For these records, the recommendation is **metadata-only preservation**: capture that the resource exists, its URL, its creator, its date, and its purpose. Do not capture or mirror the contents.

If full preservation is later deemed justified by an appropriate ethical review board, recommendations include:
- **Dark archive deposit** with restricted access
- **Tiered access**: metadata public, content researcher-only under NDA
- **Embargo periods**: e.g., 30-year restriction before any public access
- **Consultation with the originating community** where possible

### 3.2 Handles retained

The following identifying information was retained in the registry because it had been publicly self-disclosed by the relevant curator on their own platform at time of cleaning:

- `heilcheng` (WFC-008) — GitHub username, publicly displayed on the repository
- `hklittlefinger` (WFC-003) — GitHub username
- `hklittlefinger@gmail.com` (WFC-003) — published in the curator's own README
- `taipovigil.hk@proton.me` (WFC-011) — published on the curator's own site
- `@hkbackupper` (WFC-019) — Threads handle, self-associated with the Google Drive

No inference was made beyond what curators had themselves published.

### 3.3 Handles NOT retained

The source spreadsheet included Instagram handles `@wangfukmemories` and `@writingforwangfuk` in the Notes column of unrelated rows. These handles are real and belong to active accounts. They were:
- Recognised as misplaced data (not belonging to the rows they appeared in)
- Associated with the correct aggregated records (WFC-020 and WFC-021)
- Included in the `dc_description` of those ecosystem records, because the handles were evidently the creator's intended self-identification on their own platform

No additional information (post counts, follower counts, post content) was collected.

### 3.4 No cross-platform correlation

In several cases, cross-referencing platforms could plausibly identify the real person behind a pseudonym. This was not performed.

---

## 4. Limitations and open questions

### 4.1 This framework does not substitute for community consultation

Ideally, a case study of this kind would involve direct consultation with the curators and, where possible, with affected community members in Tai Po. The political context of post-2025 Hong Kong makes such consultation complicated, both for researcher safety and for participant safety. This study proceeds without that consultation and acknowledges the limitation.

### 4.2 The researcher's position

The case study author's position (citizenship, institutional affiliation, language competence, proximity to Hong Kong) shapes which archives were discoverable, which curators were approachable, and which ethical risks were salient. These factors should be disclosed in any academic publication derived from this repository.

### 4.3 Temporal risk

Ethical risk is not static. A resource that is safe to preserve in 2026 may become dangerous to preserve in 2028, or vice versa. Preservation decisions should be revisited periodically, not made once and frozen.

### 4.4 The preservation / protection trade-off

There is a genuine tension between two goods:
- **Preservation**: ensuring that the citizen documentation of this event is not lost
- **Protection**: ensuring that preserving the documentation does not harm those who created it or those it describes

These goods cannot always be reconciled. Where they conflict, this project resolves the tension in favour of protection. Other researchers may reasonably weigh them differently; the framework in this repository makes the trade-offs visible so that alternative resolutions can be reasoned about.

---

## 5. References

- Society of American Archivists. *Core Values Statement and Code of Ethics.* https://www2.archivists.org/statements/saa-core-values-statement-and-code-of-ethics
- First Archivists Circle. *Protocols for Native American Archival Materials.* http://www2.nau.edu/libnap-p/
- IFLA. *Statement on Privacy in the Library Environment.*
- Nissenbaum, Helen. *Privacy in Context: Technology, Policy, and the Integrity of Social Life.* Stanford University Press, 2010.
- Caswell, Michelle, and Marika Cifor. "From Human Rights to Feminist Ethics: Radical Empathy in the Archives." *Archivaria* 81 (2016): 23–43.
- Christen, Kimberly. "Opening Archives: Respectful Repatriation." *American Archivist* 74, no. 1 (2011): 185–210.
