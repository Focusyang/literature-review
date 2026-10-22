#!/usr/bin/env python3
"""Recompute the selection counts shown in Figure A.1 and write data/selection_flow_v1_10.csv.

Left stream: logged Crossref discovery export (search/search_log.csv, search/crossref_title_triage.csv and
search/additional_lead_dispositions.csv). Lead CL075 is a second DOI of the work recorded as CL074.
Right stream: author-assembled full-text frame. These counts come from the release 1.2 screening and
reading records, which are included in this package (data/release_1_2/). Pass
--release12 DIR to recompute and check them from that folder. The default is the bundled data/release_1_2/ folder.
Included tier: study-family totals and the coded inventory (data/coded_inventory_v1_10.csv).

Usage (from the package root):
  python code/selection_counts.py [--release12 path/to/release_1_2] [--check]
Only the Python standard library is required.
"""
import argparse, csv, io, os, sys
from collections import Counter

OUT = 'data/selection_flow_v1_10.csv'
ALIAS = {'10.1109/ichis.2007.4344036': '10.1109/his.2007.58'}  # CL075 -> CL074, same work
TARGETED_ADDITION = 'S105'  # core family added by the targeted search of 14 October 2026
FRAME_RECORDED = {  # release 1.2 screening.csv and read_reports.csv
    'initial_reports': 101, 'reports_assessed': 104, 'families_assessed': 103, 'surveys_excluded': 4,
    'core': 79, 'support': 8, 'background': 12,
}


