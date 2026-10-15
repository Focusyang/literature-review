# Supplementary methods

Version 1.2, 12 October 2026. All dates use Asia/Shanghai unless a source specifies otherwise. This supplement documents the completed author-review draft and supersedes the acquisition-stage supplement dated 11 October 2026. The original acquisition ledgers remain in the author archive and are not redistributed in this package.

## S1. Review design and scope

The review uses a bounded critical sample to compare acceleration mechanisms in column generation (CG), branch-and-price (B&P), and branch-price-and-cut (BPC). It examines where an intervention changes an algorithm, what conditions preserve its guarantees, and what part of a computation was evaluated. Standalone resource-constrained shortest-path methods are included as support when their interfaces inform pricing. The review covers traditional, heuristic, and learning-guided methods across routing, scheduling, cutting and packing, graph coloring, and other applications.

The design combines recorded public searches with selected citation tracing and full-text assessment. It does not claim exhaustive retrieval, search saturation, or representative estimates of method prevalence. The supplied collection defines the full-text assessment frame. Its composition reflects the search routes, the review's mechanism-based comparison, and full-text availability. This can underrepresent historical application literature and methods outside the retrieved sources. Counts describe this corpus and are not estimates of the whole field.

The initial protocol was saved on 11 October 2026. A retrospective amendment dated 12 October 2026 makes the critical-sample boundary explicit and records the disposition of additional Crossref leads. The protocol was not preregistered. The author-supplied product requirements document fixed the six intervention layers and guarantee and evidence labels. Its reference lists were discovery seeds rather than automatic inclusions. The unpublished author manuscript informed the motivation and internal consistency checks but was not counted as public evidence.

## S2. Search sources, dates, and query execution

Public searches and metadata checks were performed on 11–12 October 2026. The initial eligibility cutoff was 11 October 2026, with no lower publication-year limit for foundational mechanisms. Follow-up work on 12 October checked versions, journal rules, missing full text, and the remaining lead dispositions. Those operations are recorded separately and should not be interpreted as an exhaustive update search through a later cutoff.

Actual sources comprised public web search, Crossref REST, publisher and conference websites, arXiv, Optimization Online, SSRN, and author or institutional repositories. Direct API requests included arXiv and OpenReview operations where logged. Successful operations and access failures are recorded in the event log. Raw response dumps remain in the author archive and are not redistributed here. Neither Web of Science nor Scopus was searched. No hit total is attributed to either database.

Search terms combined algorithm terms with intervention terms. The root Crossref discovery batch submitted the following literal `query.bibliographic` strings, with `until-pub-date:2026-10-11` and `rows=20`.

1. `column generation machine learning`
2. `branch price learning pricing`
3. `column generation reinforcement learning selection`
4. `column generation stabilization dual prediction`
5. `resource constrained shortest path learning labeling`
6. `column generation partial pricing scheduling`
7. `column generation warmstarting column pool`
8. `branch price acceleration dominance state space relaxation`
9. `column generation cutting stock graph coloring learning`
10. `column generation crew scheduling learning`

Nine requests succeeded and one failed. These are relevance-ranked free-text requests, not Boolean searches restricted to title and abstract fields. Only the first 20 returned records from each successful request were exported. Further searches used exact titles, method terms, application terms, cited references, and known DOI or repository identifiers. Their actual strings and parameters are preserved in `search/search_log.csv`. The ten strings above describe one batch and must not be treated as the entire search strategy.

Each search-log row records an operation or batch, its source, date, timezone, literal query or URL, field or interface, restrictions, result limit, available hit total, exported count and unit, response-file path, executor, and notes. Public-web totals are generally unavailable and are marked UNKNOWN. DOI lookups and direct page opens verify known records rather than constitute independent discovery samples. A raw response file, a bibliographic hit, a PDF report, a publication record, and a study family are different counting units. They are not added together as a flow-diagram denominator.

