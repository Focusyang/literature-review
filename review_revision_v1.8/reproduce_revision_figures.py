from pathlib import Path
import os, subprocess, sys
root = Path(__file__).resolve().parent
env = os.environ.copy()
env["VARIANTS"] = str(root / "修订依据/variants_v1_8_working.csv")
env["FIG_OUT"] = str(root / "reproduced_figures")
for name in ("fig3.py", "figA1.py"):
    subprocess.run([sys.executable, str(root / "修订依据/figure_sources" / name)], env=env, cwd=root, check=True)
