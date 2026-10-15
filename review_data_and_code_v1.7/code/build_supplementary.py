#!/usr/bin/env python3
"""Build Supplementary Tables S1 (74 unselected Crossref leads) and S2 (complete-tree completion of the
24 core families with E4 evaluation). Run from the package root. Requires pandas and xlsxwriter.
Title-level categories in S1 and completion entries in S2 are curated judgments encoded below.
Version 1.7 qualifies completion by each report's own stopping rules. S044 and S091 were
rechecked against the accessed PDFs. Other rows retain the existing evidence-based coding.
Pass --csv-only when XLSX is authored separately, preserving the existing workbook layout."""
import csv, pandas as pd, html, sys
LEADS='search/additional_lead_dispositions.csv'
r=list(csv.DictReader(open(LEADS,encoding='utf-8-sig')))
CA={'CL005':'L2, L4','CL006':'L2','CL007':'L2','CL008':'L2','CL009':'L2','CL010':'L2','CL011':'L4','CL012':'L2',
    'CL023':'L4, L5','CL044':'L4','CL058':'L5','CL066':'L5','CL068':'L2, L6','CL070':'L5','CL071':'several',
    'CL073':'L2','CL074':'L5','CL075':'L5','CL077':'several','CL079':'several'}
RC=['CL013','CL015','CL016','CL017','CL018','CL019','CL020','CL021','CL022','CL024','CL025','CL027','CL028']
GC=['CL045','CL046']
LAB={'CA':'Classical acceleration at layers L1-L6 (potentially eligible; not coded)',
     'RC':'Shortest-path or RCSPP study without a stated CG interface',
     'AP':'CG/B&P application or formulation without a separately evaluated acceleration',
     'GC':'General method chapter'}
rows=[]
for x in r:
    if x['screen_status']!='NOT_SELECTED_FOR_CRITICAL_SAMPLE': continue
    lid=x['lead_id']
    cat='CA' if lid in CA else 'RC' if lid in RC else 'GC' if lid in GC else 'AP'
    note=''
    if lid=='CL075': note='Same title and venue as CL074; possible duplicate record'
    if lid=='CL079': note='Classical survey of acceleration strategies; cited in the article as context'
    if lid in ('CL006','CL007','CL010','CL011','CL012','CL044'): note='Cited in the article as classical context; not coded'
    rows.append({'Lead ID':lid,'Crossref query':x['search_id'],'Rank':x['rank'],'Authors':x['authors'],'Year':x['year'],
                 'Title':html.unescape(x['title']),'Venue':html.unescape(x['venue']),'DOI':x['doi'],
                 'Recorded disposition':'Not selected for the critical sample (title and available abstract; full text not assessed)',
                 'Screening date':x['screen_date'],
                 'Title-level category (provisional)':LAB[cat],'Category code':cat,
                 'Likely layer(s), title-level (CA only)':CA.get(lid,''),'Note':note})
s5=pd.DataFrame(rows)
print(s5['Category code'].value_counts().to_dict(), len(s5))
s5.to_csv('supplementary/Supplementary_Table_S1_unselected_leads.csv',index=False,encoding='utf-8')

