#!/usr/bin/env python3
"""Regenerate Figures 1-3 and A.1 into figures/ (run from the package root).

Figures 1 and 2 are conceptual diagrams. Figure 3 reads data/coded_inventory_v1_9.csv.
Figure A.1 draws the selection counts listed in data/selection_flow_v1_9.csv.
Requires matplotlib, numpy and pandas. The Arial font is expected (Liberation Sans is a metric-compatible substitute).
"""
import os, runpy, sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
for name in ['fig1.py', 'fig2.py', 'fig3.py', 'figA1.py']:
    runpy.run_path(os.path.join(here, name), run_name='__main__')
    print('done', name)
