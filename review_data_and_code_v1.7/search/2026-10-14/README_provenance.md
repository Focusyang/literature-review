# Search records retained from 14 October 2026

These are historical records recovered on 15 October 2026 from the local v1.5 archive. The audit did not rerun these queries and did not reconstruct missing historical outcomes.

## Contents and counts

The original index records 59 operations: 30 search queries, 25 page opens, 3 link clicks, and one combined publisher/Crossref identity check. Sixteen web-tool response files and the cited Crossref identity response are retained byte-for-byte in the local submission audit archive, outside this public data package. The normalized index only changes raw-record paths and adds audit interpretation. `query_index_original.csv` preserves the historical index bytes.

`retrieval_outcomes.csv` normalizes the archived retrieval index into 18 attempts: 8 downloads succeeded, 3 PDF retrievals failed, and 7 attempts did not identify an OA route. The historical index includes eight successful retrievals even when an earlier web-tool open of the same URL failed. Different tools and attempts must not be merged into one result.

`negative_outcomes.csv` records page access failures and unsuccessful full-text/OA retrieval attempts. They are not zero-result literature searches. No query-level zero-hit record was found. The web responses mix hits from multi-query batches, so an absent identifiable hit for an individual query does not establish zero results. Query result totals, unreturned results and a complete census of negative searches cannot be reconstructed.

Supplement fields saying `not_found` because a direct PDF URL did not identify a landing page describe the retrieval tool's route limitation. They do not show that a publication has no supplement.

## Scope and preservation

The retained queries focus on named classical references, title checks, versions and full-text access. They support a targeted supplementary lookup, not a new comprehensive mechanism-by-learning search. There is no contemporaneous retained paired-query protocol for every named mechanism. The original web batches also include journal-policy lookups, so 59 is an operation count, not a literature search or study count.

`provenance_manifest.csv` maps every locally retained raw file to its original relative workspace location and SHA-256. Historical absolute paths in retrieval records were converted to workspace-relative references in the normalized table. Original retrieval and query indexes remain in the local audit folder. No source-study PDFs are copied into this addition.

Raw response files are not included in this public package because they contain third-party search snippets and retrieved web-page text. Paths beginning with `raw/` in the indexes identify the locally retained historical responses, not downloadable files in this deposit. Their copyright is not transferred by a dataset license. Original factual indexes, disposition records, and the audit summaries may be licensed as part of the review data; third-party quoted content must be identified separately in release rights metadata. The local originals remain the primary historical evidence.

All audit statements describe AI-assisted checks on 15 October 2026. They are not independent human verification and do not establish the author's personal review of every coded item.
