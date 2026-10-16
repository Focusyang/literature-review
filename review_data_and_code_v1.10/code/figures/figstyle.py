# Shared style for Figures 1-3 and A.1 (v1.10): warm greys with one accent colour.
# Canvas widths 190 mm or 140 mm, Arial 6-8 pt, embedded TrueType fonts.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Polygon
import os
plt.rcParams.update({
    'font.family': 'Arial', 'font.size': 7, 'pdf.fonttype': 42, 'ps.fonttype': 42,
    'svg.fonttype': 'none', 'svg.hashsalt': 'cor-review-v1.10', 'axes.linewidth': 0.6,
    'mathtext.fontset': 'custom', 'mathtext.rm': 'Arial', 'mathtext.it': 'Arial:italic',
    'mathtext.bf': 'Arial:bold',
})
# Neutral palette
TEXT = '#2C2C2B'    # main text
SEC = '#6B6863'     # secondary text
LINE = '#55534F'    # arrows and lines
BORDER = '#B8B4AE'  # box outlines
PANEL = '#F5F4F2'   # panel background
FILL = '#ECEAE6'    # neutral fill for grouped or decision elements
NODE = '#D9D6D1'    # processed tree nodes
WHITE = '#FFFFFF'
# Single accent, used only for the key element of each figure
ACC = '#1F4E79'
ACC_T = '#E4ECF4'
MM = 1 / 25.4


def canvas(wmm, hmm):
    fig = plt.figure(figsize=(wmm * MM, hmm * MM))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, wmm); ax.set_ylim(0, hmm); ax.axis('off')
    return fig, ax


def box(ax, x, y, w, h, fc=WHITE, ec=BORDER, lw=0.7, r=1.2, ls='-', z=2):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0,rounding_size={r}', fc=fc, ec=ec,
                       lw=lw, ls=ls, zorder=z, joinstyle='round')
    ax.add_patch(p)
    return p


def txt(ax, x, y, s, size=7, weight='normal', color=TEXT, ha='center', va='center', style='normal',
        z=5, ls=1.25, **kw):
    return ax.text(x, y, s, fontsize=size, fontweight=weight, color=color, ha=ha, va=va,
                   fontstyle=style, zorder=z, linespacing=ls, **kw)


def badge(ax, x, y, label, fc=ACC, size=6.8, w=6.2, h=3.6):
    box(ax, x, y - h / 2, w, h, fc=fc, ec=fc, lw=0.5, r=0.9, z=6)
    txt(ax, x + w / 2, y, label, size=size, weight='bold', color=WHITE, z=7)


def arrow(ax, p1, p2, color=LINE, lw=0.8, ms=7, style='-|>', cs='arc3', z=3, shrinkA=0, shrinkB=0, ls='-'):
    a = FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=ms, color=color, lw=lw,
                        connectionstyle=cs, zorder=z, shrinkA=shrinkA, shrinkB=shrinkB, linestyle=ls,
                        joinstyle='miter', capstyle='butt')
    ax.add_patch(a)
    return a


def poly_arrow(ax, pts, color=LINE, lw=0.8, ms=7, z=3, ls='-'):
    """Polyline with an arrowhead on the last segment."""
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    ax.plot(xs[:-1], ys[:-1], color=color, lw=lw, zorder=z, solid_joinstyle='miter', ls=ls)
    arrow(ax, pts[-2], pts[-1], color=color, lw=lw, ms=ms, z=z, ls=ls)


OUTDIR = os.environ.get('FIG_OUT', 'figures')


def save(fig, name, dpi=600):
    os.makedirs(OUTDIR, exist_ok=True)
    fig.savefig(f'{OUTDIR}/{name}.pdf', metadata={'CreationDate': None})
    fig.savefig(f'{OUTDIR}/{name}.png', dpi=dpi)
    fig.savefig(f'{OUTDIR}/{name}.svg', metadata={'Date': None})
    plt.close(fig)
