# Coding dictionary

Version 1.2. The definitions preserve the review's original six intervention positions and separate a method's mathematical protection from the empirical computation that was measured. Codes are review interpretations tied to specific variants, versions, source locators and conditions. They are not universal quality scores or a certification of the supplied software.

## Units and identifiers

| Unit | Identifier | Meaning |
|---|---|---|
| Study family | study_id, Sxxx | Related reports of one retained research contribution; do not count its versions as independent studies |
| Method variant | method_id, Sxxx-Mn | A distinguishable algorithmic implementation or guarantee variant within a family |
| Publication or reading version | record_id, Rxxx or suffixed Rxxx-Vn | The formal bibliographic record or the actual version read |
| Report | report_id | A main paper, linked erratum or separately accessed companion |
| Extracted item | evidence_id | A page-located observation; not necessarily an experiment |
| Curated claim | claim_id | A synthesis proposition with supporting/counter evidence and conditions |
| Search event | search_id | A request or batch; not necessarily one returned paper |
| Additional lead | lead_id, CLxxx | A unique DOI lead from the separate Crossref diagnostic export |

The preferred bibliography and the actual source of an evidence locator may differ. actual_read_record_id joins records.csv. actual_version_relations.csv describes checked actual-reading relationships, whereas version_relations.csv preserves discovery-stage potential or reported relationships with their original verification states. A pending field in a formal bibliographic row does not override a separately coded actual-read record. The S014 review and its erratum share a family but retain separate records.

Study rows describe the main variant. Use methods.csv for variant-level analysis. A method with several empirical scopes appears in several Figure 3 columns. The 99 families, 154 method rows, 505 evidence rows and 78 claim rows are different units. None should be pooled as an experiment denominator.

## Collection

| Value | Meaning |
|---|---|
| CORE | Direct intervention in CG, B&P or BPC relevant to pricing or computational cost |
| SUPPORT | Closely related pricing or algorithmic interface without direct complete CG/B&P evidence |
| BACKGROUND | Foundations, reviews or methodological context |
| EXCLUDED | Eligibility decision in screening and coverage records, not a retained study row |

CORE and SUPPORT variants contribute to the primary mechanism/guarantee distribution. BACKGROUND rows can use NA or MULTIPLE. Unselected additional leads are not automatically excluded or ineligible.

## Six intervention layers

| Code | Decision changed |
|---|---|
| L1 | Tree control: branching decisions or open-node selection; preserve their distinction |
| L2 | Restricted master and duals: initialization, warm starts, stabilization, predicted duals or restrictions |
| L3 | Pricing orchestration: scheduling or budgeting different subproblems or pricing routines |
| L4 | Pricing domain and state: arcs, states, relaxation, dominance, bounds or safe elimination |
| L5 | Work inside one pricing problem: label order, search decisions or construction of a new column |
| L6 | Already generated columns: admission, selection, insertion, pools, retention, deletion or reuse |

main_layer is one code per CORE/SUPPORT variant. secondary_layers may contain several. Construction of a new route is distinct from selection among existing routes. Scheduling pricing subproblems is distinct from ordering labels inside one subproblem.

## Conditional guarantee labels

| Code | Meaning | Evidence required |
|---|---|---|
| G1 | Order, choice or initialization change retaining the relevant complete procedure | Unchanged completeness, admissible decisions and termination conditions |
| G2 | Restricted or heuristic phase with documented restoration or certification | Restored domain, trigger, exact fallback and closure conditions |
| G3 | Mathematical safety for elimination, pruning or fixing | Valid bounds, dominance assumptions, resource behavior, feasibility and incumbent conditions |
| G4 | Relaxation or stabilization providing a legitimate bound under stated conditions | Target relaxation, domain relationship and valid certification |
| G5 | Relevant procedure is heuristic or its overall guarantee is not established | Explicit implementation boundary; do not inherit a component's guarantee for the solver |
| GU | Accessed evidence does not settle a stronger guarantee interpretation | Retain the unresolved point; do not interpret uncertainty as proof of nonexactness |

The primary guarantee is single-valued. guarantee_secondary and explanation fields retain additional protection without mixing code and prose in the main label. Exact and approximate variants receive separate method rows. Valid recovery must match the current dual solution, branch restrictions and active cuts. Deletion that permits regeneration is generally G2, with progress conditions stated separately. Existing-column selection does not automatically establish G1 or complete enumeration.

Finding an improving column does not certify that none remain. Heuristic failure, predicted scores and an unfinished restricted-master objective do not generally provide a valid full-node bound. Theory must be tied to its formulation and assumptions. The dataset preserves safety conditions for negative cycles, resource bounds, relaxations and incomplete fallback rather than generalizing local statements to a full B&P tree.

## Empirical scopes

| Code | Evaluated computation |
|---|---|
| E0 | Offline prediction or label quality |
| E1 | Independent pricing, a standalone constrained path problem or fixed pricing states |
| E2 | CG iterations, root relaxation or CG-based integer completion without a complete B&P tree |
| E3 | Nonroot nodes or a tree component |
| E4 | Complete B&P or BPC computation |

Scopes can be multiple and are separated by a vertical bar. An E4 experiment with one instance remains a one-instance result. Integer solution of a restricted master or complete route enumeration followed by an ordinary MIP does not establish E4. The matrix describes what was evaluated and is not a ranking of experimental quality. It does not transfer E1 acceleration to CG or E4.

## Source evidence and joins

provenance_type distinguishes theory, algorithm descriptions, computational findings and other source material. Preserve the actual values rather than forcing all rows into empirical evidence. Each row retains source version, locator, summary and uncertainty. Computational rows also retain population, count, baseline, hardware/software, time limit, tolerance, metric, reported value, denominator, timing scope and termination status. Units appear with the source-reported values; no universal seconds or percentage unit is inferred for a free-text field.

Claims join supporting_evidence_ids and counter_evidence_ids to evidence.csv. The inference flag distinguishes review synthesis from a direct source statement. Claims still require their conditions. Source-version page numbers, not unverified VOR pagination, govern locators. A direct method-ID join and study-context join are marked separately in Table S3. Twenty-nine variants use the latter. Context is not a newly established proof for every variant.

## Missingness, formatting and historical records

| Value | Meaning |
|---|---|
| NR | The relevant accessible full-text content was read but did not report this item |
| NOT_ACCESSED | The material was not obtained or read |
| UNKNOWN | Information is unresolved |
| UNVERIFIED | A judgment is awaiting verification |
| NA | The field is not applicable |
| Empty cell | No consolidated value supplied for that optional field; do not replace it with zero, NR or NA |

UTF-8 CSV files use a header row and quoted cells when necessary. The export uses a UTF-8 BOM for spreadsheet compatibility. Identifier lists and normalized scope/secondary-layer codes use vertical bars. Free-text descriptions can use semicolons or natural prose and must not be split mechanically. JSON-valued cells such as source_locators_json are standard JSON strings embedded in CSV. Boolean fields use the source spellings True/False. Dates are ISO-style where available; partial years and unresolved dates remain as reported. Search dates may include their time-zone offset. The initial eligibility cutoff was 11 October 2026, with targeted follow-up on 12 October.

The initial Crossref title triage is retained for chronology and can show pending statuses that were later resolved. additional_lead_dispositions.csv holds the later decisions for its 79 unique DOI leads. Search-log hit_count is a source-reported interface count, not a screened-study total. Different exported units cannot be summed. Reader citation flags and selective known-title matches do not establish a complete citation search.

See field_dictionary.csv for file-specific columns, units and joins. See derivations.md for exact output operations and README.md for the command-line workflow and release status.
