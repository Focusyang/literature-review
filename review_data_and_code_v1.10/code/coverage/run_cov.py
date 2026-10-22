import json, urllib.request, urllib.parse, time, datetime, re, csv, sys
from oa import get, abstract
import argparse, os
ap=argparse.ArgumentParser(description='Repeat the public discovery queries. Live results may differ; raw abstracts are for local use only.')
ap.add_argument('--out-dir', required=True, help='Separate local output directory; do not overwrite the released snapshot')
a=ap.parse_args()
os.makedirs(a.out_dir, exist_ok=True)
os.chdir(a.out_dir)
TZ=datetime.timezone(datetime.timedelta(hours=8))
Q=[('L1','T','"branch-and-price" branching rule',''),('L1','M','"branch-and-price" branching learning',''),
('L1','T','"branch-price-and-cut" node selection',''),('L2','T','"column generation" stabilization dual',''),
('L2','T','"column generation" "dual-optimal inequalities"',''),('L2','T','"column generation" initial columns warm start',''),
('L2','M','"column generation" dual learning prediction',''),('L3','T','"column generation" heuristic pricing',''),
('L3','M','"column generation" pricing machine learning',''),('L3','T','"branch-and-price" pricing strategy subproblems',''),
('L4','T','"branch-price-and-cut" "reduced cost" fixing elimination',''),('L4','T','"column generation" lagrangian bound early termination',''),
('L4','T','"resource constraints" "completion bounds" labeling',''),('L4','M','"column generation" graph reduction learning',''),
('L5','T','"labeling algorithm" "column generation" bidirectional',''),('L5','M','"resource constrained shortest path" learning',''),
('L5','T','"decremental state space relaxation" OR "ng-route"',''),('L6','T','"column generation" "column selection"',''),
('L6','T','"column generation" "column management" OR "column pool"',''),('L6','M','"column generation" diving OR "variable fixing" learning',''),
('L1','T','"node selection" "column generation"','reformulates CV03'),('L1','T','"strong branching" "branch-and-price"',''),
('L4','T','"reduced cost fixing" "column generation"','reformulates CV11'),('L4','T','"arc elimination" "branch-price-and-cut"','reformulates CV11'),
('L4','T','"column generation" "lagrangian bound"','reformulates CV12'),('L4','T','"column generation" "early termination"','reformulates CV12'),
('L2','T','"column generation" "tailing-off"',''),('L2','T','"column generation" "dual smoothing"',''),
('L2','T','"column generation" "dual inequalities"',''),('L2','T','"primal-dual column generation"',''),
('L3','M','"pricing problem" "graph neural network"',''),('L3','T','"column generation" "partial pricing"',''),
('ALL','M','"column generation" "reinforcement learning"',''),('ALL','M','"branch-and-price" "machine learning"',''),
('L5','T','"elementary shortest path" dominance "column generation"',''),('L6','T','"column generation" "column pool"','reformulates CV19'),
('L6','T','"column generation" "column management"','reformulates CV19')]
assert len(Q)==37
log=[]; recs={}
for i,(lay,kind,q,note) in enumerate(Q,1):
    sid=f"CV{i:02d}"; ts=datetime.datetime.now(TZ).isoformat(timespec='seconds')
    url=f"https://api.openalex.org/works?filter=title_and_abstract.search:{urllib.parse.quote(q)}&sort=relevance_score:desc&per-page=50"
    d=get(url)
    if '_error' in d:
        log.append(dict(search_id=sid,source='OpenAlex API',search_date=ts,layer=lay,kind=kind,query=q,url=url,hit_count='',exported=0,status='FAILED '+d['_error'][:80],note=note)); continue
    res=d.get('results',[])
    log.append(dict(search_id=sid,source='OpenAlex API',search_date=ts,layer=lay,kind=kind,query=q,url=url,hit_count=d.get('meta',{}).get('count'),exported=len(res),status='SUCCESS',note=note))
    for rank,w in enumerate(res,1):
        key=w['id']
        if key not in recs:
            recs[key]=dict(openalex=w['id'],doi=(w.get('doi') or '').replace('https://doi.org/','').lower(),title=w.get('title') or '',year=w.get('publication_year'),type=w.get('type'),
               venue=((w.get('primary_location') or {}).get('source') or {}).get('display_name',''),abstract=abstract(w),
               authors='; '.join(a['author']['display_name'] for a in w.get('authorships',[])[:6]),hits=[])
        recs[key]['hits'].append(f"{sid}#{rank}")
    time.sleep(0.5)
AQ=[('ALL','M','all:"column generation" AND (all:learning OR all:neural)'),
    ('ALL','M','all:"branch-and-price" AND (all:learning OR all:neural)'),
    ('L5','M','(all:"resource constrained shortest path" OR all:ESPPRC OR all:SPPRC) AND all:learning'),
    ('L2','T','all:"column generation" AND (all:stabilization OR all:stabilized OR all:dual)'),
    ('ALL','T','(all:"branch-price-and-cut" OR all:"branch-and-price") AND (all:acceleration OR all:accelerating OR all:faster)')]
for j,(lay,kind,q) in enumerate(AQ,1):
    sid=f"CA{j:02d}"; ts=datetime.datetime.now(TZ).isoformat(timespec='seconds')
    url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'max_results':60,'sortBy':'submittedDate','sortOrder':'descending'})
    ok=False
    for k in range(4):
        try:
            x=urllib.request.urlopen(url,timeout=60).read().decode(); ok=True; break
        except Exception as ex:
            err=str(ex); time.sleep(5)
    if not ok:
        log.append(dict(search_id=sid,source='arXiv API',search_date=ts,layer=lay,kind=kind,query=q,url=url,hit_count='',exported=0,status='FAILED '+err[:80],note='')); continue
    tot=re.search(r'<opensearch:totalResults[^>]*>(\d+)<',x)
    ents=re.findall(r'<entry>(.*?)</entry>',x,re.S)
    log.append(dict(search_id=sid,source='arXiv API',search_date=ts,layer=lay,kind=kind,query=q,url=url,hit_count=tot.group(1) if tot else '',exported=len(ents),status='SUCCESS',note=''))
    for rank,e in enumerate(ents,1):
        aid=re.search(r'<id>(.*?)</id>',e).group(1).split('/abs/')[-1]
        t=re.sub(r'\s+',' ',re.search(r'<title>(.*?)</title>',e,re.S).group(1)).strip()
        s=re.sub(r'\s+',' ',re.search(r'<summary>(.*?)</summary>',e,re.S).group(1)).strip()
        pub=re.search(r'<published>(.*?)</published>',e).group(1)[:10]
        doi=re.search(r'<arxiv:doi[^>]*>(.*?)</arxiv:doi>',e); doi=doi.group(1).lower() if doi else ''
        au='; '.join(re.findall(r'<name>(.*?)</name>',e)[:6])
        key='arXiv:'+re.sub(r'v\d+$','',aid)
        if key not in recs:
            recs[key]=dict(openalex='',doi=doi,arxiv=aid,title=t,year=pub[:4],type='preprint',venue='arXiv',abstract=s,authors=au,published=pub,hits=[])
        recs[key]['hits'].append(f"{sid}#{rank}")
    time.sleep(3.5)
json.dump(recs,open('cov_records.json','w'),ensure_ascii=False,indent=0)
with open('cov_search_log.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(log[0].keys())); w.writeheader(); w.writerows(log)
print(len(log),'searches;',len(recs),'unique records')
for l in log: print(l['search_id'],l['status'][:10],l['hit_count'],l['exported'],l['query'][:60])
