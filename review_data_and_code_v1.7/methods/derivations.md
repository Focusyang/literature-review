# Derived outputs and reproducibility boundary

## Study and method units

studies.csv contains one row for each retained family. Its principal method fields summarize the selected main variant. methods.csv contains every coded variant. Only the 138 rows whose collection is CORE or SUPPORT contribute to the guarantee-by-scope matrix. Background frameworks and reviews remain available for context but are excluded from that distribution.

## Tables S1–S4

S1 joins each retained family to its preferred record, actual reading coverage, method IDs and evidence IDs. S2 adds preferred titles, actual versions and evidence linkage to every method variant. S3 selects guarantee-relevant fields and marks DIRECT_METHOD_EVIDENCE or STUDY_CONTEXT_WITH_VARIANT_CONDITIONS_ONLY. S4 enriches every evidence item with its method's variant, layer, guarantee and recovery information. Conditions in source rows are preserved. The normalized evidence table is the authoritative location of full evidence summaries, so repeated JSON copies of all study evidence are not embedded in S3.

Every data/studies.csv, methods.csv and evidence.csv field is retained in its corresponding S1, S2 or S4 output. Local source-paper file paths are omitted from the staged input tables. SHA-256 identifiers and actual-version descriptions remain available. The output row counts are 99, 154, 154 and 505 respectively.

## Figures

Figure 1 is an original conceptual diagram defined in code/build_figures.py. It encodes the L1–L6 interface definitions and does not measure an empirical effect. Figure 2 uses the supplied-frame counts in data/counts.json and the separately described Crossref diagnostic export. The two frames are not summed as one screening flow. Figure 3 iterates over CORE/SUPPORT methods, reads the single primary guarantee and each vertical-bar-separated E0–E4 scope, increments the corresponding cell once and appends the method ID. A method with several scopes contributes to several columns. The 30 cells are not additive and do not rank evidence quality.

The Figure 3 result is checked against data/expected_F3_matrix_data.csv. That file is a reference output from the manuscript's source code, not another dataset or experimental observation. SVG rendering is optional. The portable adaptation removes the author's host-only visual-audit dependency and private runtime paths; it retains the figure geometry, labels and counting logic.

## Five manuscript comparison tables

code/build_synthesis_tables.py stores and exports the five hand-curated comparisons as CSV and Markdown. Citation keys Sxxx correspond to the bibliography and study IDs. It does not infer new effects, calculate pooled performance estimates or recompute original solver experiments. Follow the cited evidence and version-specific locators to assess a numerical statement. Hardware, baselines, units, timeouts and aggregation boundaries remain source-specific.

## Validation and limitations

The standard-library checks confirm identifiers, joins, snapshot counts, scope labels, retained-main-paper reading coverage, lead dispositions and the Figure 3 matrix. Successful validation does not establish completeness of literature retrieval, correct human adjudication, a mathematical proof, experimental replication or a public repository deposit. It cannot inspect original PDFs because they are not redistributed. No complete backward or forward citation search is inferred from the selected citation records.
