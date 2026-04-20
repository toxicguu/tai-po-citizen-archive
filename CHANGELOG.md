# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-04-16

### Changed
- **Scope refined to citizen archives only.** Removed WFC-022 (CNA documentary) and WFC-023 (Wikimedia Commons) as they are institutional, not citizen-created archives.
- Registry now contains 21 records (WFC-001 through WFC-021).
- All `dc_description` fields now include bilingual content: original language + `[EN]` English translation.
- Risk assessment updated to 21 records; summary statistics recalculated.
- Controlled vocabulary `vocab_dc_type` updated: removed `MovingImage`, `StillImage`, `Text` (no longer used).

## [1.0.0] — 2026-04-13

### Added
- Initial registry of 23 citizen archives (WFC-001 through WFC-023)
- Dublin Core (simple) application profile with `dcx_` extensions
- Five controlled vocabularies: `dc_type`, `status`, `date_certainty`, `anonymity`, plus hashtag list
- Cleaning log with 14 audit entries
- Preservation risk assessment across 6 dimensions (R1–R6)
- Per-record scoring matrix (23 records × 6 dimensions)
- Mitigation action plan (64 actions across 23 records, 6 priority levels)
- Methodology, schema, ethics, and cleaning log documentation
- Integrity validation script

### Notes on source data
- Source spreadsheet contained 19 records in the primary `Database` sheet and
  an additional ~10 records in the `Back Up` sheet. Individual hashtag entries
  (15 total) were consolidated into two ecosystem records (WFC-020 Threads,
  WFC-021 Instagram). The CNA documentary and Wikimedia Commons entries from
  the `Back Up` sheet were promoted to the main registry as WFC-022 and
  WFC-023.
- Final record count: 23.
