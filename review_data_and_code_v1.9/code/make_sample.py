#!/usr/bin/env python3
"""Draw the re-coding sample of Appendix B.3 and write the coder pack and the first-coder key.

Sample: random.Random(20261014).sample(sorted(method_ids), 24) over the 113 variants of the coded
inventory in data/coded_inventory_v1_9.csv, plus the prespecified boundary variants S066-M2,
S053-M1, S088-M1 and S045-M1. None of the boundary variants is drawn in the random set, so the pack
contains 28 cases. The cases are then shuffled with the same generator and labelled C01-C28, so that
case identifiers reveal neither the method identifier nor set membership.

Usage (from the package root):
  python code/make_sample.py            # write recoding_pack/cases.csv, recoding_pack/coding_form_blank.csv
                                        # and recoding_key/first_coder_key.csv
  python code/make_sample.py --check    # verify that the released files are reproduced exactly
Only the Python standard library is required.
"""
import csv, io, random, sys

SEED = 20261014
N_RANDOM = 24
N_VARIANTS = 113
BOUNDARY = ['S066-M2', 'S053-M1', 'S088-M1', 'S045-M1']
VARIANTS = 'data/coded_inventory_v1_9.csv'
PACK = 'recoding_pack/cases.csv'
FORM = 'recoding_pack/coding_form_blank.csv'
KEY = 'recoding_key/first_coder_key.csv'
FORM_FIELDS = ['case_id', 'coder_id', 'date_coded', 'version_read', 'primary_layer', 'secondary_layers',
               'layer_reason_and_location', 'primary_mechanism', 'secondary_mechanisms',
               'mechanism_reason_and_location', 'scopes', 'scope_reason_and_location', 'confidence', 'notes',
               'minutes_spent']


def rows_to_csv(header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(header)
    w.writerows(rows)
    return buf.getvalue()


def build():
    with open(VARIANTS, encoding='utf-8-sig', newline='') as f:
        V = {r['method_id']: r for r in csv.DictReader(f)}
    ids = sorted(V)
    assert len(ids) == N_VARIANTS, len(ids)
    assert all(b in V for b in BOUNDARY)
    rng = random.Random(SEED)
    rand = rng.sample(ids, N_RANDOM)
    cases = list(rand) + [b for b in BOUNDARY if b not in rand]
    rng.shuffle(cases)
    pack, key = [], []
    for i, mid in enumerate(cases, 1):
        v = V[mid]
        cid = f'C{i:02d}'
        sets = '|'.join(s for s, inside in (('random', mid in rand), ('boundary', mid in BOUNDARY)) if inside)
        desc = v['variant_description']
        if desc.strip().lower() == 'main described algorithm':
            desc = 'The main algorithm proposed in the source'
        pack.append([cid, v['citation'], v['full_reference'], v['reading_version'], desc])
        key.append([cid, mid, v['study_id'], sets, v['primary_layer'], v['secondary_layers'],
                    v['primary_mechanism'], v['documentation_status'], v['scopes']])
    p = rows_to_csv(['case_id', 'source_citation', 'full_reference', 'version_to_read', 'variant_to_code'], pack)
    k = rows_to_csv(['case_id', 'method_id', 'study_id', 'set', 'primary_layer', 'secondary_layers',
                     'primary_mechanism', 'documentation_status', 'scopes'], key)
    form = rows_to_csv(FORM_FIELDS, [[f'C{i:02d}'] + [''] * (len(FORM_FIELDS) - 1) for i in range(1, len(cases) + 1)])
    return {PACK: p, FORM: form, KEY: k}, rand


def main():
    outputs, rand = build()
    if '--check' in sys.argv:
        ok = True
        for path, txt in outputs.items():
            with open(path, encoding='utf-8-sig', newline='') as f:
                same = f.read().replace('\r\n', '\n') == txt
            print(f'{path}: {"reproduced" if same else "DIFFERS"}')
            ok &= same
        return 0 if ok else 1
    for path, txt in outputs.items():
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(txt)
    print('random sample:', ', '.join(sorted(rand)))
    print('boundary variants also in the random sample:', ', '.join(b for b in BOUNDARY if b in rand) or 'none')
    print('cases written:', len(rand) + sum(b not in rand for b in BOUNDARY))
    return 0


if __name__ == '__main__':
    sys.exit(main())
