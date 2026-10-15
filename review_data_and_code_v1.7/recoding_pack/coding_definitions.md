# Coding definitions for the independent re-coding

These definitions are taken from the review codebook (methods/codebook.md) and the decision sequence of Appendix B.1 of the article. Case-specific boundary decisions of the first coder are deliberately not reproduced here.

## Unit

Code one **method variant** per case: the algorithmic implementation or guarantee regime named in `variant_to_code`. Exact and approximate versions of a method are different variants. Code what the accessed source documents, not what the method could achieve in principle.

## Step 1. Endpoint and layer

First identify the variant and its endpoint. The original LP, a weaker relaxation, a feasible integer solution and a complete proof are different targets. Next code the object directly changed, not every downstream consequence. Record one primary layer and any secondary layers.

| Code | Decision changed |
|---|---|
| L1 | Tree control: branching decisions or open-node selection |
| L2 | Restricted master and duals: initialization, warm starts, stabilization, predicted duals or restrictions |
| L3 | Pricing orchestration: scheduling or budgeting different subproblems or pricing routines |
| L4 | Pricing domain and state: arcs, states, relaxation, dominance, bounds or safe elimination |
| L5 | Work inside one pricing problem: label order, search decisions or construction of a new column |
| L6 | Already generated columns: admission, selection, insertion, pools, retention, deletion or reuse |

L3 chooses a block or oracle; L4 restricts its internal admissible domain; L5 reorders retained states or constructs a new column; L6 handles an existing or explicitly enumerated column. Construction of a new route is distinct from selection among existing routes. Scheduling pricing subproblems is distinct from ordering labels inside one subproblem. Use `NA` only if the case is not a within-CG/B&P intervention at all.

## Step 2. Documentation status and primary mechanism

First decide whether the accessed documentation establishes a mechanism. If it does not, code `GU`. If the variant is an offline prediction without an integrated guarantee target, code `GU-offline`. Otherwise code one primary mechanism G1-G5; secondary mechanisms may be listed.

| Code | Meaning | Evidence required |
|---|---|---|
| G1 | Order, choice or initialization change retaining the relevant complete procedure | Unchanged completeness, admissible decisions and termination conditions |
| G2 | Restricted or heuristic phase with documented restoration or certification | Restored domain, trigger, exact fallback and closure conditions |
| G3 | Mathematical safety for elimination, pruning or fixing | Valid bounds, dominance assumptions, resource behavior, feasibility and incumbent conditions |
| G4 | Relaxation or stabilization providing a legitimate bound under stated conditions | Target relaxation, domain relationship and valid certification |
| G5 | Relevant procedure is heuristic or its overall guarantee is not established | Explicit implementation boundary; a component's guarantee is not inherited by the solver |
| GU | Accessed evidence does not settle the mechanism | Record the unresolved point; uncertainty is not proof of non-exactness |
| GU-offline | Prediction-only variant without an integrated guarantee target | No deployed solver component to certify |

Decision rules: safe elimination supported by a current sufficient condition is G3. A justified relaxation or stabilization is G4 for the bound or convergence target it actually establishes. An unproved restriction or heuristic proposal that relies on complete restoration for the original target is G2. Complete order changes are G1. Explicitly incomplete search or stopping without that certification is G5. Missing accessed evidence leaves the mechanism unassigned rather than proving absence of a guarantee. Valid recovery must match the current dual solution, branch restrictions and active cuts. Deletion that permits regeneration is generally G2. Existing-column selection does not automatically establish G1 or complete enumeration. Finding an improving column does not certify that none remain; heuristic failure, predicted scores and an unfinished restricted-master objective do not provide a valid full-node bound.

## Step 3. Empirical scopes

Code every scope actually tested (several are allowed; write `NONE` if no computation of the variant is reported).

| Code | Evaluated computation |
|---|---|
| E0 | Offline prediction or label quality |
| E1 | Independent pricing, a standalone constrained path problem or fixed pricing states |
| E2 | CG iterations, root relaxation or CG-based integer completion without a complete B&P tree |
| E3 | Nonroot nodes or a tree component |
| E4 | Complete B&P or BPC computation |

A full implementation under a time limit may be E4 even when it fails to finish. A deliberately incomplete dive is E3. Solving an integer restricted master after root CG is E2 unless nonroot CG is evaluated. Complete route enumeration followed by an ordinary MIP does not establish E4. An exact branch-and-bound routine inside one pricing problem is E1, not E4. A separate exact solver used to obtain known optima for a heuristic benchmark does not upgrade that heuristic's scope.