Final PMLR and NeurIPS bibliographic checks are recorded in `search/search_log.csv`. Earlier visible returns from that final pass are preserved as selected observations, explicitly distinguished from complete raw responses. A same-day repeat open of the two official pages was saved as a complete response. The unsuccessful web-tool BibTeX request and successful direct HTTP retrieval are both logged. This repeat retrieval adds no study.

## S3. Study identification and selection

A CORE study directly changes a CG, B&P, or BPC algorithmic decision relevant to pricing or computational cost. SUPPORT studies provide a pricing method or a closely related algorithmic interface without directly establishing complete CG or B&P performance. BACKGROUND sources provide foundations, tutorials, related reviews, or review methodology. These collections serve different purposes in the synthesis and are not interchangeable denominators.

Generic neural optimization without a relevant CG or B&P interface, prediction of external problem inputs without such an interface, and uses of CG to construct or train a learning procedure were not treated as core acceleration studies. Title and accessible-abstract assessment preceded download selection. Full-text eligibility and mechanism coding were performed after receipt of the papers. Missing full text was treated as an access status, not as evidence of an unsuitable or inadequately reported method.

The author initially supplied 101 PDF reports representing 100 candidate study families. Three later-supplied main papers bring the current assessment frame to 104 reports and 103 families. One report is an erratum attached to its original review. Four broad adjacent surveys, S006, S009, S010, and S011, were excluded on eligibility grounds. Their abstracts, introductory scope, and targeted text-search hits were inspected. Their remaining contents were not represented as fully read and are not used for substantive manuscript claims. Reasons and inspected-page coverage are recorded in `data/screening.csv` and the paper-level records.

The retained collection comprises 99 study families: 79 CORE, 8 SUPPORT, and 12 BACKGROUND. Every supplied main paper retained for synthesis was read in full, including appendices embedded in that file. The coverage ledger records 2,133 pages for the retained main papers, plus the two-page erratum. An additional 19-page publisher e-companion to S027 was read through the public web PDF interface. It is a separate report and is not one of the 104 supplied files. External supplements were not assumed to be covered by reading an article's embedded appendices. Unaccessed supplements are identified at paper level.

### Separate disposition of the Crossref diagnostic export

The root discovery batch produced 180 hit rows with 170 unique DOIs. Initial dispositions were 52 title exclusions, 44 represented rows corresponding to 39 unique DOIs, and 84 pending rows corresponding to 79 unique DOIs. These numbers describe this export alone. They are not the numbers entering the author-supplied full-text frame.

The 79 pending leads were subsequently assessed at title and available-abstract level. One earlier conference report was linked to the already included S018 family. One paper was excluded because CG supplies an action space for reinforcement learning rather than being accelerated by learning. Three method leads were initially full-text gaps and were subsequently supplied and fully read in the version 1.1 update. The other 74 were retained as historical, application, or pricing-support leads not selected for this critical sample. They were not labeled ineligible or counted as full-text exclusions. All 79 dispositions are available in `search/additional_lead_dispositions.csv`.

Table SM1 identifies the three additional main papers.

**Table SM1. Main-paper additions after the diagnostic search.**

| Lead | Title | Identifier | Status in this review |
|---|---|---|---|
| CL002 | A Tolerance-Aware Pricing Certificate for Stabilized Dantzig–Wolfe Branch-and-Price in Unit Commitment | 10.3390/a19090731 | FULL_TEXT_READ; included with the version and evidence boundaries below |
| CL014 | Polyhedral Analysis and a Preprocessed Labeling Algorithm for the Elementary Shortest Path Problem with Resource Constraints | 10.2139/ssrn.6595201 | FULL_TEXT_READ; included with the version and evidence boundaries below |
| CL026 | A Learning-Based Framework for Constrained Shortest Path Problems | 10.1109/SMC53992.2023.10394613 | FULL_TEXT_READ; included with the version and evidence boundaries below |

