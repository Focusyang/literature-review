# Figure 1: six intervention layers (conceptual diagram). Accent: layer badges, node in process,
# and the certification path (closure check and certified node bound).
from figstyle import *
import math
W, H = 190, 104
fig, ax = canvas(W, H)
# ---------- panel (a): search tree ----------
box(ax, 1, 1, 56, H - 2, fc=PANEL, ec='none', r=2, z=0)
txt(ax, 4, H - 4.5, '(a) Integer search tree', size=8, weight='bold', ha='left')
badge(ax, 4, H - 11.2, 'L1')
txt(ax, 11.8, H - 11.2, 'Tree control', size=7.4, weight='bold', ha='left')
txt(ax, 4, H - 15.0, 'Branching disjunctions, candidate\nevaluation and open-node selection', size=6.6,
    ha='left', va='top', color=SEC)
R = 3.0
nodes = {'r': (27, 68), 'a': (15, 52), 'b': (39, 52), 'c': (8, 36), 'd': (22, 36)}
edges = [('r', 'a', '$x_a=0$', 'l'), ('r', 'b', '$x_a=1$', 'r'), ('a', 'c', '', ''), ('a', 'd', '', '')]
for u, v, lab, side in edges:
    (x1, y1), (x2, y2) = nodes[u], nodes[v]
    d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    ax.plot([x1 + ux * R, x2 - ux * R], [y1 + uy * R, y2 - uy * R], color=LINE, lw=0.7, zorder=2)
    if lab:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        txt(ax, mx + (-2.6 if side == 'l' else 2.6), my + 1.0, lab, size=6.6, ha='right' if side == 'l' else 'left')
style = {'r': (NODE, LINE, '-'), 'a': (NODE, LINE, '-'), 'b': (ACC, ACC, '-'), 'c': (WHITE, LINE, '--'),
         'd': (NODE, LINE, '-')}
for k, (x, y) in nodes.items():
    fc, ec, ls = style[k]
    ax.add_patch(Circle((x, y), R, fc=fc, ec=ec, lw=0.8, ls=ls, zorder=4))
fx, fy = nodes['d']
ax.plot([fx - 1.6, fx + 1.6], [fy - 1.6, fy + 1.6], color=LINE, lw=0.9, zorder=5)
ax.plot([fx - 1.6, fx + 1.6], [fy + 1.6, fy - 1.6], color=LINE, lw=0.9, zorder=5)
bx, by = nodes['b']
txt(ax, bx, by - 4.4, 'current node', size=6.2, color=ACC, va='top')
txt(ax, nodes['c'][0], nodes['c'][1] - 4.4, 'open', size=6.0, color=SEC, va='top', ls=1.05)
txt(ax, fx, fy - 4.4, 'pruned\nby bound', size=6.0, color=SEC, va='top', ls=1.05)
for i, (fc, ec, ls, lab) in enumerate([(ACC, ACC, '-', 'node in process'), (NODE, LINE, '-', 'processed node'),
                                       (WHITE, LINE, '--', 'open node')]):
    ly = 21.5 - i * 4.4; x = 6.5
    ax.add_patch(Circle((x, ly), 1.5, fc=fc, ec=ec, lw=0.7, ls=ls, zorder=4))
    txt(ax, x + 2.8, ly, lab, size=6.2, ha='left', color=SEC)
txt(ax, 4, 5.2, 'Learned scores may rank candidates or nodes,\nbut each disjunction must stay valid.', size=6.1,
    ha='left', color=SEC, style='italic', ls=1.1)
# ---------- panel (b): node processing ----------
X0 = 61
box(ax, X0, 1, W - X0 - 1, H - 2, fc=PANEL, ec='none', r=2, z=0)
txt(ax, X0 + 3, H - 4.5, '(b) Column generation at the current node', size=8, weight='bold', ha='left')
rx, ry, rw, rh = X0 + 4, 60, 52, 28
box(ax, rx, ry, rw, rh, fc=WHITE, ec=BORDER)
badge(ax, rx + 3, ry + rh - 5, 'L2')
txt(ax, rx + 11, ry + rh - 5, 'Master and dual guidance', size=7.2, weight='bold', ha='left')
txt(ax, rx + 3, ry + rh - 9.6, 'Restricted master problem (RMP):\ninitial columns, master solution,\nstabilization and the dual point\nsupplied to pricing',
    size=6.6, ha='left', va='top')
