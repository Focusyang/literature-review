#!/usr/bin/env python3
"""Build the derived tables of version 1.9 (run from the package root).

  data/figure3_matrix_v1_9.csv       variant-scope memberships by type, primary mechanism and scope (Figure 3)
  data/figure3_margins_v1_9.csv      variants per type and primary mechanism, including variants without a scope
  supplementary/Supplementary_Tables_S1_S2.xlsx   formatted copy of the two supplementary CSV tables
  recoding_pack/coding_form_blank.xlsx            blank re-coding form with drop-down lists

Usage:
  python code/build_tables.py           # write the files
  python code/build_tables.py --check   # verify the CSV outputs and the workbook cell values
Requires xlsxwriter (writing) and openpyxl (checking).
"""
import csv, datetime, io, sys

INV = 'data/coded_inventory_v1_9.csv'
MATRIX = 'data/figure3_matrix_v1_9.csv'
MARGINS = 'data/figure3_margins_v1_9.csv'
S1 = 'supplementary/Supplementary_Table_S1_unselected_leads.csv'
S2 = 'supplementary/Supplementary_Table_S2_complete_tree_completion.csv'
XLSX = 'supplementary/Supplementary_Tables_S1_S2.xlsx'
FORM_CSV = 'recoding_pack/coding_form_blank.csv'
FORM_XLSX = 'recoding_pack/coding_form_blank.xlsx'
TYPES = [('ALL', None), ('TRADITIONAL', 'TRADITIONAL'), ('LEARNING_GUIDED', 'LEARNING_GUIDED')]
GS = ['G1', 'G2', 'G3', 'G4', 'G5', 'GU']
ES = ['E0', 'E1', 'E2', 'E3', 'E4']
FIXED_DATE = datetime.datetime(2026, 10, 16, 0, 0, 0)

README = [
    ('Item', 'Description'),
    ('Article', 'Accelerating Column Generation and Branch-and-Price with Traditional and Learning-Guided Methods: '
                'A Critical Review (X. Yang)'),
    ('Table S1', 'The 74 lead records from the logged Crossref follow-up that were not selected for the critical sample. '
                 'They represent 73 independent works, because CL074 and CL075 are two DOIs of the same work. '
                 'The leads were assessed at title and available-abstract level and are not full-text exclusions. '
                 '"Cited in the article" marks records that appear in the reference list of the article. '
                 'Chapters of cited books are marked separately.'),
    ('Table S2', 'The 24 core study families that evaluate at least one variant in a complete B&P or BPC implementation. '
                 'Completion is recorded under the stopping rules stated by each source. No common numerical optimality '
                 'threshold is imposed, so the completion column is not a uniform count of exact optimality proofs. '
                 'The table is compiled at family level. It includes three families (S039, S048 and S062) whose '
                 'variants are not listed in the coded inventory (Table A.1). Type(s): T traditional, ML learning-guided. '
                 'Publication status: J journal, Cnf conference, P preprint.'),
    ('Provenance', 'Table S1 bibliographic fields come from the logged Crossref export '
                   '(search/additional_lead_dispositions.csv). Table S2 entries come from the full-text records. '
                   'Evidence record identifiers refer to release 1.2 (evidence.csv), which is retained unchanged in '
                   'version 1.7 of this dataset.'),
    ('Status', 'Prepared with AI assistance and approved by the author. No independent human double screening or '
               'double coding was performed.'),
    ('Version', 'Version 1.9 of the data and code package. Zenodo concept DOI 10.5281/zenodo.23386415.'),
]
S1_WIDTHS = {'Lead ID': 10.7, 'Crossref query': 10.7, 'Rank': 6.7, 'Authors': 51.7, 'Year': 6.7, 'Title': 60.7,
             'Venue': 40.7, 'DOI': 26.7, 'Recorded disposition': 60.7, 'Screening date': 12.7,
             'Canonical work ID': 12.7, 'Count as independent work': 16.7, 'Cited in the article': 30.7}
S2_WIDTHS = {'Family': 10.7, 'Study': 24.7, 'Publication status': 10.7, 'Type(s)': 10.7,
             'At least one completed tree solve reported': 14.7, 'Basis in accessed report': 60.7,
             'Single showcased instance': 12.7, 'Evidence records (release 1.2 IDs)': 56.7}
FORM_WIDTHS = [12, 12, 12, 28, 12, 28, 28, 12, 28, 28, 28, 28, 12, 28, 12]
FORM_HELP = [
    'Independent re-coding form (Appendix B.3).',
    'Code each case in cases.csv without consulting the article, its tables, the coded inventory or the first-coder key.',
    'primary_layer: one of L1-L6 (NA only if the case is not a within-CG/B&P intervention). secondary_layers: codes separated by |.',
    'primary_mechanism: G1-G5, GU (accessed documentation does not establish the mechanism) or GU-offline '
    '(prediction only, no integrated guarantee target).',
    'scopes: every evaluated scope among E0-E4, separated by |, or NONE.',
    'Give page-, section- or table-level reasons for each decision.',
    'Save as CSV (UTF-8) and run: python code/agreement.py --key recoding_key/first_coder_key.csv --coder2 <file> --out agreement_results',
    'Definitions: see coding_definitions.md.',
]


def rd(p):
    with open(p, encoding='utf-8-sig', newline='') as f:
        r = csv.reader(f)
        head = next(r)
        return head, [row for row in r]