Their earlier failed access attempts and available metadata are retained. CL002 is now S102, a published Algorithms article and CORE study; CL014 is S103, an SSRN preprint and SUPPORT study; CL026 is S104, an IEEE SMC proceedings paper and SUPPORT study. All 65 supplied pages were read. The S102 online File S1 and S103 external supplement remain unavailable. S103 is a traditional deterministic algorithm despite its LearningStrategy name. S104 evaluates nonnegative-cost path construction without CG integration. The 74 other leads remain unselected, not ineligible.

## S4. Deduplication, publication status, and versions

`record_id` identifies a publication or actual reading version. `study_id` identifies a research family. DOI and repository identifiers provided the first deduplication keys, followed by checks of titles, author lists, dates, and explicit version relationships. Closely related papers were not merged solely because they share authors, applications, or a method name. An earlier report was attached to a family only when the relationship was supported.

The preferred formal bibliography and the version actually read are recorded separately. When the supplied file is an accepted manuscript, author manuscript, advance article, or proof, evidence locators refer to that file. Final volume and page metadata do not replace its internal or PDF pagination. Differences in pagination do not prove a content change, but content equivalence is not assumed. The actual-version relation table records the relationship and its verification status.

First-public date, online-publication date, and issue year are distinct. A DOI suffix, copyright year, download stamp, submission date, or template header does not by itself establish publication date. Preprints retain their status unless a formal publication is verified. S084 illustrates this procedure: the acquisition lead was an arXiv preprint, whereas the supplied file was the published journal article. S082 is recorded as a 2022 workshop paper; its author-listed 2021 manuscript year does not establish an exact first-public date or main-conference publication. The bibliography audit records these decisions.

The S014 review and its erratum retain separate record identifiers within one family. Registry lookups therefore use `record_id` when selecting a specific publication. A dictionary keyed only by `study_id` could otherwise overwrite the base review with its erratum. Page counts, SHA-256 hashes, identity checks, reading status, and pages read are preserved in the report and reading-coverage ledgers. Source-paper files are not redistributed.

## S5. Reading, calibration, and AI-assisted adjudication

The work was performed through a lead AI agent and three specialized AI agents, with shared identifiers and coding definitions. Work was divided across traditional methods, learning-guided methods, related reviews, and bibliographic or journal checks. The lead agent consolidated classifications, reviewed evidence boundaries, and resolved inconsistent coding. This is AI-assisted extraction and adjudication. It is not independent human dual screening, and no inter-rater agreement statistic was calculated.

An 18-study pilot was completed before corpus-wide consolidation. It covered S016, S018, S019, S027, S050, S051, S052, S053, S055, S056, S061, S075, S079, S080, S083, S087, S089, and S098. Selection reflected completed readable papers and coverage of stabilization, search restriction, restoration, safe bounds, column selection, and integer completion. The final pilot differs from the prospective acquisition queue, as recorded in the change log. The lead agent inspected the pilot's mechanism, guarantee, empirical-scope, and boundary records. This does not imply that two reviewers independently reread every page.

Calibration required a single primary guarantee label, explicit separation of exact and heuristic variants, separate evidence rows for different experimental scopes, and preservation of source-specific denominators. It also distinguished restoration of CG from completeness of an outer integer search. The resulting decisions and examples are listed in the author archive; the operational definitions used here are reproduced in `methods/codebook.md`. Subsequent machine-readable checks verified identifiers, categorical values, counts, and the existence of evidence links. These checks establish internal consistency of the review package; they do not prove an algorithm correct or reproduce its experiments.

The supplied papers were inspected through page-numbered extracted text and, where extraction or table layout required it, rendered PDF pages. Each retained paper has a reading note and structured analyst record. Selected tables and contradictory numerical entries were checked against their rendered source. No claim is made that every PDF page underwent an independent second visual inspection. The author confirmed having contributed the research conception, original draft, literature collection, methodological design, evidence checking and revision. Final approval of this revised version remains pending. AI-assisted adjudication does not itself establish human dual screening or final author approval.

