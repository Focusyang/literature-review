#!/usr/bin/env python3
"""Recompute the selection counts shown in Figure A.1 and write data/selection_flow_v1_6.csv.

Left stream: logged Crossref discovery export (search/*.csv, 11-12 October 2026).
Right stream: author-assembled full-text frame (data/release_1_2/screening.csv and read_reports.csv)
plus the family added by the targeted search of 14 October 2026 (data/studies_added_v1_6.csv).
Run from the package root; only the standard library is required.
"""
import csv
from collections import Counter


def rd(p):
    with open(p, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


log = [r for r in rd('search/search_log.csv') if r['search_id'].startswith('CRQ')]
tri = rd('search/crossref_title_triage.csv')
leads = rd('search/additional_lead_dispositions.csv')
scr = rd('data/release_1_2/screening.csv')
rep = rd('data/release_1_2/read_reports.csv')
added = rd('data/studies_added_v1_6.csv')
var = rd('data/variants_v1_6.csv')

by_doi = {}
for r in tri:
    by_doi.setdefault(r['doi'].lower(), set()).add(r['screen_status'])
assert all(len(s) == 1 for s in by_doi.values())
doi_status = Counter(next(iter(s)) for s in by_doi.values())
lead_status = Counter(r['screen_status'] for r in leads)
fam_dec = Counter(r['decision'] for r in scr)
supplied_reports = [r for r in rep if r['report_id'].startswith('FT-') and '-SUP' not in r['report_id']]  # excludes the separately accessed e-companion
later = sorted(r['update_study_id'] for r in leads if r['screen_status'] == 'FULLTEXT_READ_INCLUDED')
core_added = sum(r['collection'] == 'CORE' for r in added)

rows = [
    ('Crossref', 'Queries run / returning records', f"{len(log)} / {len({r['search_id'] for r in tri})}", 'search_log.csv; crossref_title_triage.csv'),
    ('Crossref', 'Records identified', len(tri), 'crossref_title_triage.csv rows'),
    ('Crossref', 'Duplicate DOI rows removed', len(tri) - len(by_doi), 'rows minus distinct DOIs'),
    ('Crossref', 'Distinct DOIs screened at title', len(by_doi), 'distinct DOIs'),
    ('Crossref', 'Excluded at title', doi_status['EXCLUDED_AT_TITLE'], 'screen_status EXCLUDED_AT_TITLE'),
    ('Crossref', 'Already in the full-text frame', doi_status['REPRESENTED_IN_DOWNLOAD_CHECKLIST'], 'screen_status REPRESENTED_IN_DOWNLOAD_CHECKLIST'),
    ('Crossref', 'Leads assessed at title and available abstract', len(leads), 'additional_lead_dispositions.csv rows'),
    ('Crossref', 'Not selected for the critical sample (Supplementary Table S1)', lead_status['NOT_SELECTED_FOR_CRITICAL_SAMPLE'], 'NOT_SELECTED_FOR_CRITICAL_SAMPLE'),
    ('Crossref', 'Excluded (CG as RL action space)', lead_status['EXCLUDED'], 'EXCLUDED'),
    ('Crossref', 'Earlier report of an included family (S018)', lead_status['EARLIER_REPORT_OF_INCLUDED_FAMILY'], 'EARLIER_REPORT_OF_INCLUDED_FAMILY'),
    ('Crossref', 'Supplied, read in full and added to the frame', f"{lead_status['FULLTEXT_READ_INCLUDED']} ({', '.join(later)})", 'FULLTEXT_READ_INCLUDED'),
    ('Frame', 'Reports assembled for full-text assessment (initial)', len(supplied_reports) - lead_status['FULLTEXT_READ_INCLUDED'], 'supplied FT- reports minus later additions'),
    ('Frame', 'Reports assessed in full text', len(supplied_reports), 'read_reports.csv supplied reports, excluding the separately accessed e-companion (includes 1 linked erratum)'),
    ('Frame', 'Candidate families assessed', len(scr), 'screening.csv rows'),
    ('Frame', 'Adjacent surveys excluded from method coding', fam_dec['EXCLUDED'], 'decision EXCLUDED'),
    ('Frame', 'Families retained in release 1.2 (core / supporting / background)', f"{fam_dec['CORE'] + fam_dec['SUPPORT'] + fam_dec['BACKGROUND']} ({fam_dec['CORE']} / {fam_dec['SUPPORT']} / {fam_dec['BACKGROUND']})", 'decisions CORE, SUPPORT, BACKGROUND'),
    ('Frame', 'Core families added by the targeted search of 14 October 2026', core_added, 'studies_added_v1_6.csv'),
    ('Included', 'Study families included (core / supporting / background)', f"{fam_dec['CORE'] + fam_dec['SUPPORT'] + fam_dec['BACKGROUND'] + len(added)} ({fam_dec['CORE'] + core_added} / {fam_dec['SUPPORT']} / {fam_dec['BACKGROUND']})", 'release 1.2 plus additions'),
    ('Included', 'Coded method variants (core and supporting families)', len(var), 'variants_v1_6.csv rows'),
]
expected = ['10 / 9', 180, 10, 170, 52, 39, 79, 74, 1, 1, '3 (S102, S103, S104)', 101, 104, 103, 4, '99 (79 / 8 / 12)', 1, '100 (80 / 8 / 12)', 146]
for (s, lab, n, src), e in zip(rows, expected):
    assert str(n) == str(e), (lab, n, e)
with open('data/selection_flow_v1_6.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['stream', 'stage', 'count', 'derivation'])
    w.writerows(rows)
print('All Figure A.1 counts reproduced;', len(rows), 'rows written to data/selection_flow_v1_6.csv')
