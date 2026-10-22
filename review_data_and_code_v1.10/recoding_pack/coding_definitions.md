# Codebook, version 1.10

This codebook defines the units and codes used in the version 1.10 files. A code is a review interpretation of a named variant. It is tied to the source version read and to the conditions stated in that source. Codes are not quality scores, and they do not certify the software described in a source. Appendix B of the article gives the same decision sequence with worked boundary cases.

## Units and identifiers

| Unit | Identifier | Meaning |
|---|---|---|
| Study family | `study_id`, Sxxx | Related reports of one research contribution. Versions of a report are not counted as separate studies. |
| Method variant | `method_id`, Sxxx-Mn | A separately evaluated algorithmic object or guarantee regime within a family, after the R1 merging rule below. |
| Reading record | Rxxx or Rxxx-Vn | The version actually read for a family. |
| Lead record | CLxxx | A DOI lead from the logged Crossref follow-up (Supplementary Table S1). |
| Evidence record | for example E-T-S017-03 | A page-located observation in the release 1.2 evidence table. |
| Re-coding case | C01-C27 | A neutral case identifier in the re-coding pack. |

Identifiers are stable across versions, so the numbering of variants within a family need not be consecutive.

## Collection

| Value | Meaning |
|---|---|
| CORE | Direct intervention in CG, B&P or BPC that is relevant to pricing or computational cost |
| SUPPORT | Closely related pricing or algorithmic interface without direct complete CG or B&P evidence |
| BACKGROUND | Foundations, reviews or methodological context. Background families are not coded at variant level. |

## Coded inventory

A variant of a core or supporting family enters the coded inventory when its description, layers, guarantee decision and scopes are all settled under the rules below. GU counts as a settled guarantee decision. The inventory of version 1.10 contains 130 variants from all 88 core or supporting families (80 core and 8 supporting). Supplementary Table S2, for example, reports complete-tree completion for all 24 core families with a complete-tree evaluation.

## R1 granularity rule

A variant receives its own row only when the source treats an algorithm, configuration or guarantee mechanism as a separate object with a separate result. Rows within one family with identical primary and secondary layers, primary mechanism, scopes and method type are merged, and their configurations are listed in the description. `merged_from` retains the earlier identifiers. Identical codes are compared as sets where order has no meaning.

## Step 1. Endpoint and intervention layer

First identify the variant and its endpoint. The original LP, a weaker relaxation, a feasible integer solution and a complete proof are different targets. Next code the object that the variant directly changes, not every downstream consequence.

| Code | Decision changed |
|---|---|
| L1 | Tree control: branching decisions or open-node selection |
| L2 | Restricted master and duals: initialization, warm starts, stabilization, predicted duals or dual restrictions |
| L3 | Pricing orchestration: scheduling or budgeting different subproblems or pricing routines |
| L4 | Pricing domain and state: arcs, states, relaxation, dominance, bounds or safe elimination |
| L5 | Work inside one pricing problem: label order, search decisions or construction of a new column |
| L6 | Already generated columns: admission, selection, insertion, pools, retention, deletion or reuse |

L3 chooses a block or oracle. L4 restricts the admissible domain inside it. L5 reorders retained states or constructs a new column. L6 handles an existing or explicitly enumerated column. Construction of a new column is distinct from selection among existing columns. Scheduling pricing subproblems is distinct from ordering labels inside one subproblem.

`primary_layer` holds one code. `secondary_layers` lists the other layers that the variant directly changes. Shared host-solver operations and downstream consequences are not coded as additional layers unless the variant directly changes them.

## Step 2. Documentation status and guarantee mechanism

First decide whether the accessed documentation establishes a mechanism. If it does not, code GU. If the variant is an offline prediction without an integrated guarantee target, code GU-offline. Otherwise code one primary mechanism from G1 to G5.