## S6. Intervention, guarantee, and empirical-scope coding

The primary unit of method comparison is a method variant within a study family. Common study information is inherited into a variant unless overridden. The `study` object contains the main method, normally M1. A `methods` array may contain only additional variants. Consolidation retains the main method if its identifier is absent from that array. Applying this convention produces 154 retained method rows, including 138 CORE/SUPPORT variants. There are 16 background method or framework rows. Method counts must not be reported as independent study counts.

### Intervention layers

Table SM2 defines the six intervention layers.

**Table SM2. Intervention-layer definitions.**

| Label | Decision location | Distinctions preserved |
|---|---|---|
| L1 | Tree search | Branching decisions and open-node selection are separate decisions |
| L2 | Restricted master problem and dual information | Initialization, warm starts, stabilization, predicted duals, and dual restrictions |
| L3 | Pricing scheduling | Order or budget of pricing-subproblem calls and choice of pricing solver |
| L4 | Pricing domain and state representation | Arc or state restriction, dominance, relaxation, bounds, and safe pruning |
| L5 | Search inside one pricing problem and new-column construction | Label processing, route or pattern construction, and internal search policy |
| L6 | Management of already generated columns | Selection, insertion, deletion, caching, and reuse |

A CORE/SUPPORT variant has one primary layer and may have secondary layers. The primary layer is chosen by the decision directly changed by that variant. Column construction is not coded as selection of existing columns. Ordering different pricing subproblems is not coded as label ordering within one subproblem. A family is counted once in study-level maps even when it has several variants or interfaces.

### Guarantee labels

Table SM3 defines the guarantee labels and their qualifications.

**Table SM3. Guarantee-label definitions.**

| Label | Operational meaning | Required qualification |
|---|---|---|
| G1 | Changes ordering, choices, or initialization while preserving the relevant complete procedure | State the unchanged completeness and termination conditions |
| G2 | Uses a restricted or heuristic phase followed by documented restoration or certification | Identify the restored domain, trigger, fallback, and termination conditions |
| G3 | Removes states, arcs, columns, or variables using a mathematical safety argument | Record valid-bound, dominance, incumbent, and feasibility assumptions |
| G4 | Uses a relaxation or stabilization that supplies a legitimate bound under stated conditions | Identify the mathematical target, domain relationship, and certification rule |
| G5 | The relevant implementation is heuristic or an overall guarantee is not established | Do not transfer a local component guarantee to the entire solver |
| GU | Available evidence is insufficient to assign a stronger guarantee interpretation | This is uncertainty, not a finding that the method is nonexact |

Each variant has one primary guarantee label. Secondary guarantees and conditions are retained in explanatory fields. Materially different implementations, such as a heuristic standalone procedure and an exact-CG warm start, receive separate method identifiers. Labels summarize a mechanism under its assumptions; they are not universal ratings of a paper or proof of an implemented solver's correctness.

Finding an improving column is distinct from certifying that no improving column exists. Failure of a heuristic does not provide the latter certificate. For minimization, an incomplete restricted-master objective is not automatically a lower bound on the full node relaxation. Predicted duals or learned scores do not automatically define valid bounds. The reading checks therefore seek the complete-domain fallback, recovery trigger, reduced-cost test, termination tolerance, incumbent-dependent conditions, and treatment of additional branching or cut rows. Phase-I or Farkas pricing is recorded when relevant and reported, with missing details retained as missing.

### Empirical scope

Table SM4 defines the empirical scopes used in the coding.

**Table SM4. Empirical-scope definitions.**

| Label | Evidence evaluated |
|---|---|
| E0 | Offline prediction or label quality |
| E1 | Independent pricing or fixed pricing states |
| E2 | CG iterations, root relaxation, or CG-based integer completion without a complete B&P tree |
| E3 | Non-root nodes or a component used within a tree |
| E4 | Complete B&P or BPC tree computation |

