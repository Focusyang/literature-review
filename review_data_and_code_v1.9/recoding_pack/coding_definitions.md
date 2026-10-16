# Coding definitions for the independent re-coding

These definitions are taken from the review codebook (`methods/codebook_v1_9.md`) and the decision sequence in Appendix B.1 of the article. Case-specific boundary decisions of the first coder are deliberately not reproduced here.

## Unit

Code one **method variant** per case: the algorithmic implementation or guarantee regime named in `variant_to_code`. Exact and approximate versions of a method are different variants. Code what the accessed source documents, not what the method could achieve in principle.

## Step 1. Endpoint and layer

First identify the variant and its endpoint. The original LP, a weaker relaxation, a feasible integer solution and a complete proof are different targets. Next code the object directly changed, not every downstream consequence. Record one primary layer and any secondary layers.

| Code | Decision changed |
|---|---|
| L1 | Tree control: branching decisions or open-node selection |
| L2 | Restricted master and duals: initialization, warm starts, stabilization, predicted duals or dual restrictions |
| L3 | Pricing orchestration: scheduling or budgeting different subproblems or pricing routines |
| L4 | Pricing domain and state: arcs, states, relaxation, dominance, bounds or safe elimination |
| L5 | Work inside one pricing problem: label order, search decisions or construction of a new column |
| L6 | Already generated columns: admission, selection, insertion, pools, retention, deletion or reuse |

L3 chooses a block or oracle. L4 restricts the admissible domain inside it. L5 reorders retained states or constructs a new column. L6 handles an existing or explicitly enumerated column. Construction of a new route is distinct from selection among existing routes. Scheduling pricing subproblems is distinct from ordering labels inside one subproblem. Use `NA` only if the case is not a within-CG/B&P intervention at all.

## Step 2. Documentation status and primary mechanism

First decide whether the accessed documentation establishes a mechanism. If it does not, code `GU`. If the variant is an offline prediction without an integrated guarantee target, code `GU-offline`. Otherwise code one primary mechanism from G1 to G5. Secondary mechanisms may be listed.

| Code | Meaning | Evidence required |
|---|---|---|
| G1 | An admissible order, choice or initialization change that retains the relevant complete procedure | Unchanged completeness, admissible decisions and termination conditions |
| G2 | Restriction or heuristic discovery followed by restoration of the required domain or another valid certifying procedure | Restored domain, recovery trigger, exact fallback and closure conditions |
| G3 | Elimination, pruning or fixing justified by a sufficient dominance, fixing or bound argument | Valid bounds, dominance assumptions, resource behavior, feasibility and incumbent conditions |
| G4 | Relaxation or stabilization with a justified bound or recovery of the original problem | Target relaxation, domain relationship and valid certification |
| G5 | The intended complete guarantee is explicitly absent, for example permanent restriction or learned stopping without recovery | Explicit implementation boundary. A component's guarantee is not inherited by the solver. |
| GU | Accessed evidence does not establish the mechanism | Record the reason. Uncertainty is not proof of non-exactness. |
| GU-offline | Prediction-only variant without an integrated guarantee target | No deployed solver component to certify |

Decision rules: safe elimination supported by a current sufficient condition is G3. A justified relaxation or stabilization is G4 for the bound or convergence target it actually establishes. An unproved restriction or heuristic proposal that relies on complete restoration for the original target is G2. Complete order changes are G1. Explicitly incomplete search or stopping without that certification is G5. Missing accessed evidence leaves the mechanism unassigned rather than proving absence of a guarantee. Valid recovery must match the current dual solution, branch restrictions and active cuts. Deletion that permits regeneration is generally G2. Existing-column selection does not automatically establish G1 or complete enumeration. Finding an improving column does not certify that none remain. Heuristic failure, predicted scores and an unfinished restricted-master objective do not provide a valid full-node bound.

## Step 3. Empirical scopes

Code every scope actually tested. Several scopes are allowed. Write `NONE` if no computation of the variant is reported.

| Code | Evaluated computation |
|---|---|
| E0 | Offline prediction or label quality |
| E1 | Standalone pricing, a constrained path problem or fixed pricing states |
| E2 | CG iterations, a root relaxation or CG-based integer completion without a complete B&P tree |
| E3 | Nonroot nodes, a tree component or incomplete integer search |
| E4 | Complete B&P or BPC computation |

A full implementation under a time limit may be E4 even when it fails to finish. A deliberately incomplete dive is E3. Solving an integer restricted master after root CG is E2 unless nonroot CG is evaluated. Complete route enumeration followed by an ordinary MIP does not establish E4. An exact branch-and-bound routine inside one pricing problem is E1, not E4. A separate exact solver used to obtain known optima for a heuristic benchmark does not upgrade that heuristic's scope.
