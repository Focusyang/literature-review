# Review revision 1.8

Materials for *Accelerating Column Generation and Branch-and-Price with Traditional and Learning-Guided Methods: A Critical Review*.

Author: Xinran Yang, School of Management and Engineering, Capital University of Economics and Business, China.

Revision date: 15 October 2026.

Version 1.8 archive: [10.5281/zenodo.23398854](https://doi.org/10.5281/zenodo.23398854).

## Contents and status

This version applies 43 confirmed decisions and 34 decisions derived from the author-approved coding rule. The directly intervened object determines the layer. Operations of the host solver, downstream effects and evidence from a different variant are not automatically inherited. The 46 unresolved decisions remain unresolved; 33 variant rows contain unresolved fields. Six author-confirmed statements concern the research process.

- `Yang_CG-BP_Critical_Review_v1.8_裁决修订稿.docx` is the revised manuscript snapshot, retaining all 146 variants and 123 reference entries. It corrects unsupported wording and mismatched citations without removing entire studies.
- `核对工作簿_v1.8_r3.xlsx` retains the historical source columns. Approved values and unresolved decisions are recorded in the columns marked ✎. Read those columns when determining the revised values.
- `修改清单_v1.8.xlsx` lists changed locations, original and revised values, decision identifiers and evidence. It includes decision coverage and revised counts.
- `修订依据/variants_v1_8_working.csv` is the effective 146-variant coding snapshot used by the revised manuscript and Figure 3. Unresolved fields retain provisional original values, with explicit status columns. They are not automatically converted to GU.
- `修订依据/Supplementary_Table_S1_v1_8_working.csv` retains 74 lead records representing 73 independent works after linking CL074/CL075. Unresolved classifications remain unresolved.
- `修订依据/Supplementary_Table_S2_v1_8_working.csv` contains the corrected complete-tree assessment records.
- `修订依据/figures/` contains the revised Figures 3 and A.1 in PNG, PDF and SVG formats.
- `修订依据/figure_sources/` and `reproduce_revision_figures.py` reproduce those two figures.

There are 239 variant-scope memberships, comprising 116 traditional and 123 learning-guided memberships. These counts include provisional original values in unresolved fields and are descriptive snapshots. No independent second human coding or inter-rater agreement result is claimed.

## Relationship to version 1.7

This is a revision supplement to the full data and code archive in [version 1.7](https://doi.org/10.5281/zenodo.23386416), also retained in the repository at `review_data_and_code_v1.7/`. Use that archive for historical search records, source-evidence locators, the original codebook, re-coding materials and unchanged Figures 1 and 2. For revised coding, counts and Supplementary Tables S1-S2, use the files in this revision supplement. Earlier snapshots have not been overwritten.

The manuscript and change list are preserved exactly as delivered before this upload. Their statements that revision materials were local and that the public archive was version 1.7 describe that pre-publication snapshot. Consult `PUBLICATION_STATUS.json` for the current upload status; an old DOI must not be presented as the DOI of this revision. The DOI for this revision supplement is [10.5281/zenodo.23398854](https://doi.org/10.5281/zenodo.23398854). The version 1.7 archive remains the historical baseline.

## Reproduce revised figures

With Python 3.10 or later, install `numpy`, `pandas`, `matplotlib` and `Pillow`, then run:

```sh
python reproduce_revision_figures.py
```

Outputs are written to `reproduced_figures/`, leaving the delivered figures intact. Arial is the design font; platform font availability can affect rendered appearance and binary checksums. No source-paper solver experiment is reproduced here.

## Rights and source access

Original review data and documentation follow the author's existing CC BY 4.0 release terms. Figure code uses MIT. The accompanying manuscript is an author manuscript, not a journal version of record. Third-party rights remain with their owners. Original source-paper PDFs, scanned source pages and downloaded full texts are excluded. Workbook local-source paths are evidence locators from the author's workspace, not bundled files or public download links. No source-paper permission or redistribution right is implied.

## 中文使用说明

工作簿的原始列是历史记录，新值与裁决在 ✎ 列。当前编码以 `variants_v1_8_working.csv` 和修订稿为准。46 条未确定裁决仍保留，不能视为已验证。本文献集未整篇删除研究。原文 PDF 不随公开包分发。版本 1.7 的完整数据包保持不变。