Empirical-scope codes may be multiple because one paper can report different experiments. Individual evidence rows retain their own scope. The codes are not a quality ranking. A complete-tree result on one instance is E4 with that one-instance limitation. A restricted-master integer solve, a diving heuristic, or complete route enumeration followed by an ordinary MIP is not automatically E4. Standalone constrained shortest-path results remain E1 even when the method could serve as a pricing component.

## S7. Evidence extraction and synthesis

The method record captures problem family, pricing structure, intervention, learning paradigm, model architecture, state inputs, action outputs, training source, teacher or reward, train/test split unit, offline cost, online cost, baseline, guarantee, recovery or certificate, empirical scope, and reported code or data access. Learning paradigm and model architecture are separate fields. For example, reinforcement learning does not identify a network architecture, and use of a neural network does not establish the training paradigm.

Training/test partitions are examined at the instance or instance-family level where possible. Random label-level splitting within related pricing trajectories is recorded because it can expose closely related states on both sides of a split. Cross-size, cross-topology, application, non-root, and newly added-cut tests are distinguished. Prediction accuracy alone is not treated as evidence of CG or complete-tree acceleration. Offline training and data-generation costs are kept separate from inference and solver time unless the source includes them in a clearly defined total.

Each evidence row carries an `evidence_id`, study and method identifiers, actual publication record, version read, evidence type, page/section/table locator, summary, and uncertainty. Computational rows retain instance families and counts, numbers of states when reported, baselines, hardware and software, time limits, tolerances, metric definitions, values as reported, denominators, timing scope, and termination status. The consolidated ledger contains 505 evidence rows. A row is an extracted item, not an independent experiment or independent study.

Source arithmetic, text/table conflicts, and unusual percentage denominators are preserved and qualified. A ratio of baseline time to accelerated time is not relabeled as a baseline-relative percentage reduction. Failed, timed-out, memory-limited, and unsolved cases remain relevant to interpretation. A mean over jointly solved instances is not generalized to all tested instances. Historical comparisons on different hardware are distinguished from controlled within-paper comparisons.

The synthesis groups studies by intervention and guarantee conditions, then compares the scope and adequacy of their evidence. It does not average speedups across heterogeneous hardware, baselines, objectives, stopping rules, or timing boundaries. No cross-paper meta-analysis, publication-bias statistic, new solver benchmark, or experimental reproduction was performed. Where several components change together, integrated solver gains are not attributed exclusively to learning or to one mechanism without an appropriate ablation.

Manuscript claims are linked to evidence identifiers in `data/claims.csv`, with counter-evidence, conditions, and inference flags where applicable. Comparative interpretations are marked as synthesis or inference rather than as a verbatim statement from one source. Related reviews support claims about review coverage; numerical or algorithmic claims about primary studies require the relevant primary text. The overlap assessment therefore does not establish priority for the first review of learned CG, column generation, or column selection.

## S8. Missing information and unresolved access

The package uses distinct missingness labels. NR means the relevant accessible full-text content was read but did not report the item. NOT_ACCESSED means the material was not obtained or read. UNKNOWN indicates unresolved information. UNVERIFIED indicates a judgment pending verification. NA means the field is not applicable. These values are not interchangeable and are not converted to zero, absence of cost, absence of failures, or proof of exactness.

Missing external appendices constrain claims that depend on their proof, detailed protocol, or numerical results. Statements supported by the available main paper can remain, with the missing material identified. The three former main-paper gaps have been closed by full reading; external proof and experiment supplements for two of them remain separately identified as NOT_ACCESSED. A formal bibliographic record does not establish that its complete text was read. An anonymous or undated supplied preprint can be matched to a verified public record while retaining uncertainty about the PDF's authorship display or exact revision date.

