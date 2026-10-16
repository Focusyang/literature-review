import json, urllib.request, time
MAILTO = ''  # polite-pool address intentionally not recorded in the released log
def get(url, tries=4):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'review-coverage-check/1.10'})
            return json.loads(urllib.request.urlopen(req, timeout=60).read().decode())
        except Exception as ex:
            err = str(ex); time.sleep(2 + 3 * k)
    return {'_error': err}
def abstract(w):
    inv = w.get('abstract_inverted_index') or {}
    pos = {}
    for t, ps in inv.items():
        for p in ps: pos[p] = t
    return ' '.join(pos[i] for i in sorted(pos))
