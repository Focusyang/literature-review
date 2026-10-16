# Figure 2: from a checked proposal to valid LP closure (conceptual flow).
# Accent: the certified outcome only. Decision steps use a neutral fill.
from figstyle import *
W, H = 140, 122
fig, ax = canvas(W, H)
mx, mw = 12, 73; cxm = mx + mw / 2
rxx, rw = 96, 40
DASH = (0, (3, 1.6))


def node(y, h, title, body, fc=WHITE, ec=BORDER, ls='-', lw=0.7, tcol=TEXT, x=mx, w=mw):
    box(ax, x, y, w, h, fc=fc, ec=ec, ls=ls, lw=lw)
    if title:
        txt(ax, x + w / 2, y + h - 3.4, title, size=7.0, weight='bold', color=tcol)
        txt(ax, x + w / 2, y + h - 6.6, body, size=6.6, va='top', ls=1.15)
    else:
        txt(ax, x + w / 2, y + h / 2, body, size=6.8, ls=1.15)


y1, h1 = 102, 14; y2, h2 = 81, 14; y3, h3 = 60, 13; y4, h4 = 39, 13; y5, h5 = 18, 13
node(y1, h1, 'Node LP at the current dual', 'RMP solved with the node rows (branching\nconstraints, active cuts) passes duals $\\pi$ to pricing')
node(y1, h1, 'If the RMP is infeasible', 'Phase-I or Farkas pricing\nbefore any closure (Sect. 6.1)', x=rxx, w=rw)
node(y2, h2, 'Discovery', 'Heuristic, learned or restricted pricing\nproposes candidate columns', ls=DASH, ec=SEC)
node(y3, h3, None, 'Is a proposed column legal at this node,\nwith verified negative reduced cost at $\\pi$?', fc=FILL, ec=BORDER, lw=0.8)
node(y3, h3, None, 'Admit column(s) and\nre-optimize the RMP', x=rxx, w=rw)
node(y4, h4, None, 'Does a valid lower bound $\\geq 0$ (within tolerance)\ncover the full current domain of every block?', fc=FILL, ec=BORDER, lw=0.8)
node(y4, h4, 'LP closure certified', 'Valid node bound,\nthen prune or branch', x=rxx, w=rw, fc=ACC_T, ec=ACC, lw=1.0, tcol=ACC)
node(y5, h5, 'Recovery (G2)', 'Restore the full current domain or call a\ncertifying oracle, and count its cost in the run')
node(y5, h5, 'Interrupted or unchecked', 'Node stays open with the last\nvalid bound, e.g. Eq. (3)', x=rxx, w=rw, ec=LINE, lw=0.8)
for (ya, yb, lab) in [(y1, y2 + h2, ''), (y2, y3 + h3, ''), (y3, y4 + h4, 'No'), (y4, y5 + h5, 'No')]:
    arrow(ax, (cxm, ya), (cxm, yb))
    if lab:
        txt(ax, cxm + 1.6, (ya + yb) / 2, lab, size=6.4, ha='left', color=SEC)
for yy, col, lw in [(y3 + h3 / 2, LINE, 0.8), (y4 + h4 / 2, ACC, 1.0)]:
    arrow(ax, (mx + mw, yy), (rxx, yy), color=col, lw=lw)
    txt(ax, (mx + mw + rxx) / 2, yy + 1.4, 'Yes', size=6.4, color=SEC, va='bottom')
arrow(ax, (mx + mw, y1 + h1 / 2), (rxx, y1 + h1 / 2), ls=DASH, color=SEC)
xr = rxx + rw / 2
poly_arrow(ax, [(xr, y3 + h3), (xr, y1 - 3.5), (cxm + 28, y1 - 3.5), (cxm + 28, y1)])
txt(ax, xr + 1.4, (y3 + h3 + y1 - 3.5) / 2, 'next\niteration', size=6.0, ha='left', color=SEC, ls=1.05)
xl = 7.0
poly_arrow(ax, [(mx, y5 + h5 / 2), (xl, y5 + h5 / 2), (xl, y3 + h3 / 2), (mx, y3 + h3 / 2)])
txt(ax, xl - 1.9, (y5 + h5 / 2 + y3 + h3 / 2) / 2, 'columns or bounds returned', size=6.0, color=SEC, rotation=90)
arrow(ax, (mx + mw, y5 + h5 / 2), (rxx, y5 + h5 / 2), color=LINE, lw=0.8)
items = [(dict(fc=WHITE, ec=SEC, ls=DASH, lw=0.7), 'may be heuristic or learned'),
         (dict(fc=FILL, ec=BORDER, ls='-', lw=0.8), 'requires a valid check'),
         (dict(fc=ACC_T, ec=ACC, ls='-', lw=1.0), 'certified outcome')]
xs = [12, 52, 86]
for (st, lab), x in zip(items, xs):
    yy = 8.0
    box(ax, x, yy - 1.6, 5.5, 3.2, r=0.6, **st)
    txt(ax, x + 7.5, yy, lab, size=6.2, ha='left', color=SEC)
save(fig, 'Figure_2')
