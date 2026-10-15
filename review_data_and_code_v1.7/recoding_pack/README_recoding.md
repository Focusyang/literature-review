# Independent re-coding pack (Appendix B.3)

This pack lets a second researcher re-code a sample of the frozen 146-variant inventory without seeing the first coder's labels.

## Contents

| File | Purpose |
|---|---|
| `cases.csv` | 27 cases with neutral identifiers C01-C27: 24 variants drawn at random and 3 additional prespecified boundary variants, in shuffled order. Each row gives the source citation, full reference, the version read by the first coder and the variant to code. |
| `coding_definitions.md` | Layer, mechanism and scope definitions and the decision sequence. |
| `coding_form_blank.csv`, `coding_form_blank.xlsx` | Blank answer form (the spreadsheet has drop-down lists). |
| `../recoding_key/first_coder_key.csv` | First-coder answers and set membership. **Do not open before all cases are coded.** |
| `../code/agreement.py` | Agreement statistics (standard library only). |
| `../code/make_sample.py` | Regenerates `cases.csv` and the key from `data/variants_v1_6.csv` (`--check` verifies them). |

## Procedure for the second coder

1. Do not consult the article, its tables, the variants file or the key until every case is coded and the form is saved.
2. For each case, obtain the source (DOI or repository link in `cases.csv`). Read the stated version where possible; otherwise record the version you read in `version_read`.
3. Code the primary layer, any secondary layers, the primary mechanism (G1-G5, GU or GU-offline), optional secondary mechanisms and every evaluated scope (E0-E4 or NONE). Separate multiple codes with `|`.
4. Give page-, section- or table-level reasons for each decision, a confidence rating (1 low, 2 medium, 3 high) and the minutes spent.
5. Save the completed form as CSV (UTF-8) and record the date. Keep this file unchanged after computing the statistics.

## Computing agreement

```
python code/agreement.py --key recoding_key/first_coder_key.csv --coder2 completed_form.csv --out agreement_results
```

The script reports, separately for the random set (24 cases, including S088-M1) and the boundary set (4 cases, including S088-M1): raw agreement and Cohen's kappa for the primary layer, primary mechanism and documentation status; per-scope binary agreement and kappa; exact scope-set agreement; mean Jaccard overlap; and 95% percentile bootstrap intervals that resample study families. Undefined kappa values are printed as `undefined`. Boundary cases inform the codebook and are not pooled with the random-sample estimates. Discuss disagreements only after the statistics have been saved, and document any codebook change separately from the first-pass results.