def rd(p):
    with open(p, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


FRAME_SOURCE = 'release 1.2 screening.csv and read_reports.csv (data/release_1_2/)'


def frame_counts(rel, n_later):
    if rel is None:
        return dict(FRAME_RECORDED), FRAME_SOURCE
    scr = rd(os.path.join(rel, 'screening.csv'))
    rep = rd(os.path.join(rel, 'read_reports.csv'))
    dec = Counter(r['decision'] for r in scr)
    supplied = [r for r in rep if r['report_id'].startswith('FT-') and '-SUP' not in r['report_id']]
    got = {'initial_reports': len(supplied) - n_later, 'reports_assessed': len(supplied),
           'families_assessed': len(scr), 'surveys_excluded': dec['EXCLUDED'], 'core': dec['CORE'],
           'support': dec['SUPPORT'], 'background': dec['BACKGROUND']}
    assert got == FRAME_RECORDED, got
    print('Frame counts recomputed from', rel)
    return got, FRAME_SOURCE


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--release12', default='data/release_1_2')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()

    log = [r for r in rd('search/search_log.csv') if r['search_id'].startswith('CRQ')]
    tri = rd('search/crossref_title_triage.csv')
    leads = rd('search/additional_lead_dispositions.csv')
    inv = rd('data/coded_inventory_v1_10.csv')

    by_doi = {}
    for r in tri:
        by_doi.setdefault(r['doi'].lower(), set()).add(r['screen_status'])
    assert all(len(s) == 1 for s in by_doi.values())
    works = {ALIAS.get(d, d) for d in by_doi}
    doi_status = Counter(next(iter(s)) for s in by_doi.values())
    lead_status = Counter(r['screen_status'] for r in leads)
    lead_works = {ALIAS.get(r['doi'].lower(), r['doi'].lower()) for r in leads}
    unsel = [r for r in leads if r['screen_status'] == 'NOT_SELECTED_FOR_CRITICAL_SAMPLE']
    unsel_works = {ALIAS.get(r['doi'].lower(), r['doi'].lower()) for r in unsel}
    later = sorted(r['update_study_id'] for r in leads if r['screen_status'] == 'FULLTEXT_READ_INCLUDED')
    fr, fsrc = frame_counts(a.release12, len(later))

    fam = {}
    for r in inv:
        fam.setdefault(r['study_id'], r['collection'])
    n_core_inv = sum(c == 'CORE' for c in fam.values())
    n_sup_inv = sum(c == 'SUPPORT' for c in fam.values())
    assert TARGETED_ADDITION in fam
    core_all = fr['core'] + 1
    n_cs = core_all + fr['support']

    rows = [
        ('Crossref', 'Queries run / returning records', f"{len(log)} / {len({r['search_id'] for r in tri})}",
         'search_log.csv; crossref_title_triage.csv'),
        ('Crossref', 'Records identified', len(tri), 'crossref_title_triage.csv rows'),
        ('Crossref', 'Duplicate DOI rows removed', len(tri) - len(by_doi), 'rows minus distinct DOIs'),
        ('Crossref', 'Distinct DOIs screened at title', len(by_doi), 'distinct DOIs'),
        ('Crossref', 'Independent works among distinct DOIs', len(works), 'CL075 linked to CL074'),
        ('Crossref', 'Excluded at title', doi_status['EXCLUDED_AT_TITLE'], 'screen_status EXCLUDED_AT_TITLE'),
        ('Crossref', 'Already in the full-text frame', doi_status['REPRESENTED_IN_DOWNLOAD_CHECKLIST'],
         'screen_status REPRESENTED_IN_DOWNLOAD_CHECKLIST'),
        ('Crossref', 'Lead records assessed at title and available abstract', len(leads),
         'additional_lead_dispositions.csv rows'),
        ('Crossref', 'Independent works among lead records', len(lead_works), 'CL075 linked to CL074'),
        ('Crossref', 'Not selected: records (Supplementary Table S1)', len(unsel), 'NOT_SELECTED_FOR_CRITICAL_SAMPLE'),
        ('Crossref', 'Not selected: independent works', len(unsel_works), 'CL075 linked to CL074'),
        ('Crossref', 'Excluded (CG as RL action space)', lead_status['EXCLUDED'], 'EXCLUDED'),
        ('Crossref', 'Earlier report of an included family (S018)', lead_status['EARLIER_REPORT_OF_INCLUDED_FAMILY'],
         'EARLIER_REPORT_OF_INCLUDED_FAMILY'),
        ('Crossref', 'Supplied, read in full and added to the frame', f"{lead_status['FULLTEXT_READ_INCLUDED']} ({', '.join(later)})",
         'FULLTEXT_READ_INCLUDED'),
        ('Frame', 'Reports assembled for full-text assessment (initial)', fr['initial_reports'], fsrc),
        ('Frame', 'Reports assessed in full text (including 1 linked erratum)', fr['reports_assessed'], fsrc),
        ('Frame', 'Candidate families assessed', fr['families_assessed'], fsrc),
        ('Frame', 'Adjacent surveys excluded from method coding', fr['surveys_excluded'], fsrc),
        ('Frame', 'Families retained (core / supporting / background)',
         f"{fr['core'] + fr['support'] + fr['background']} ({fr['core']} / {fr['support']} / {fr['background']})", fsrc),
        ('Frame', 'Core families added by the targeted search of 14 October 2026', f'1 ({TARGETED_ADDITION})',
         'S105 in data/coded_inventory_v1_10.csv'),
        ('Included', 'Study families read in full (core / supporting / background)',
         f"{n_cs + fr['background']} ({core_all} / {fr['support']} / {fr['background']})", 'retained families plus S105'),
        ('Included', 'Coded inventory: variants', len(inv), 'data/coded_inventory_v1_10.csv rows'),
        ('Included', 'Coded inventory: families (core / supporting)', f'{len(fam)} ({n_core_inv} / {n_sup_inv})',
         'distinct study_id by collection'),
        ('Included', 'Core or supporting families not in the coded inventory', n_cs - len(fam),
         'core and supporting families minus inventory families'),
        ('Included', 'Background families (context only)', fr['background'], fsrc),
    ]
    expected = ['10 / 9', 180, 10, 170, 169, 52, 39, 79, 78, 74, 73, 1, 1, '3 (S102, S103, S104)', 101, 104, 103, 4,
                '99 (79 / 8 / 12)', '1 (S105)', '100 (80 / 8 / 12)', 130, '88 (80 / 8)', 0, 12]
    for (s, lab, n, src), e in zip(rows, expected):
        assert str(n) == str(e), (lab, n, e)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(['stream', 'stage', 'count', 'derivation'])
    w.writerows(rows)
    if a.check:
        with open(OUT, encoding='utf-8-sig', newline='') as f:
            same = f.read().replace('\r\n', '\n') == buf.getvalue()
        print(f'{OUT}: {"reproduced" if same else "DIFFERS"}')
        return 0 if same else 1
    with open(OUT, 'w', encoding='utf-8', newline='') as f:
        f.write(buf.getvalue())
    print('All Figure A.1 counts reproduced;', len(rows), 'rows written to', OUT)
    return 0


if __name__ == '__main__':
    sys.exit(main())
