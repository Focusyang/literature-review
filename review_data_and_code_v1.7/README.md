# Data and code for a critical review of column generation and branch-and-price acceleration

Version 1.7, 15 October 2026. Public audit version at https://github.com/Focusyang/literature-review/tree/main/review_data_and_code_v1.7. Archived on Zenodo at [10.5281/zenodo.23386416](https://doi.org/10.5281/zenodo.23386416). [Archive record](https://zenodo.org/records/23386416).

Creator: Xinran Yang, School of Management and Engineering, Capital University of Economics and Business, China.

This release supports the article *Accelerating Column Generation and Branch-and-Price with Traditional and Learning-Guided Methods: A Critical Review*. It supersedes release 1.2 for the article's counts, Table A.1, Figure 3, Figure A.1 and Supplementary Tables S1-S2. Release 1.2 remains available unchanged in the repository; its data tables are also included here under `data/release_1_2/`.

## What the release contains

| Path | Content |
|---|---|
| `data/variants_v1_6.csv` | The frozen inventory of 146 coded method variants from 88 core or supporting study families (Table A.1, Figure 3) |
| `data/figure3_matrix_v1_6.csv` | Variant-scope memberships by primary mechanism and scope (245 in total) |
| `data/selection_flow_v1_6.csv` | Counts shown in Figure A.1, recomputed from the search and screening records |
| `data/records_added_v1_6.csv`, `data/studies_added_v1_6.csv` | Records and the study family added since release 1.2 |
| `data/release_1_2/` | Release 1.2 tables: studies, methods, evidence, claims, records, reading reports, screening and version relations |
| `search/` | Retained public search, title-triage and disposition records, including the recovered 14 October query and unsuccessful access/retrieval indexes |
| `data/evidence_s105_v1_7.csv` | Source-version and page locators for all eight S105 variants and five supporting claims |
| `audit/` | Evidence coverage, supplementary-table checks, source comparison checks and unresolved AI coding proposals |
| `supplementary/` | Supplementary Table S1 (74 unselected leads) and Table S2 (complete-tree completion of the 24 core families with E4 evaluation), CSV and XLSX |
| `methods/` | Codebook (version 1.2) with the version 1.6 addendum and the version 1.7 audit note, field dictionaries, derivations and supplementary methods |
| `recoding_pack/`, `recoding_key/` | Materials for an independent re-coding (Appendix B.3) and the first-coder key |
| `code/` | Scripts for figures, supplementary tables, the re-coding sample, selection counts and agreement statistics |
| `figures/` | Figures 1-3 and A.1 (PDF, PNG at 600 dpi, SVG) |
| `CHANGES_v1.2_to_v1.6.csv` | Crosswalk of every change since release 1.2 |

## Counts

100 study families are included: 80 core, 8 supporting and 12 background. The 88 core or supporting families contribute 146 method variants, 72 traditional and 74 learning-guided, with 245 variant-scope memberships. Twenty-four core families include a complete-tree (E4) evaluation. The Crossref follow-up left 74 leads unselected at title and available-abstract level. These counts describe a bounded critical sample, not the prevalence of methods in the literature.

## Changes since release 1.2

* Added family S105 (Sadykov et al., 2019, diving heuristics for branch-and-price; eight variants), identified by a targeted search on 14 October 2026 and read in its HAL author-manuscript version.
* Recoded S064-M1 from GU to GU-offline and S066-M2 from G4 to G2 primary (G4 secondary).
* Added reading records for the extended FFCG report (S059) and the extended in-out smoothing report (earlier report of S018).
* Removed the primary layer from five secondary-layer lists (no substantive change).
* Added Supplementary Tables S1-S2, the re-coding pack and the scripts listed below.

## Reproducing the article outputs

Run from this folder with Python 3.10 or later (`pip install -r requirements.txt`).

```
python code/figures/make_all.py        # Figures 1-3 and A.1 -> figures/
python code/selection_counts.py        # recomputes and checks every count in Figure A.1
python code/build_supplementary.py     # Supplementary Tables S1 and S2 -> supplementary/
python code/make_sample.py --check     # verifies the re-coding sample and key
python code/agreement.py --key recoding_key/first_coder_key.csv --coder2 <completed form> --out agreement_results
```

Figures 1 and 2 are conceptual diagrams. Figure 3 is computed from `data/variants_v1_6.csv`. The figure scripts were written with AI assistance (see the article's AI declaration). Fonts: Arial (Liberation Sans is a metric-compatible substitute).

## Re-coding sample

The random set contains 24 variants drawn with `random.Random(20261014).sample` from the sorted method identifiers. The prespecified boundary variants are S066-M2, S053-M1, S088-M1 and S045-M1; S088-M1 is also in the random set. The 27 cases are shuffled with the same generator and carry neutral identifiers C01-C27. See `recoding_pack/README_recoding.md`.

## Audit status and known limits

This public version preserves the frozen 146-variant inventory and adds an audit. It is not a claim that every coding decision has been personally verified by the author. The 27-case AI review contains proposals awaiting author adjudication. No second human coder or inter-rater reliability result exists. `audit/` identifies the extent of the current checks. Versioned data filenames retain `v1_6` so existing scripts and the frozen sample continue to match.

Of 146 variants, 113 join directly to method-level evidence in release 1.2 and 25 join only to study-family evidence. The eight new S105 variants now have page-level entries in `data/evidence_s105_v1_7.csv`. An evidence join is a provenance check, not proof that every source claim was reread or independently validated. The S105 addition does not retroactively alter `data/release_1_2/evidence.csv`.

The author confirmed that the initial 101 PDFs were obtained through searches in Web of Science, ScienceDirect, SSRN and other sources, but the complete initial search logs were not retained. Separately retained public-search records document the AI-assisted discovery process. The 14 October index has 30 queries and 29 other operations. Its 21 negative access/retrieval entries are not zero-result literature searches. No query-level zero-hit history is reconstructed.

Supplementary Table S2 reports 23 families with at least one completed tree solve under each source's stopping criteria. It is not a uniform count of exact optimality proofs. S091's numerical gap threshold and full outcomes require its unavailable supplement. S044 and S091 source locators and conditions have been revised.

The author selected CC BY 4.0 for original data and documentation and MIT for code on 15 October 2026. See `RIGHTS_AND_RELEASE.md`. Third-party full texts, source-page images and raw web-page response dumps are excluded from this public package; historical originals are retained in the local audit archive. The archival DOI for this audit version is [10.5281/zenodo.23386416](https://doi.org/10.5281/zenodo.23386416).

The reproducibility audit passed manifest, selection-count, sample and synthetic agreement checks. Tables, count data and SVGs regenerated byte-for-byte in the tested environment. PNG RGB pixels matched, but PNG and PDF bytes differed. This is software validation, not independent human coding reliability.
