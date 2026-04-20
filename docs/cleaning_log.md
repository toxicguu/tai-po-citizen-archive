# Cleaning Log

Audit trail of transformations applied to the source spreadsheet. Every decision that altered, recoded, restructured, or discarded data is recorded here.

**Source file:** `Tai_Po_Citizen_Archive.xlsx` (user-supplied)
**Cleaned on:** 2026-04-13
**Target schema:** Dublin Core (simple) + `dcx_` extensions
**Date format target:** EDTF / ISO 8601

---

## Structural changes

| Action | Rationale |
|---|---|
| Merged `Database` sheet (19 records) and `Back Up` sheet (~10 records) into a single unified registry | Source split was organisational, not semantic; all entries are in scope |
| Consolidated 15 individual hashtag rows from `Back Up` sheet into 2 ecosystem records (WFC-020 Threads, WFC-021 Instagram) | Individual hashtags are not independently preservable archives; they are collectively a "hashtag ecosystem" around the event. Granular hashtags preserved in `hashtags.csv`. |
| Promoted CNA documentary (WFC-022) and Wikimedia Commons (WFC-023) from `Back Up` to main registry | These are standalone archival resources, not ancillary to other entries |
| Removed trailing curator memo at source row 29 ("Discover > wide use of AI, curators are in young age, repetitive and unorganized") | This is curator paradata (observation about curation process), not a record. Moved conceptually into the case study narrative. |
| Removed stray `@wangfukmemories @writingforwangfuk` entries in empty rows | These are social media handles belonging to WFC-020 and WFC-021; merged into those records |

## Schema changes

| Action | Rationale |
|---|---|
| Migrated to Dublin Core (simple) with `dcx_` extensions | Web-friendly, widely supported, trivially exportable |
| Split original `Type` column into three facets: `dc_type` / `dc_format` / `dcx_platform` | Original column conflated content genre, format, and hosting platform — three independent dimensions for risk analysis |
| Added `dcx_creator_anonymity` facet | Allows analysis of creator anonymity patterns without de-anonymising |
| Added `dcx_date_certainty` facet | Separates date value from confidence in that value |
| Renamed columns to snake_case | Programming-friendly, standard practice |

## Field-level normalisation

| Original | Cleaned | Rationale |
|---|---|---|
| `Name ` (trailing space) | `dc_title` | Whitespace error |
| `Plateform` | `dcx_platform` | Spelling correction |
| `Date Created`, `Date Last updated` | `dc_date_created`, `dc_date_modified` | ISO / EDTF format |
| Mixed date formats (`2025-12-01 00:00:00`, `Dec 6, 2025`, `February 15, 2026`) | ISO 8601 `YYYY-MM-DD` | Standardisation |
| `unknown` (date) | `uuuu` | EDTF convention for unknown year |
| `auto-update` (date) | `dcx_date_certainty = ongoing` | Recoded as certainty, not date value |
| `/` (notes, contact) | empty string | Unified null encoding |
| `NaN`, blank | empty string | Unified null encoding |
| `Stop` (status) | `inactive` | Standard terminology |
| Anonymous creators (blank or "Anonymous group/individual") | `[anonymous]` + `dcx_creator_anonymity` category | Explicit anonymisation marker + typed facet |

## Identifier assignment

| Action | Rationale |
|---|---|
| Assigned local PIDs `WFC-001` through `WFC-023` | No stable identifiers existed in source; identifiers enable citation and cross-reference |
| Ordering broadly follows source order, with `Back Up` sheet entries appended | Preserves original curatorial order where possible |

## Ethical decisions

| Decision | Rationale |
|---|---|
| No new creator identification performed | Anonymous curators remain anonymous regardless of whether identification is technically possible |
| Retained real handles (`heilcheng`, `hklittlefinger`, `@hkbackupper`) | Each curator had already publicly self-disclosed these on their own platform |
| Retained public email `hklittlefinger@gmail.com` | Published in the curator's own GitHub README |
| Retained ProtonMail `taipovigil.hk@proton.me` | Published on the curator's own site; choice of ProtonMail indicates curator awareness of operational security |
| Did NOT capture or mirror contents of WFC-015, WFC-016, WFC-019 | These contain missing-persons data or victim accounts; registry-level description only |

## Language

| Action | Rationale |
|---|---|
| Retained original language in `dc_description` | Preserves voice and avoids translation loss |
| Added `dc_title_alternative` where an English / romanised title exists | Accessibility for non-Chinese-reading researchers |
| Added `dc_language` ISO 639-1 codes | Standard practice; `zh-HK` for Cantonese; `en` and `zh` for bilingual records |

## Discarded content

The following content from the source was intentionally not carried forward into the cleaned registry, with reasons:

- **Trailing memo** at source row 29 (curator observation about the registry curators) — moved to case study narrative, not a record
- **"AI" as a platform value** for WFC-009, WFC-013, WFC-015 — recoded to the actual hosting platform (Website / Vercel / Google Sheets) where determinable; "AI" was not a hosting platform but a construction method
- **"資安浪人" as a platform value** for WFC-010 — recoded to Website; "資安浪人" appears to be a contributor credit, moved to `dcx_notes`