# ---- S2: complete-tree (E4) completion
ev=pd.read_csv('data/release_1_2/evidence.csv')
a=pd.read_csv('data/variants_v1_6.csv',keep_default_na=False)
a['coll']=a.collection.map({'CORE':'C','SUPPORT':'S'}); a['typ']=a.method_type.map({'TRADITIONAL':'T','LEARNING_GUIDED':'ML'})
a['pub']=a.publication_type.map({'JOURNAL':'J','CONFERENCE':'Cnf','PREPRINT':'P','WORKSHOP':'W'})
a['study']=a.study_id; a['method']=a.method_id
e4=a[a.scopes.str.split('|').apply(lambda l: 'E4' in l) & (a.coll=='C')]
D={
'S017':('Yes','Five new optimality proofs on Solomon instances; five instances remain unsolved with LB/UB reported.','NR','No',''),
'S019':('Yes','70 of 74 instances solved by the proposed variant versus 65 of 74 by the baseline.','NR','No',''),
'S020':('Yes','470 (default) and up to 473 (IPColGen settings) instances proven optimal in the 1205-instance test set.','NR','No',''),
'S021':('Yes','200 of 200 instances solved to optimality in each problem class (CVRP and VRPTW).','Yes (near-optimal initial UB)','No',''),
'S022':('Yes','Tree proofs, tree time-outs, root failures and recovered incumbents distinguished; all 29 VRPTW 25-customer base cases solved.','NR','No',''),
'S023':('Yes','Optimal values reported for the four facility-count instances.','NR','No',''),
'S028':('Yes','Optimality proved for 42 of 42 instances with strong cuts under a one-hour limit; failures reported otherwise.','NR','No',''),
'S031':('Yes','132 versus 131 of 168 and 293 versus 288 of 504 instances solved.','NR','No',''),
'S033':('Yes','50 (SP1) and 47 (SP2) of 76 selected instances solved; failures retained as unsolved.','NR','No',''),
'S034':('Yes','Combined strategies prove optimality where baselines hit time or memory limits; 26 of 70 filtered instances solved with a BKS+1 initial UB.','Yes (BKS-based UB)','No','Several comparisons use selected instances'),
'S039':('Yes','14/14, 40/40 and 3/30 instances solved in reported benchmark sets; six open instances proved optimal (2.0-15.2 days).','NR','No',''),
'S044':('Yes','The report describes complete BPC solution runs for 33 selected VRPTW instances, using a supplied optimal upper bound and replayed branching decisions.','Yes (optimal UB)','No','Source checked: PDF pp.13, 15-17 (journal pp.308, 310-312), Section 6 and Table 2. Completion is supported by the stated full solution process and solved-instance text; the reported speedup is conditional on the supplied bound and controlled tree.'),
'S045':('Yes','459 two-arc-fixing proofs in the selected set; 551 EVRPTW instances proved within one hour.','Yes (known optimum + 1 for VRPTW)','No',''),
'S046':('Yes','10 proofs and 7 time-outs in the reported table.','NR','No',''),
'S048':('Yes','Exact optimal solutions reported for 13 nurse-rostering and 12 multiplexing instances (10 runs each).','NR','No','Time limit not reported'),
'S049':('Yes','Most test instances solved within the 4 h or 25000-open-node limits (e.g., 200/200 for one base instance).','NR','No',''),
'S052':('Yes','15 Class A proofs among 16 exact-dominance attempts.','NR','No',''),
'S053':('Yes','Zero-gap runs: 482 versus 444 and 1524 versus 1325 of 1584 runs (8000 s cutoff).','NR','No',''),
'S058':('Yes','All nine 5-day cases solved to optimality; 5 of 9 10-day cases.','NR','No',''),
'S062':('Yes','Complete tree solves on 90 CVRP150 instances with an optimal (or 0.1% above optimal) supplied UB; proofs for 2 of 5 selected large instances.','Yes (optimal or near-optimal UB)','No',''),
'S083':('Yes','A single showcased instance solved to optimality; the baseline exceeds memory.','NR','Yes','Supplement not accessed'),
'S088':('Yes','Optimal cases 14/17/3/1 (learned) versus 14/9/4/0 (solution-pool baseline), each out of 28.','NR','No',''),
'S091':('Yes','The main report states that all four policies completed 18 of 30 benchmark families within the 60-second limit under the prescribed numerical gap criterion.','NR','No','Source checked: PDF pp.28-31, Theorem 1 and Sections 7.1-7.3. Numerical gap thresholds and complete per-policy outcomes are referred to the unavailable supplement. Reported completion is not recoded as verified exact optimality; preprint.'),
'S102':('No','No decomposition tree proof: 0 of 6 small tree checks completed; comparative runs limit-terminated.','NR','No','Online File S1 not accessed'),
}
rows=[]
for sid,g in e4.groupby('study'):
    evs=ev[(ev.study_id==sid) & ev.empirical_scope.astype(str).str.contains('E4')].evidence_id.tolist()
    comp,basis,ub,single,chk=D[sid]
    rows.append({'Family':sid,'Study':g.citation.iloc[0],'Publication status':g.pub.iloc[0],
                 'Variants evaluated at E4':', '.join(g.method),'Type(s)':'/'.join(sorted(set(g.typ))),
                 'At least one completed tree solve reported':comp,'Basis in accessed report':basis,
                 'Upper bound supplied to the tree':ub,'Single showcased instance':single,
                 'Evidence records (release 1.2 IDs)':'; '.join(evs) if evs else 'Recorded in Table A.1 only',
                 'Check note':chk or ''})
s6=pd.DataFrame(rows)
print(len(s6), (s6['At least one completed tree solve reported']=='Yes').sum(), s6['Upper bound supplied to the tree'].str.startswith('Yes').sum(), (s6['Single showcased instance']=='Yes').sum(), s6['Type(s)'].str.contains('ML').sum())
s6.to_csv('supplementary/Supplementary_Table_S2_complete_tree_completion.csv',index=False,encoding='utf-8')
if '--csv-only' in sys.argv:
    raise SystemExit(0)
import datetime
with pd.ExcelWriter('supplementary/Supplementary_Tables_S1_S2.xlsx',engine='xlsxwriter') as w:
    w.book.set_properties({'created': datetime.datetime(2026,10,14)})
    readme=pd.DataFrame({'Item':['Article','Table S1','Table S2','Provenance','Status'],
     'Description':['Accelerating Column Generation and Branch-and-Price with Traditional and Learning-Guided Methods: A Critical Review (X. Yang)',
       'The 74 Crossref follow-up leads not selected for the critical sample. Assessed at title and available-abstract level only; not full-text exclusions. Title-level categories were assigned while preparing the article and are provisional.',
       'The 24 core families with at least one variant evaluated in a complete B&P/BPC implementation (E4), with reported completion under each source\'s stopping rules, supplied upper bounds and single-instance cases. Completion does not impose a common numerical optimality threshold.',
       'Bibliographic data from the logged Crossref export (search/additional_lead_dispositions.csv, data release 1.2); completion entries from evidence.csv (release 1.2) and Table A.1.',
       'AI-assisted coding. S044 and S091 completion passages were rechecked against the accessed PDFs in version 1.7. The inventory does not constitute independent human double coding.']})
    for name,df in [('README',readme),('Table S1 unselected leads',s5),('Table S2 E4 completion',s6)]:
        df.to_excel(w,sheet_name=name[:31],index=False)
        ws=w.sheets[name[:31]]
        fmt=w.book.add_format({'text_wrap':True,'valign':'top','font_name':'Arial','font_size':9})
        hdr=w.book.add_format({'bold':True,'text_wrap':True,'valign':'top','font_name':'Arial','font_size':9,'bottom':1})
        for j,c in enumerate(df.columns):
            width=min(60,max(10,int(df[c].astype(str).str.len().quantile(0.9)*0.9) if len(df) else 12))
            ws.set_column(j,j,width,fmt)
            ws.write(0,j,c,hdr)
        ws.freeze_panes(1,0)
print('ok')