| Code | Meaning | Evidence required |
|---|---|---|
| G1 | An admissible order, choice or initialization change that retains the relevant complete procedure | Unchanged completeness, admissible decisions and termination conditions |
| G2 | Restriction or heuristic discovery followed by restoration of the required domain or another valid certifying procedure | Restored domain, recovery trigger, exact fallback and closure conditions |
| G3 | Elimination, pruning or fixing justified by a sufficient dominance, fixing or bound argument | Valid bounds, dominance assumptions, resource behavior, feasibility and incumbent conditions |
| G4 | Relaxation or stabilization with a justified bound or recovery of the original problem | Target relaxation, domain relationship and valid certification |
| G5 | The intended complete guarantee is explicitly absent, for example permanent restriction or learned stopping without recovery | Explicit implementation boundary. A component's guarantee is not inherited by the solver. |
| GU | Accessed evidence does not establish the mechanism | Record the reason. Uncertainty is not proof of non-exactness. |
| GU-offline | Prediction-only variant without an integrated guarantee target | No deployed solver component to certify |

Decision rules:

* Safe elimination supported by a current sufficient condition is G3.
* A justified relaxation or stabilization is G4 for the bound or convergence target it actually establishes. A claim of return to the original problem needs that return established in the accessed report; otherwise the variant is GU.
* An unproved restriction or heuristic proposal that relies on complete restoration for the original target is G2.
* Complete order changes are G1.
* Explicitly incomplete search, or stopping without that certification, is G5.
* Missing accessed evidence leaves the mechanism unassigned rather than proving the absence of a guarantee.
* Valid recovery must match the current dual solution, branch restrictions and active cuts.
* Deletion that permits regeneration is generally G2. Its progress conditions are recorded separately.
* Selection among existing columns does not by itself establish G1 or complete enumeration.
* Finding an improving column does not certify that none remain. Heuristic failure, predicted scores and an unfinished restricted-master objective do not provide a valid full-node bound.

The primary mechanism holds one code. The rules permit secondary mechanisms and do not claim that the mechanisms are mathematically disjoint.

`documentation_status` is derived from the primary mechanism.

| Value | Primary mechanism |
|---|---|
| MECHANISM_ASSIGNED | G1-G5 |
| UNASSIGNED | GU |
| UNASSIGNED_OFFLINE_ONLY | GU-offline |

GU and GU-offline record documentation status. They are neither a sixth mechanism nor a judgment that an algorithm is incorrect. Figure 3 shows both in the GU row, separately from G1-G5.

## Step 3. Empirical scope

Code every scope actually tested. Several scopes are allowed. E0 requires a separately reported offline prediction or label-quality metric, not a training loss alone. E3 requires (a) a separately reported nonroot result, (b) a separately measured tree component such as branching-test time or an in-tree heuristic, or (c) deliberately incomplete integer search such as a dive. Aggregate complete-tree totals do not add E3.

| Code | Evaluated computation |
|---|---|
| E0 | Offline prediction or label quality |
| E1 | Standalone pricing, a constrained path problem or fixed pricing states |
| E2 | CG iterations, a root relaxation or CG-based integer completion without a complete B&P tree |
| E3 | Nonroot nodes, a tree component or incomplete integer search |
| E4 | Complete B&P or BPC computation |

A full implementation under a time limit may be E4 even when it fails to finish. E4 identifies the evaluated procedure, not a proof on every instance. A timeout is not a completed solve. A deliberately incomplete dive is E3. Solving an integer restricted master after root CG is E2 unless nonroot CG is evaluated. Complete route enumeration followed by an ordinary MIP does not establish E4. An exact branch-and-bound routine inside one pricing problem is E1, not E4. A separate exact solver used to obtain known optima for a heuristic benchmark does not upgrade the scope of that heuristic. An empty `scopes` cell means that no computation of the variant is reported.

## Upper bounds in Supplementary Table S2

An upper bound counts as supplied only when given before or outside the timed run. An initial feasible solution or restricted-IP heuristic inside the timed run does not count as supplied. NR means that the accessed report does not state the supplied-bound status.

## Formats and missing values

CSV files are UTF-8 with a header row. Lists of codes and identifiers in the inventory, the Figure 3 files and the re-coding files use a vertical bar (`|`). Supplementary Table S2 separates evidence record identifiers with semicolons. Free-text descriptions can contain semicolons and must not be split mechanically.

| Value | Meaning |
|---|---|
| NR | The accessible full text was read but does not report the item |
| NOT_ACCESSED | The material was not obtained or read |
| NA | The field does not apply |
| Empty cell | No value applies or none was recorded for an optional field. An empty cell is not zero. |

The historical records in `search/` keep their original values. In them, UNKNOWN marks a value that the interface did not report or that was not recorded, such as a hit count.

Field definitions are in `field_dictionary_v1_10.csv`.
