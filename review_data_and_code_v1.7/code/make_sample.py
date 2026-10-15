#!/usr/bin/env python3
"""Draw the re-coding sample of Appendix B.3 and write the coder pack and the first-coder key.

Sample: random.Random(20261014).sample(sorted(method_ids), 24) over the 146 frozen variants in
data/variants_v1_6.csv, plus the prespecified boundary variants S066-M2, S053-M1, S088-M1 and S045-M1.
S088-M1 is also drawn in the random set, so the boundary set adds three cases. The 27 cases are then
shuffled with the same generator and labelled C01-C27, so that case identifiers reveal neither the
method identifier nor set membership.

Usage (from the package root):
  python code/make_sample.py            # write recoding_pack/cases.csv and recoding_key/first_coder_key.csv
  python code/make_sample.py --check    # verify that the released files are reproduced exactly
Only the Python standard library is required.
"""
import csv, io, random, sys

SEED = 20261014
N_RANDOM = 24
BOUNDARY = ['S066-M2', 'S053-M1', 'S088-M1', 'S045-M1']
VARIANTS = 'data/variants_v1_6.csv'
PACK = 'recoding_pack/cases.csv'
KEY = 'recoding_key/first_coder_key.csv'


def rows_to_csv(header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(header); w.writerows(rows)
    return buf.getvalue()


def build():
    with open(VARIANTS, encoding='utf-8-sig', newline='') as f:
        V = {r['method_id']: r for r in csv.DictReader(f)}
    ids = sorted(V)
    assert len(ids) == 146, len(ids)
    rng = random.Random(SEED)
    rand = rng.sample(ids, N_RANDOM)
    cases = list(rand) + [b for b in BOUNDARY if b not in rand]
    rng.shuffle(cases)
    pack, key = [], []
    for i, mid in enumerate(cases, 1):
        v = V[mid]; cid = f'C{i:02d}'
        sets = '|'.join(s for s, inside in (('random', mid in rand), ('boundary', mid in BOUNDARY)) if inside)
        desc = v['variant_description']
        if desc.strip().lower() == 'main described algorithm':
            desc = 'The main algorithm proposed in the source'
        pack.append([cid, v['citation'], v['full_reference'], v['reading_version'], desc])
        key.append([cid, mid, v['study_id'], sets, v['primary_layer'], v['secondary_layers'],
                    v['primary_mechanism'], v['scopes']])
    p = rows_to_csv(['case_id', 'source_citation', 'full_reference', 'version_to_read', 'variant_to_code'], pack)
    k = rows_to_csv(['case_id', 'method_id', 'study_id', 'set', 'primary_layer', 'secondary_layers',
                     'primary_mechanism', 'scopes'], key)
    return p, k, rand


def main():
    p, k, rand = build()
    if '--check' in sys.argv:
        ok = True
        for path, txt in ((PACK, p), (KEY, k)):
            with open(path, encoding='utf-8-sig', newline='') as f:
                same = f.read().replace('\r\n', '\n') == txt
            print(f'{path}: {"reproduced" if same else "DIFFERS"}'); ok &= same
        return 0 if ok else 1
    for path, txt in ((PACK, p), (KEY, k)):
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(txt)
    print('random sample:', ', '.join(sorted(rand)))
    print('boundary variants also in the random sample:', ', '.join(b for b in BOUNDARY if b in rand) or 'none')
    return 0


if __name__ == '__main__':
    sys.exit(main())