cx, cy, cw_, chh = X0 + 4, 28, 52, 22
box(ax, cx, cy, cw_, chh, fc=WHITE, ec=BORDER)
badge(ax, cx + 3, cy + chh - 5, 'L6')
txt(ax, cx + 11, cy + chh - 5, 'Generated-column management', size=7.2, weight='bold', ha='left')
txt(ax, cx + 3, cy + chh - 9.6, 'Admission, pool storage, deletion,\nreuse and fixing once a column\nexists', size=6.6,
    ha='left', va='top')
px, py, pw, ph = X0 + 68, 30, W - X0 - 1 - 68 - 3, 64
box(ax, px, py, pw, ph, fc=FILL, ec=BORDER, lw=0.6, r=1.6, z=1)
txt(ax, px + 3, py + ph - 4, 'Pricing problem(s)', size=7.4, weight='bold', ha='left', color=TEXT)
inner = [('L3', 'Pricing orchestration', 'Which block or oracle to call next,\nincluding cascades and partial pricing', 15.2),
         ('L4', 'Pricing domain and state', 'Admissible arcs and paths, resource\nmemory, dominance, bound-based\nelimination', 18.6),
         ('L5', 'Internal search and construction', 'Order of retained labels or states,\nor sequential construction of a column', 15.2)]
ig = 2.0; ytop = py + ph - 8.0
for k, (b, t, dsc, ih) in enumerate(inner):
    yy = ytop - ih; ytop = yy - ig
    box(ax, px + 2.5, yy, pw - 5, ih, fc=WHITE, ec=BORDER)
    badge(ax, px + 5, yy + ih - 4.2, b)
    txt(ax, px + 13, yy + ih - 4.2, t, size=7.2, weight='bold', ha='left')
    txt(ax, px + 5, yy + ih - 8.1, dsc, size=6.6, ha='left', va='top')
assert yy >= py + 1.5, (yy, py)
yd = ry + rh - 8
poly_arrow(ax, [(rx + rw, yd), (px, yd)])
txt(ax, (rx + rw + px) / 2, yd + 1.7, r'duals $\pi$', size=6.6)
yc = cy + chh / 2 + 1
poly_arrow(ax, [(px, yc), (cx + cw_, yc)])
txt(ax, (cx + cw_ + px) / 2, yc + 1.6, 'candidate\ncolumns', size=6.4, va='bottom', ls=1.05)
poly_arrow(ax, [(cx + cw_ / 2, cy + chh), (cx + cw_ / 2, ry)])
txt(ax, cx + cw_ / 2 + 1.5, (cy + chh + ry) / 2, 'admitted columns', size=6.4, ha='left')
# closure check: the certification path is the only accented element in panel (b)
gx, gy, gw, gh = px, 3, pw, 20
box(ax, gx, gy, gw, gh, fc=ACC_T, ec=ACC, lw=0.9)
txt(ax, gx + 3, gy + gh - 3.8, 'Closure check (Sections 3 and 6)', size=7.0, weight='bold', ha='left', color=ACC)
txt(ax, gx + 3, gy + gh - 7.2, 'The node LP closes only with a valid lower\nbound over the full current domain of every\nblock. Otherwise recover, or keep the node\nopen with its last valid bound.',
    size=6.3, ha='left', va='top', ls=1.15)
poly_arrow(ax, [(px + pw / 2, py), (px + pw / 2, gy + gh)], color=ACC, lw=0.9)
txt(ax, px + pw / 2 + 1.5, (py + gy + gh) / 2, 'no improving column found', size=6.2, ha='left', color=ACC)
yg = gy + gh / 2 - 1
poly_arrow(ax, [(gx, yg), (50, yg), (50, 49.3), (41.4, 49.3)], color=ACC, lw=0.9)
txt(ax, X0 + 5, yg + 1.6, 'certified node bound: prune or branch', size=6.2, ha='left', color=ACC, va='bottom')
# connector current node -> RMP (neutral)
arrow(ax, (bx + R * 0.8, by + R * 0.6), (rx - 0.4, ry + 8), color=LINE, lw=0.8, cs='arc3,rad=-0.22')
txt(ax, 44, 71, 'node model:\nbranch rows,\ncuts', size=6.1, color=SEC, ha='left', ls=1.05)
save(fig, 'Figure_1')
