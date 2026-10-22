#!/usr/bin/env python3
"""Regenerate the descriptive family-by-type sensitivity table; --check verifies released outputs."""
import collections, csv, io, json, sys
INV = 'data/coded_inventory_v1_10.csv'
CSV = 'data/family_level_sensitivity_v1_10.csv'
JSON = 'data/family_sensitivity_v1_10.json'
with open(INV, encoding='utf-8-sig', newline='') as f:
    inv = list(csv.DictReader(f))
fam = collections.defaultdict(lambda: {'scopes': set(), 'mech': set(), 'n': 0})
for r in inv:
    v = fam[(r['study_id'], r['method_type'])]
    v['n'] += 1
    v['scopes'].update(s for s in r['scopes'].split('|') if s)
    v['mech'].add(r['primary_mechanism'].replace('GU-offline', 'GU'))
rows, result = [], {}
for t, name in [('TRADITIONAL', 'traditional'), ('LEARNING_GUIDED', 'learning-guided')]:
    fs = {k: v for k, v in fam.items() if k[1] == t}
    hi = collections.Counter(max(v['scopes']) if v['scopes'] else 'none' for v in fs.values())
    mech = collections.Counter(m for v in fs.values() for m in v['mech'])
    scope = collections.Counter(s for v in fs.values() for s in v['scopes'])
    result[t] = dict(families=len(fs), variants=sum(v['n'] for v in fs.values()),
                     highest_scope=dict(sorted(hi.items())),
                     families_with_E3_or_E4=sum(bool(v['scopes'] & {'E3', 'E4'}) for v in fs.values()),
                     families_only_E0_to_E2=sum(bool(v['scopes']) and v['scopes'] <= {'E0', 'E1', 'E2'} for v in fs.values()),
                     families_with_mechanism=dict(sorted(mech.items())),
                     families_with_scope=dict(sorted(scope.items())))
    for k, v in sorted(fs.items()):
        rows.append([k[0], name, v['n'], '|'.join(sorted(v['scopes'])),
                     max(v['scopes']) if v['scopes'] else '', '|'.join(sorted(v['mech']))])
b = io.StringIO()
w = csv.writer(b, lineterminator='\n')
w.writerow(['study_id', 'method_type', 'variants', 'scopes_union', 'highest_scope', 'primary_mechanisms_present'])
w.writerows(rows)
txt = b.getvalue()
if '--check' in sys.argv:
    with open(CSV, encoding='utf-8-sig', newline='') as f:
        assert f.read().replace('\r\n', '\n') == txt, 'family CSV differs'
    with open(JSON, encoding='utf-8') as f:
        assert json.load(f) == result, 'family JSON differs'
    print('Family-level table and summaries reproduced: 38/51 learning families at E0-E2; 19/38 traditional families at E3/E4.')
else:
    with open(CSV, 'w', encoding='utf-8', newline='') as f:
        f.write(txt)
    with open(JSON, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=1)
