#!/usr/bin/env python3
"""Inter-coder agreement for the independent reliability check (Appendix B.3).

Compares a completed second-coder form with the first-coder key and reports, separately for the
random sample and the boundary set:
  * raw agreement and Cohen's kappa for the primary layer and the primary mechanism;
  * raw agreement and kappa for documentation status (mechanism assigned / GU / GU-offline);
  * per-scope binary agreement and kappa for E0-E4;
  * exact scope-set agreement and mean Jaccard overlap of scope sets;
  * mean Jaccard overlap of secondary layers (supplementary);
with percentile bootstrap intervals that resample study families (clusters).

Undefined kappa values (expected agreement equal to one) are reported as 'undefined', never as 1 or 0.
Unassigned (GU, GU-offline) and not-applicable (NA) answers are explicit categories.

Usage:
  python code/agreement.py --key recoding_key/first_coder_key.csv \
                           --coder2 path/to/completed_form.csv --out results/
Only the Python standard library is required.
"""
import argparse, csv, json, os, random, sys
from collections import Counter

LAYERS = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'NA']
MECHS = ['G1', 'G2', 'G3', 'G4', 'G5', 'GU', 'GU-offline', 'NA']
SCOPES = ['E0', 'E1', 'E2', 'E3', 'E4']
NONE_TOKENS = {'', 'NONE', 'NA', '-', '\u2014'}


def read_csv(path):
    with open(path, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def norm_code(x, allowed, field, case):
    x = (x or '').strip()
    if x.lower() == 'gu-offline':
        x = 'GU-offline'
    elif x.upper() in [a.upper() for a in allowed]:
        x = [a for a in allowed if a.upper() == x.upper()][0]
    if x not in allowed:
        raise ValueError(f'{case}: {field} = {x!r} is not one of {allowed}')
    return x


def norm_set(x, allowed, field, case):
    x = (x or '').strip()
    if x.upper() in NONE_TOKENS:
        return frozenset()
    parts = [p.strip().upper() for p in x.replace(',', '|').replace(';', '|').split('|') if p.strip()]
    for p in parts:
        if p not in allowed:
            raise ValueError(f'{case}: {field} contains {p!r}; allowed {allowed}')
    return frozenset(parts)


def doc_status(m):
    if m in ('GU', 'GU-offline', 'NA'):
        return m
    return 'ASSIGNED'


def kappa(a, b):
    """Cohen's unweighted kappa; returns None when undefined (expected agreement == 1)."""
    n = len(a)
    if n == 0:
        return None
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb.get(k, 0) for k in ca) / (n * n)
    if abs(1 - pe) < 1e-12:
        return None
    return (po - pe) / (1 - pe)


def raw(a, b):
    return sum(x == y for x, y in zip(a, b)) / len(a) if a else None


def jacc(s, t):
    if not s and not t:
        return 1.0
    return len(s & t) / len(s | t)


def stats(cases):
    """cases: list of dicts with k_* (key) and c_* (coder) values."""
    out = {'n_cases': len(cases), 'n_families': len({c['study_id'] for c in cases})}
    for fld in ('layer', 'mech', 'doc'):
        a = [c['k_' + fld] for c in cases]; b = [c['c_' + fld] for c in cases]
        out[f'{fld}_raw'] = raw(a, b); out[f'{fld}_kappa'] = kappa(a, b)
    for e in SCOPES:
        a = [e in c['k_scopes'] for c in cases]; b = [e in c['c_scopes'] for c in cases]
        out[f'{e}_raw'] = raw(a, b); out[f'{e}_kappa'] = kappa(a, b)
    out['scopes_exact'] = raw([c['k_scopes'] for c in cases], [c['c_scopes'] for c in cases])
    out['scopes_jaccard'] = sum(jacc(c['k_scopes'], c['c_scopes']) for c in cases) / len(cases) if cases else None
    out['seclayers_jaccard'] = sum(jacc(c['k_sec'], c['c_sec']) for c in cases) / len(cases) if cases else None
    return out


def bootstrap(cases, B, seed):
    fams = sorted({c['study_id'] for c in cases})
    by = {f: [c for c in cases if c['study_id'] == f] for f in fams}
    rng = random.Random(seed)
    reps = []
    for _ in range(B):
        draw = [rng.choice(fams) for _ in fams]
        sample = [c for f in draw for c in by[f]]
        reps.append(stats(sample))
    return reps


def pct(vals, q):
    vals = sorted(vals)
    if not vals:
        return None
    k = (len(vals) - 1) * q
    lo, hi = int(k), min(int(k) + 1, len(vals) - 1)
    return vals[lo] + (vals[hi] - vals[lo]) * (k - lo)


