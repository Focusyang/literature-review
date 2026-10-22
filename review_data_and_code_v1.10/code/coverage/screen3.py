#!/usr/bin/env python3
"""Recompute the coverage-check work counts and family recall from the finalized screening table.

The check runs offline from the released curated decisions; it needs no abstracts or live API access.
"""
from pathlib import Path
import collections, csv, json, re
ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'search/2026-10-16'
def rd(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))
rows = rd(BASE / 'cov_screening_v1_10.csv')
inv = rd(ROOT / 'data/coded_inventory_v1_10.csv')
assert len(rows) == 651 and len({r['record_id'] for r in rows}) == 651
groups = collections.defaultdict(list)
for r in rows:
    groups[r['work_id']].append(r)
assert len(groups) == 594
counts = collections.Counter()
for rs in groups.values():
    cats = {r['work_category'] for r in rs}
    assert len(cats) == 1
    counts[next(iter(cats))] += 1
expected = json.loads((BASE / 'cov_work_counts.json').read_text())
assert dict(counts) == expected
fams = {m.group(1) for r in rows if r['screening_category'] == 'IN_INVENTORY'
        and (m := re.match(r'(S\d{3})', r['basis']))}
learning = {r['study_id'] for r in inv if r['method_type'] == 'LEARNING_GUIDED'}
classical_only = {r['study_id'] for r in inv} - learning
recall = {'learning': (len(fams & learning), len(learning)),
          'classical_only': (len(fams & classical_only), len(classical_only))}
assert recall == {'learning': (42, 51), 'classical_only': (15, 37)}, recall
print('Coverage snapshot verified: 651 records, 594 works; recall 42/51 learning and 15/37 classical-only families.')
print('Outside frame and Crossref leads: 23 learning, 73 classical-method works; 17 acquisition-list works; 7 unclear learning roles.')
