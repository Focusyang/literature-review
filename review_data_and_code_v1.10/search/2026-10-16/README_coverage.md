# Coverage check of 16 October 2026

This check used OpenAlex and arXiv (article Section 2.1), with AI-assisted screening (Section 2.2).
It is separate from Figure A.1 and did not add coded variants. The retained files are the query log, 651 screened
bibliographic records with work identifiers, and counts for 594 deduplicated works. Results were
assessed at title and available-abstract level. Original abstracts and raw responses are excluded.

Of the inventory families, the queries retrieved 42/51 families with learning-guided variants and
15/37 classical-only families. These are retrieval checks on the existing sample, not estimates of
literature-wide recall. Outside both the full-text frame and Crossref leads, 23 learning-guided
works and 73 classical-method works were found but not coded. Seventeen acquisition-list works
were not coded, and seven works have an unclear learning role.

`query_ids` links each record to the query and its result rank. `record_id` identifies an API record;
`work_id` groups records by DOI or normalized title. `screening_category` is the record decision and
`work_category` is the priority decision of its group. `basis` is the coder's short reason.
The table preserves the finalized decisions; it is not an automated classifier.

From the package root, `python code/coverage/screen3.py --check` recomputes the retained counts and
family recall offline from the finalized decisions.

`python code/coverage/run_cov.py --out-dir coverage_rerun` repeats the public queries using `oa.py`.
This optional command needs network access, may be subject to API limits and returns current,
not necessarily identical, results. It stores raw responses and reconstructed abstracts locally
for screening. Do not publish that raw directory as part of this licensed curated package.
No API key, access token or personal email address is needed or included.