METRICS = [('layer_raw', 'Primary layer: raw agreement'), ('layer_kappa', "Primary layer: Cohen's kappa"),
           ('mech_raw', 'Primary mechanism: raw agreement'), ('mech_kappa', "Primary mechanism: Cohen's kappa"),
           ('doc_raw', 'Documentation status: raw agreement'), ('doc_kappa', "Documentation status: Cohen's kappa")] + \
          [(f'{e}_{s}', f'Scope {e}: {"raw agreement" if s == "raw" else "Cohen" + chr(39) + "s kappa"}')
           for e in SCOPES for s in ('raw', 'kappa')] + \
          [('scopes_exact', 'Scope set: exact agreement'), ('scopes_jaccard', 'Scope set: mean Jaccard overlap'),
           ('seclayers_jaccard', 'Secondary layers: mean Jaccard overlap (supplementary)')]


def build_cases(key_rows, coder_rows):
    coder = {r['case_id'].strip(): r for r in coder_rows if (r.get('case_id') or '').strip()}
    cases, missing = [], []
    for k in key_rows:
        cid = k['case_id'].strip()
        if cid not in coder:
            missing.append(cid); continue
        c = coder[cid]
        if not (c.get('primary_layer') or '').strip() or not (c.get('primary_mechanism') or '').strip():
            missing.append(cid); continue
        km = norm_code(k['primary_mechanism'], MECHS, 'key primary_mechanism', cid)
        cm = norm_code(c['primary_mechanism'], MECHS, 'primary_mechanism', cid)
        cases.append({
            'case_id': cid, 'study_id': k['study_id'], 'set': k['set'],
            'k_layer': norm_code(k['primary_layer'], LAYERS, 'key primary_layer', cid),
            'c_layer': norm_code(c['primary_layer'], LAYERS, 'primary_layer', cid),
            'k_mech': km, 'c_mech': cm, 'k_doc': doc_status(km), 'c_doc': doc_status(cm),
            'k_scopes': norm_set(k['scopes'], SCOPES, 'key scopes', cid),
            'c_scopes': norm_set(c.get('scopes'), SCOPES, 'scopes', cid),
            'k_sec': norm_set(k.get('secondary_layers'), LAYERS[:-1], 'key secondary_layers', cid),
            'c_sec': norm_set(c.get('secondary_layers'), LAYERS[:-1], 'secondary_layers', cid),
        })
    return cases, missing


def fmt(v):
    return 'undefined' if v is None else f'{v:.3f}'


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--key', required=True); ap.add_argument('--coder2', required=True)
    ap.add_argument('--out', default='agreement_results'); ap.add_argument('--boot', type=int, default=2000)
    ap.add_argument('--seed', type=int, default=20261014)
    a = ap.parse_args(argv)
    cases, missing = build_cases(read_csv(a.key), read_csv(a.coder2))
    os.makedirs(a.out, exist_ok=True)
    results, lines = [], []
    if missing:
        lines.append(f'WARNING: {len(missing)} case(s) not coded and excluded: {", ".join(missing)}')
    for setname in ('random', 'boundary'):
        sub = [c for c in cases if setname in c['set'].split('|')]
        if not sub:
            continue
        point = stats(sub)
        reps = bootstrap(sub, a.boot, a.seed)
        lines.append(f'\n== {setname} set: {point["n_cases"]} cases from {point["n_families"]} study families '
                     f'(bootstrap B = {a.boot}, family-clustered, seed {a.seed})')
        for m, label in METRICS:
            vals = [r[m] for r in reps if r[m] is not None]
            lo, hi = (pct(vals, 0.025), pct(vals, 0.975)) if point[m] is not None and vals else (None, None)
            results.append({'set': setname, 'metric': m, 'label': label, 'estimate': point[m],
                            'ci95_low': lo, 'ci95_high': hi, 'valid_bootstrap_replicates': len(vals),
                            'n_cases': point['n_cases'], 'n_families': point['n_families']})
            ci = f'[{fmt(lo)}, {fmt(hi)}]' if lo is not None else ''
            lines.append(f'{label:<58} {fmt(point[m]):>9} {ci}')
        if setname == 'boundary':
            lines.append('Boundary cases inform the codebook and are not pooled with the random-sample estimates.')
    with open(os.path.join(a.out, 'agreement_results.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()) if results else ['set'])
        w.writeheader(); [w.writerow(r) for r in results]
    with open(os.path.join(a.out, 'case_level_comparison.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['case_id', 'study_id', 'set', 'key_layer', 'coder_layer', 'key_mechanism', 'coder_mechanism',
                    'key_scopes', 'coder_scopes', 'layer_agree', 'mechanism_agree', 'scopes_exact'])
        for c in cases:
            w.writerow([c['case_id'], c['study_id'], c['set'], c['k_layer'], c['c_layer'], c['k_mech'], c['c_mech'],
                        '|'.join(sorted(c['k_scopes'])), '|'.join(sorted(c['c_scopes'])),
                        c['k_layer'] == c['c_layer'], c['k_mech'] == c['c_mech'], c['k_scopes'] == c['c_scopes']])
    rep = '\n'.join(lines)
    with open(os.path.join(a.out, 'agreement_report.txt'), 'w', encoding='utf-8') as f:
        f.write(rep + '\n')
    print(rep)
    return 0


if __name__ == '__main__':
    sys.exit(main())
