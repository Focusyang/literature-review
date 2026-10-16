# Current version 1.10

[review_data_and_code_v1.10](review_data_and_code_v1.10/) is the data and code package that accompanies the article *Accelerating Column Generation and Branch-and-Price with Traditional and Learning-Guided Methods: A Critical Review*. It holds the same 85 files as review_data_and_code_v1.10.zip in the Zenodo record of version 1.10, DOI [10.5281/zenodo.23419224](https://doi.org/10.5281/zenodo.23419224). The concept DOI [10.5281/zenodo.23386415](https://doi.org/10.5281/zenodo.23386415) resolves to the latest version. The [package README](review_data_and_code_v1.10/README.md) describes its contents, counts and scripts.

## Earlier versions

All earlier files are preserved unchanged.

| Version | Location | Zenodo DOI |
|---|---|---|
| 1.9 | [review_data_and_code_v1.9](review_data_and_code_v1.9/) | [10.5281/zenodo.23410513](https://doi.org/10.5281/zenodo.23410513) |
| 1.8, revision supplement to version 1.7 | [review_revision_v1.8](review_revision_v1.8/) | [10.5281/zenodo.23398854](https://doi.org/10.5281/zenodo.23398854) |
| 1.7 | [review_data_and_code_v1.7](review_data_and_code_v1.7/) | [10.5281/zenodo.23386416](https://doi.org/10.5281/zenodo.23386416) |
| 1.2 | Supplementary_Data_and_Code.zip, documented below | None |

## Earlier release documentation

# Column generation and branch-and-price review data and code

Version 1.2, prepared 12 October 2026 for public release at https://github.com/Focusyang/literature-review.

**Creator:** Xinran Yang, School of Management and Engineering, Capital University of Economics and Business, China.

The author has authorized publication of these curated materials in this repository. Repository history records any actual upload. This package does not assert that an archival DOI has been assigned, and no data or software reuse license has been authorized.

## Download and inspect

Supplementary_Data_and_Code.zip contains **53 files** under review_data_and_code/. They include 99 study-family records, 154 method variants, 505 source-located evidence items and 78 curated claims. The archive also contains publication/version metadata, search and screening logs, the codebook and field dictionary, Tables S1–S4, five manuscript comparison tables, three editable SVG figures, two BibTeX collections, portable Python scripts and integrity checksums.

The review uses a bounded critical sample. It is not an exhaustive literature census. Pricing, column generation and complete branch-and-price trees are coded separately. Of the 154 method rows, 138 CORE/SUPPORT variants enter the guarantee-by-evidence-scope matrix. The remaining rows provide background context.

Downloaded papers, extracted third-party full text, raw response dumps, the private author draft, contact emails, host paths and historical QA images are excluded. Source-version descriptions and page locators allow an authorized reader to obtain and check the original papers separately. Their rights are not transferred by this package.

## Unzip and validate

Python 3.10 or later is required. From the directory containing the downloaded ZIP:

    python -m zipfile -e Supplementary_Data_and_Code.zip extracted
    cd extracted/review_data_and_code
    python code/reproduce.py

The standard-library command checks the saved records and regenerates Tables S1–S4, the five comparison tables and all 30 Figure 3 cells with their method IDs. It needs neither internet access nor the original paper PDFs. It returns a nonzero exit status if a validation check fails. These checks do not rerun any source-paper solver experiment or establish a mathematical guarantee.

For optional SVG rendering, install the package's pinned plotting dependency in an environment and run:

    python -m pip install -r requirements.txt
    python code/reproduce.py --figures

See the archive's README.md, methods/codebook.md and methods/derivations.md for complete instructions, counting units, missingness codes, file relationships and limitations. MANIFEST.sha256 lists the checksum of each distributed file except itself.

## Citation and rights

CITATION.cff and metadata.json identify the creator, title and prepared version. Cite the repository version or immutable commit actually accessed. No upload date, DOI, article identifier or reuse license is invented in these files. GitHub availability alone does not grant an open reuse license. Any later authorized license or archival identifier should be recorded explicitly.