def to_csv(header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(header)
    w.writerows(rows)
    return buf.getvalue()


def figure3():
    with open(INV, encoding='utf-8-sig', newline='') as f:
        inv = list(csv.DictReader(f))
    assert len(inv) == 113
    for v in inv:
        v['G'] = 'GU' if v['primary_mechanism'] in ('GU', 'GU-offline') else v['primary_mechanism']
        v['E'] = [e for e in v['scopes'].split('|') if e]
    mrows, grows = [], []
    for tname, tval in TYPES:
        sub = [v for v in inv if tval is None or v['method_type'] == tval]
        for g in GS:
            sg = [v for v in sub if v['G'] == g]
            for e in ES:
                ids = sorted(v['method_id'] for v in sg if e in v['E'])
                mrows.append([tname, g, e, len(ids), '|'.join(ids)])
            grows.append([tname, g, len(sg), sum(not v['E'] for v in sg),
                          '|'.join(sorted(v['method_id'] for v in sg if not v['E']))])
    tot = {t: sum(r[3] for r in mrows if r[0] == t) for t, _ in TYPES}
    var = {t: sum(r[2] for r in grows if r[0] == t) for t, _ in TYPES}
    assert tot == {'ALL': 181, 'TRADITIONAL': 88, 'LEARNING_GUIDED': 93}, tot
    assert var == {'ALL': 113, 'TRADITIONAL': 58, 'LEARNING_GUIDED': 55}, var
    m = to_csv(['method_type', 'primary_mechanism', 'scope', 'n_variant_scope_memberships', 'method_ids'], mrows)
    g = to_csv(['method_type', 'primary_mechanism', 'n_variants', 'n_variants_without_scope',
                'method_ids_without_scope'], grows)
    return {MATRIX: m, MARGINS: g}


def write_sheet(wb, name, header, rows, widths, fmt_h, fmt_c):
    ws = wb.add_worksheet(name)
    for j, h in enumerate(header):
        ws.write_string(0, j, h, fmt_h)
        ws.set_column(j, j, widths[j] if isinstance(widths, list) else widths.get(h, 12.7))
    for i, row in enumerate(rows, 1):
        for j, v in enumerate(row):
            ws.write_string(i, j, v, fmt_c)
    ws.freeze_panes(1, 0)
    return ws


def workbooks():
    import xlsxwriter
    for path, kind in ((XLSX, 'supp'), (FORM_XLSX, 'form')):
        wb = xlsxwriter.Workbook(path)
        wb.set_properties({'title': 'Supplementary Tables S1 and S2' if kind == 'supp' else 'Re-coding form',
                           'author': 'Xinran Yang', 'created': FIXED_DATE})
        base = {'font_name': 'Arial', 'font_size': 9, 'text_wrap': True, 'valign': 'top'}
        fh = wb.add_format(dict(base, bold=True, bottom=1))
        fc = wb.add_format(base)
        if kind == 'supp':
            write_sheet(wb, 'README', README[0], README[1:], [10.7, 90.7], fh, fc)
            for src, name, widths in ((S1, 'Table S1 unselected leads', S1_WIDTHS), (S2, 'Table S2 E4 completion', S2_WIDTHS)):
                head, rows = rd(src)
                write_sheet(wb, name, head, rows, widths, fh, fc)
        else:
            head, rows = rd(FORM_CSV)
            ws = write_sheet(wb, 'Coding form', head, rows, FORM_WIDTHS, fh, fc)
            ws.freeze_panes(1, 1)
            n = len(rows)
            col = {h: j for j, h in enumerate(head)}
            for fld, vals in (('primary_layer', ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'NA']),
                              ('primary_mechanism', ['G1', 'G2', 'G3', 'G4', 'G5', 'GU', 'GU-offline', 'NA']),
                              ('confidence', ['1', '2', '3'])):
                ws.data_validation(1, col[fld], n, col[fld], {'validate': 'list', 'source': vals})
            wi = wb.add_worksheet('Instructions')
            wi.set_column(0, 0, 120)
            for i, t in enumerate(FORM_HELP):
                wi.write_string(i, 0, t, fh if i == 0 else fc)
        wb.close()


def check_workbooks():
    import openpyxl
    ok = True
    wb = openpyxl.load_workbook(XLSX, read_only=True)
    expect = [('README', [list(r) for r in README])]
    for src, name in ((S1, 'Table S1 unselected leads'), (S2, 'Table S2 E4 completion')):
        head, rows = rd(src)
        expect.append((name, [head] + rows))
    for name, rows in expect:
        got = [[('' if c is None else str(c)) for c in r] for r in wb[name].iter_rows(values_only=True)]
        same = got == rows
        print(f'{XLSX} [{name}]: {"reproduced" if same else "DIFFERS"}')
        ok &= same
    wb = openpyxl.load_workbook(FORM_XLSX, read_only=True)
    head, rows = rd(FORM_CSV)
    got = [[('' if c is None else str(c)) for c in r] for r in wb['Coding form'].iter_rows(values_only=True)]
    same = got == [head] + rows
    print(f'{FORM_XLSX} [Coding form]: {"reproduced" if same else "DIFFERS"}')
    return ok and same


def main():
    outs = figure3()
    if '--check' in sys.argv:
        ok = True
        for path, txt in outs.items():
            with open(path, encoding='utf-8-sig', newline='') as f:
                same = f.read().replace('\r\n', '\n') == txt
            print(f'{path}: {"reproduced" if same else "DIFFERS"}')
            ok &= same
        ok &= check_workbooks()
        return 0 if ok else 1
    for path, txt in outs.items():
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(txt)
    workbooks()
    print('written:', ', '.join(list(outs) + [XLSX, FORM_XLSX]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
