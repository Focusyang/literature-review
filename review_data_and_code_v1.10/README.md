# Data and code for a critical review of column generation and branch-and-price acceleration

Version 1.10, 16 October 2026. Version DOI [10.5281/zenodo.23419224](https://doi.org/10.5281/zenodo.23419224).
Concept DOI [10.5281/zenodo.23386415](https://doi.org/10.5281/zenodo.23386415) resolves to the latest
version. Mirrored at https://github.com/Focusyang/literature-review.

Creator: Xinran Yang, School of Management and Engineering, Capital University of Economics and Business, China.

This package accompanies *Accelerating Column Generation and Branch-and-Price with Traditional
and Learning-Guided Methods: A Critical Review*. It contains the coded inventory, adjudication
record, family-level sensitivity table, figure data and code, source locators, supplementary
tables, retained search records, codebook and independent re-coding materials.
It does not reproduce source-paper solver experiments.

## Contents

| Path | Content |
|---|---|
| `data/coded_inventory_v1_10.csv` | 130 method variants from 88 study families; Table A.1 |
| `data/adjudication_v1_10.csv` | 48 records D078-D125, including 46 earlier decisions and two S021 scope checks |
| `data/family_level_sensitivity_v1_10.csv` | 89 family-by-type rows; one mixed-type family enters both type summaries |
| `data/figure3_matrix_v1_10.csv`, `data/figure3_margins_v1_10.csv` | 207 scope memberships and distinct-variant margins |
| `data/selection_flow_v1_10.csv` | Figure A.1 counts and derivations |
| `data/table4_source_locators_v1_10.csv` | Source versions, PDF pages, denominators, located values and source-check notes |
| `data/evidence_s105.csv` | Historical source-level locators mapped to the two v1.10 S105 variants |
| `data/release_1_2/` | Historical release 1.2 evidence, reading and screening tables |
| `supplementary/` | S1: 74 unselected lead records; S2: 24 core families with complete-tree evaluations, with the supplied-UB column |
| `search/` | Retained public discovery records, including the 14 October targeted lookup and the 16 October coverage check |
| `methods/` | Codebook and field dictionary |
| `recoding_pack/`, `recoding_key/` | 27 neutral cases, blank CSV/XLSX forms, definitions and separate first-coder key |
| `code/` | Derived-table, sample and agreement scripts; portable coverage check; figure sources |
| `figures/` | Figures 1-3 and A.1 in PDF, PNG and SVG |

## Counts and units

The full-text frame contains 100 study families: 80 core, 8 supporting and 12 background.
All 88 core or supporting families contribute to the coded inventory. It contains 130 variants,
63 traditional and 67 learning-guided, after the R1 granularity rule. Rows within a family with
identical primary/secondary layers, primary mechanism, scopes and method type are merged.
`merged_from` preserves their earlier identifiers. `adjudication_v1_10` links affected rows to
the recorded decisions and rule labels.

The inventory has 207 variant-scope memberships (97 traditional, 110 learning-guided).
Each variant enters a margin once but may enter several scope cells. One variant has no
measured scope. GU and GU-offline together account for five variants and describe documentation
status, not proof of an incorrect algorithm. The 51 families with learning-guided variants and
38 with traditional variants overlap in one family. Their sensitivity counts are descriptive.

Supplementary Table S2 contains 24 core families with at least one complete B&P/BPC evaluation.
Twenty-three report at least one completed tree solve under their own stopping criteria. A
timeout is not a completed solve. These are not exact-optimality proofs under a common numerical
threshold. A supplied upper bound must be given before or outside the timed run. S046 uses an
internally generated initial solution and node restricted-IP heuristic (No); S091 remains NR.

The Crossref follow-up left 74 unselected records representing 73 independent works, assessed
only at title and available-abstract level. The separate 16 October coverage check used OpenAlex
and arXiv and retained 651 records for 594 works. It retrieved 42/51 learning families and
15/37 classical-only families. It found 23 learning-guided and 73 classical-method works outside
both the frame and Crossref leads, 17 acquisition-list works not coded, and seven works with an
unclear learning role. None was added to this inventory. These counts describe the critical
sample, not literature-wide prevalence.

## Reproducing retained outputs

Run from this folder with Python 3.10 or later (`pip install -r requirements.txt`).

```
python code/make_sample.py --check
python code/build_tables.py --check
python code/selection_counts.py --check
python code/family_sensitivity.py --check
python code/coverage/screen3.py --check
```

Omit `--check` to regenerate the corresponding tables and forms. `selection_counts.py` checks
the full-text frame against the bundled `data/release_1_2/`. `screen3.py` recomputes the coverage
counts from the finalized screening decisions. The optional live
query script is documented in `search/2026-10-16/README_coverage.md`.

```
python code/figures/make_all.py
python code/agreement.py --key recoding_key/first_coder_key.csv --coder2 completed_form.csv --out agreement_results
```

Figures 1 and 2 are conceptual diagrams; Figure 3 is computed from the inventory. Figure A.1
keeps discovery and full-text assessment as separate streams. Figure scripts were written with
AI assistance, as stated in the article. Arial is used, with Liberation Sans as a compatible fallback.

## Independent re-coding

The random set contains 24 variants drawn with `random.Random(20261014).sample` from sorted
identifiers in the frozen 130-variant inventory. The four prespecified boundary variants are
S066-M2, S053-M1, S088-M1 and S045-M1. S045-M1 is also in the random set, giving 27 unique cases
C01-C27. Its key membership is `random|boundary`; it enters both separately reported analyses.

## Coding process and scope

OpenAI GPT-series models accessed through Codex, and Notion AI, assisted discovery, screening,
extraction, initial coding and source checks. The author is the only human coder, set the coding
rules and approved every correction; the re-coding pack is for a later independent check
(article Section 2.2 and Appendix B.3).

The initial 101 full-text reports were obtained through Web of Science, ScienceDirect, SSRN and
other sources; their search strings and query-level results were not retained (article Section 2.1).
The 14 October index records 30 queries and 27 other operations; its 20 negative access or
retrieval entries are not zero-result literature searches.

Table 4 retains the FFCG source's label “total runtime”; whether these values are per-instance
means or 60-instance sums is not stated. Only within-source ratios are used. Kraul's
5695-instance means are derived from the reported class means. Unassigned mechanisms and
conditional recovery/return claims remain bounded by the accessed report versions.

## Rights and integrity

Original review data and documentation use CC BY 4.0; code uses MIT. Third-party material retains
its original rights. Paper PDFs, extracted third-party full text, abstracts, source-page images,
raw API responses, personal contact details and credentials are not distributed.
See `RIGHTS_AND_RELEASE.md`, `CITATION.cff`, and `MANIFEST.sha256`.
