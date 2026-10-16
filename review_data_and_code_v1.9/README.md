# Data and code for a critical review of column generation and branch-and-price acceleration

Version 1.9, 16 October 2026. Zenodo concept DOI [10.5281/zenodo.23386415](https://doi.org/10.5281/zenodo.23386415), which resolves to the latest version. Mirrored at https://github.com/Focusyang/literature-review.

Creator: Xinran Yang, School of Management and Engineering, Capital University of Economics and Business, China.

This version accompanies the article *Accelerating Column Generation and Branch-and-Price with Traditional and Learning-Guided Methods: A Critical Review*. It contains the coded inventory of Table A.1, the data behind Figures 3 and A.1, the Table 4 source locators, Supplementary Tables S1 and S2, the retained search and screening records, the codebook, the re-coding materials and the scripts for the figures and derived tables.

## Contents

| Path | Content |
|---|---|
| `data/coded_inventory_v1_9.csv` | Coded inventory of 113 method variants from 70 core or supporting study families (Table A.1, Figure 3) |
| `data/figure3_matrix_v1_9.csv` | Variant-scope memberships by variant type, primary mechanism and scope (181 in total) |
| `data/figure3_margins_v1_9.csv` | Variants per type and primary mechanism, including the variant without a measured scope |
| `data/selection_flow_v1_9.csv` | Counts shown in Figure A.1 with their derivation |
| `data/table4_source_locators_v1_9.csv` | Source version, pages, population, statistic and located values for each row of Table 4 |
| `data/evidence_s105.csv` | Page locators for the eight S105 variants and five supporting statements, with `README_evidence_s105.md` |
| `supplementary/` | Supplementary Table S1 (74 unselected lead records) and Table S2 (24 core families with a complete-tree evaluation), as CSV and XLSX |
| `search/` | Retained public search, title-triage and lead-disposition records, including the 14 October 2026 query index and access outcomes |
| `methods/` | Codebook (`codebook_v1_9.md`) and field dictionary (`field_dictionary_v1_9.csv`) |
| `recoding_pack/`, `recoding_key/` | Materials for an independent re-coding (Appendix B.3) and the first-coder key |
| `code/` | Scripts for the figures, derived tables, selection counts, re-coding sample and agreement statistics |
| `figures/` | Figures 1-3 and A.1 (PDF, PNG at 600 dpi, SVG) |
| `CHANGES_v1.9.md` | Changes from version 1.7 |

## Counts

The full-text frame contains 100 study families: 80 core, 8 supporting and 12 background. The coded inventory lists 113 variants, 58 traditional and 55 learning-guided, from 70 families (64 core and 6 supporting). A variant enters the inventory when its description, layers, guarantee decision and scopes are all settled under the codebook rules. GU counts as a settled guarantee decision. The 113 variants have 181 variant-scope memberships, and one variant has no measured scope. Twenty-four core families evaluate at least one variant in a complete B&P or BPC implementation (Supplementary Table S2). The Crossref follow-up left 74 lead records unselected at title and available-abstract level. They represent 73 independent works (Supplementary Table S1). These counts describe a bounded critical sample, not the prevalence of methods in the literature.

## Identifiers and earlier versions

Study, method and reading-record identifiers are stable across versions. Evidence record identifiers in Supplementary Table S2, such as E-T-S017-03, refer to the release 1.2 evidence table. The release 1.2 tables are retained unchanged in version 1.7 (`data/release_1_2/`), which is available through the concept DOI. Earlier versions also keep the working records from which this version was prepared.

## Reproducing the outputs

Run from this folder with Python 3.10 or later (`pip install -r requirements.txt`).

```
python code/figures/make_all.py      # Figures 1-3 and A.1 -> figures/
python code/build_tables.py          # Figure 3 matrix and margins, supplementary workbook, blank XLSX coding form
python code/selection_counts.py      # checks and writes the Figure A.1 counts
python code/make_sample.py --check   # verifies the re-coding cases, blank CSV form and key
python code/agreement.py --key recoding_key/first_coder_key.csv --coder2 <completed form> --out agreement_results
```

`build_tables.py --check` and `selection_counts.py --check` compare regenerated files with the released ones. `selection_counts.py --release12 <folder>` also recomputes the full-text frame counts from the release 1.2 tables. Figures 1 and 2 are conceptual diagrams. Figure 3 is computed from the coded inventory. The figure scripts were written with AI assistance, as stated in the article. Fonts: Arial (Liberation Sans is a metric-compatible substitute).

## Re-coding sample

The random set contains 24 variants drawn with `random.Random(20261014).sample` from the sorted method identifiers of the 113-variant inventory. The four prespecified boundary variants are S066-M2, S053-M1, S088-M1 and S045-M1. None of them occurs in the random set, so the pack contains 28 cases. The cases are shuffled with the same generator and carry neutral identifiers C01-C28. See `recoding_pack/README_recoding.md`.

## Coding process and limits

OpenAI GPT-series models accessed through Codex, and Notion AI, assisted discovery, screening, data extraction, initial coding and source checks. The author set the coding rules and approved the corrections applied to the inventory. No independent human double screening or double coding was performed, and no inter-rater reliability statistic is reported. The re-coding pack supports such a check.

The author obtained the initial 101 full-text reports through Web of Science, ScienceDirect, SSRN and other sources. Search strings and query-level results for this initial collection were not retained. The records in `search/` document the separately logged public discovery. The 14 October index has 30 queries and 29 other operations. Its 21 negative access or retrieval entries are not zero-result literature searches.

Supplementary Table S2 records 23 families with at least one completed tree solve under the stopping criteria of each source. It is not a uniform count of exact optimality proofs.

## Rights

Original data and documentation are licensed under CC BY 4.0 (`LICENSE-DATA.txt`), and code under MIT (`LICENSE-CODE.txt`). Third-party full texts, source-page images and raw web responses are not included. See `RIGHTS_AND_RELEASE.md` and `CITATION.cff`.