The complete 19-page Computers & Operations Research Guide for Authors supplied on 12 October 2026 was read and applied in version 1.2. The review targets the Surveys in Operations Research and Management Science section. The guide specifies single-anonymized review, an editable single-column Word source, an abstract of at most 250 words, one to seven keywords, and a separate highlights file. It does not specify a review word limit, mandatory invitation, body font, point size or line spacing. A repository deposit and dataset citation, or a truthful reason why sharing is not possible, are required by its Option C data policy. Local preparation does not constitute a public deposit.

## S9. Public-candidate reproducibility materials

The local package includes adjudicated data tables, publication and actual-version metadata, screening and reading-coverage records, search-event metadata, additional-lead decisions, citation-tracing records, a codebook and field dictionary, two BibTeX collections, and portable scripts. File purposes and transformations are described in README.md and provenance/source_snapshot.json. The package contains no source-paper PDF, extracted full text, source-page screenshot, raw search-response dump, private manuscript draft, or author contact information. Version 1.2 is prepared for public release at https://github.com/Focusyang/literature-review. No DOI, archival persistent identifier or reuse license is assigned in this package. The repository history records any completed upload.

The normalized data contain 99 retained families, 154 method variants, 505 evidence rows and 78 curated claims. Tables S1–S4 join those records without inventing a new reading or proof. For 29 method variants, no evidence row directly uses that method identifier. The guarantee table marks study-context linkage separately and retains the stated variant conditions.

The search log contains 186 discovery or access events, not 186 studies. The Crossref initial triage and 79 later lead dispositions remain separate to preserve their chronology. The 41 selected backward-reference matches add no study. The 76 reading-note flags do not assert completed tracing. Removed raw-response and internal-note paths are not required to execute the packaged code.

Run code/reproduce.py to validate the data, regenerate Tables S1–S4 and the manuscript's five curated comparison tables, and recompute all 30 Figure 3 cells with method identifiers. Its --figures option renders the three original diagrams in SVG. The script requires no source-paper PDF, web service, private workspace or installed skill. Data validation uses Python's standard library; figure rendering additionally uses Matplotlib. The checks establish bookkeeping and source-table consistency, not search exhaustiveness, mathematical correctness or reproduced solver performance. Search ranks can change over time. No paper's solver experiment is rerun by this package.

## S10. Author review and completion boundary

The current output is an author-review draft supported by saved full-text evidence records. It is not represented as a submission-ready final manuscript. The author must complete final review of the substantive interpretations and chosen claims, review the remaining coverage gaps, and finalize the repository and AI statements before submission. The author identity, address, no-funding and no-conflict declarations, and contribution roles were confirmed on 12 October 2026. AI assistance covered search support, metadata checks, full-text extraction and coding, synthesis, writing, and artifact preparation. The final disclosure must accurately state that contribution and the human review actually completed. No emails, editorial proposals or journal submissions were made. The author subsequently authorized release of the curated data and code to the designated GitHub repository; authorization is distinct from a verified upload.

## S11. Figures and submission-format preparation

The original conceptual diagrams and assessment-flow figure were rendered from definitions and recorded counts in `code/build_figures.py`. The evidence-scope matrix is calculated directly from `data/methods.csv`, with its 30 cells and method identifiers saved in `generated/figures/F3_matrix_data.csv`. Rendering uses Matplotlib 3.11.2, developed by the Matplotlib development team. OpenAI Codex, a GPT-6-based assistant whose exact model build was not exposed in the session, assisted figure organization and Python code drafting. No raster image-generation model was used. Programmatic alignment and rendered-page checks do not substitute for the author’s substantive verification. The author submission artwork includes vector PDFs and 600-dpi previews. This data/code package regenerates editable SVGs; it does not contain the author document-rendering environment.

The manuscript uses Harvard author–year citations, an alphabetical reference list, editable equations and tables, and separate highlights and captions. The complete supplied journal guide was checked against the prepared files. Earlier journal-access failures remain in the historical logs and do not describe the current guide-access status. These formatting checks add no study to the literature sample.
