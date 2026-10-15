# Codebook addendum, version 1.6

This addendum records the coding conventions used for release 1.6. The definitions of the six layers, the conditional guarantee labels G1-G5 and the empirical scopes E0-E4 in `codebook.md` (version 1.2) are unchanged.

1. **Unassigned variants.** `GU` marks a variant whose accessed documentation does not establish its mechanism. `GU-offline` marks a prediction-only variant without an integrated guarantee target (S064-M1). Both are reported separately from G1-G5 and are not a sixth mechanism. `documentation_status` in `data/variants_v1_6.csv` is derived from the primary mechanism: `MECHANISM_ASSIGNED` (G1-G5), `UNASSIGNED` (GU) or `UNASSIGNED_OFFLINE_ONLY` (GU-offline).
2. **Secondary layers** list only layers other than the primary layer. Five release 1.2 rows that repeated the primary layer were normalized (see `CHANGES_v1.2_to_v1.6.csv`).
3. **Recovered dual restrictions.** A variant that removes or relaxes unproved learned restrictions until the original LP is restored is G2 primary, with the relaxation retained as a secondary mechanism (S066-M2).
4. **Diving.** A deliberately incomplete dive is E3 (Appendix B.1); diving heuristics whose overall guarantee is not established are G5 (S105).
5. **Scopes and lists** in the 1.6 files use vertical bars; an empty `scopes` cell means that no computation of the variant is reported.
