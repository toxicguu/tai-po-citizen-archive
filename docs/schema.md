# Schema — Dublin Core Application Profile

This registry uses a **Dublin Core (simple) application profile** with locally defined extensions (prefixed `dcx_`).

## Design principles

1. **Reuse standards where possible.** The core fields (`dc_*`) map directly to Dublin Core Metadata Terms, enabling trivial export to any Dublin Core-aware system (OAI-PMH, DSpace, Omeka, etc.).
2. **Extend, don't mutate.** Where Dublin Core is insufficient, extensions are added under the `dcx_` prefix rather than overloading existing fields. `x` = extension.
3. **Facet rather than concatenate.** Fields that would otherwise conflate multiple dimensions (e.g., content type + hosting platform) are split into orthogonal facets.
4. **Controlled vocabularies for categorical fields.** Any field with a closed set of values has a corresponding vocabulary sheet in `data/`.

## Field definitions

### Core (Dublin Core)

| Field | DC term | Definition |
|---|---|---|
| `dc_identifier` | `identifier` | Local persistent identifier. Format: `WFC-###`. Stable across name changes. |
| `dc_title` | `title` | Primary title in original language (usually Cantonese / Traditional Chinese). |
| `dc_title_alternative` | `title.alternative` | Romanised or English title, where available. |
| `dc_type` | `type` | DCMI Type Vocabulary term (see `vocab_dc_type.csv`). |
| `dc_format` | `format` | Genre or format descriptor (e.g., Database, Map, Documentary). |
| `dc_description` | `description` | Scope and content narrative. Retains original language. |
| `dc_subject` | `subject` | Keywords and topics, semicolon-separated. |
| `dc_creator` | `creator` | Attributed creator. Uses `[anonymous]` for undisclosed; see also `dcx_creator_anonymity`. |
| `dc_date_created` | `date.created` | EDTF date of creation. `uuuu` = unknown year. |
| `dc_date_modified` | `date.modified` | EDTF date of most recent modification. |
| `dc_language` | `language` | ISO 639-1 code(s), semicolon-separated. |
| `dc_identifier_url` | `identifier` (URI form) | Canonical URL of the resource. |

### Extensions (`dcx_`)

| Field | Rationale for extension |
|---|---|
| `dcx_platform` | Dublin Core has no dedicated "hosting platform" field. Separating platform from `dc_format` is essential for risk assessment (R2 platform dependency). |
| `dcx_creator_anonymity` | Captures the *type* of anonymity (anonymous_individual / anonymous_group / pseudonymous / named / institutional) as a facet, enabling analysis without de-anonymising. |
| `dcx_date_certainty` | Marks whether a date is known, approximate, unknown, or ongoing. EDTF has some provisions for this but `dcx_date_certainty` provides a simpler, enumerated alternative. |
| `dcx_status` | Lifecycle state (active / inactive / ongoing). Not directly expressible in Dublin Core. |
| `dcx_contact` | Public contact information, retained only where curator had already self-disclosed. |
| `dcx_notes` | Free-text archivist notes. Distinct from `dc_description` (which describes the resource) in that `dcx_notes` describes the *record about* the resource. |

## Controlled vocabularies

Five vocabularies are published alongside the registry:

| File | Scope |
|---|---|
| `vocab_dc_type.csv` | DCMI Type terms used: Collection, Dataset, InteractiveResource, MovingImage, StillImage, Software, Text |
| `vocab_status.csv` | active, inactive, ongoing |
| `vocab_date_certainty.csv` | known, approximate, unknown, ongoing |
| `vocab_anonymity.csv` | named, pseudonymous, anonymous_individual, anonymous_group, institutional |
| `hashtags.csv` | Individual hashtags aggregated under WFC-020 (Threads) and WFC-021 (Instagram) |

## Export paths

The registry is provided in three formats:

- **`registry.xlsx`** — Full workbook with vocabularies, cleaning log, and README
- **`registry.csv`** — Flat CSV for programmatic access
- **`registry.json`** — JSON array, one object per record, for web applications

All three are generated from the same source and contain identical data.

## Compatibility notes

- **Dublin Core export:** Drop all `dcx_*` fields; remaining `dc_*` fields are valid simple Dublin Core.
- **OAI-PMH:** The `dc_*` subset can be exposed via OAI-PMH using the `oai_dc` metadata prefix with no transformation.
- **Schema.org:** A mapping to `schema.org/Dataset` and `schema.org/CreativeWork` is feasible but not currently provided.
- **DataCite:** Local identifiers (`WFC-###`) are not DOIs. If DOI assignment becomes desirable, Zenodo deposit would be the recommended path.
