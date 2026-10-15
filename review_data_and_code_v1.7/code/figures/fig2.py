from figstyle import *
W,H=140,122
fig,ax=canvas(W,H)
DG='#2E6E4B'; DO='#8A4A17'
mx,mw=12,73; cxm=mx+mw/2
rxx,rw=96,40
def node(y,h,title,body,fc=WHITE,ec=BORDER,ls='-',lw=0.7,tcol=TEXT,x=mx,w=mw,tag=None):
    box(ax,x,y,w,h,fc=fc,ec=ec,ls=ls,lw=lw)
    if title:
        txt(ax,x+w/2,y+h-3.4,title,size=7.0,weight='bold',color=tcol)
        txt(ax,x+w/2,y+h-6.6,body,size=6.6,va='top',ls=1.15)
    else:
        txt(ax,x+w/2,y+h/2,body,size=6.8,ls=1.15)
    if tag:
        txt(ax,x+w-1.5,y+h+0.4,tag,size=5.8,color=SEC,ha='right',va='bottom',style='italic')
# rows
y1,h1=102,14; y2,h2=81,14; y3,h3=60,13; y4,h4=39,13; y5,h5=18,13
node(y1,h1,'Node LP at the current dual','RMP solved with the node rows (branching\nconstraints, active cuts); duals $\\pi$ to pricing')
node(y1,h1,'If the RMP is infeasible','Phase-I or Farkas pricing\nbefore any closure (Sect. 6.1)',x=rxx,w=rw)
node(y2,h2,'Discovery','Heuristic, learned or restricted pricing\nproposes candidate columns',ls=(0,(3,1.6)),ec=SEC)
node(y3,h3,None,'Is a proposed column legal at this node,\nwith verified negative reduced cost at $\\pi$?',fc=BLUE_L,ec='#9CC5EE',lw=0.8)
node(y3,h3,None,'Admit column(s);\nre-optimize the RMP',x=rxx,w=rw,fc=WHITE,ec=BORDER)
node(y4,h4,None,'Does a valid lower bound $\\geq 0$ (within tolerance)\ncover the full current domain of every block?',fc=BLUE_L,ec='#9CC5EE',lw=0.8)
node(y4,h4,'LP closure certified','Node bound valid;\nprune or branch',x=rxx,w=rw,fc=GREEN_L,ec=GREEN,lw=0.9,tcol=DG)
node(y5,h5,'Recovery (G2)','Restore the full current domain or call a\ncertifying oracle; its cost counts in the run')
node(y5,h5,'Interrupted or unchecked','Unresolved: keep the last valid\nbound, e.g. Eq. (3); no closure',x=rxx,w=rw,fc=ORANGE_L,ec=ORANGE,lw=0.9,tcol=DO)
# vertical arrows main
for (ya,yb,lab) in [(y1,y2+h2,''),(y2,y3+h3,''),(y3,y4+h4,'No'),(y4,y5+h5,'No')]:
    arrow(ax,(cxm,ya),(cxm,yb))
    if lab: txt(ax,cxm+1.6,(ya+yb)/2,lab,size=6.4,ha='left',color=SEC)
# yes arrows
for yy,lab,col in [(y3+h3/2,'Yes',LINE),(y4+h4/2,'Yes',GREEN)]:
    arrow(ax,(mx+mw,yy),(rxx,yy),color=col,lw=0.8 if col==LINE else 0.9)
    txt(ax,(mx+mw+rxx)/2,yy+1.4,lab,size=6.4,color=SEC,va='bottom')
# infeasible branch
arrow(ax,(mx+mw,y1+h1/2),(rxx,y1+h1/2),ls=(0,(3,1.6)),color=SEC)
# admit loop back to S1
xr=rxx+rw/2
poly_arrow(ax,[(xr,y3+h3),(xr,y1-3.5),(cxm+28,y1-3.5),(cxm+28,y1)])
txt(ax,xr+1.4,(y3+h3+y1-3.5)/2,'next\niteration',size=6.0,ha='left',color=SEC,ls=1.05)
# recovery loop back to S3 (left side)
xl=7.0
poly_arrow(ax,[(mx,y5+h5/2),(xl,y5+h5/2),(xl,y3+h3/2),(mx,y3+h3/2)])
txt(ax,xl-1.9,(y5+h5/2+y3+h3/2)/2,'columns or bounds returned',size=6.0,color=SEC,rotation=90)
# interrupted
arrow(ax,(mx+mw,y5+h5/2),(rxx,y5+h5/2),color=ORANGE,lw=0.9)
# legend
ly=6.5
items=[(dict(fc=WHITE,ec=SEC,ls=(0,(3,1.6)),lw=0.7),'may be heuristic or learned'),
       (dict(fc=BLUE_L,ec='#9CC5EE',ls='-',lw=0.8),'requires a valid check'),
       (dict(fc=GREEN_L,ec=GREEN,ls='-',lw=0.9),'certified outcome'),
       (dict(fc=ORANGE_L,ec=ORANGE,ls='-',lw=0.9),'unresolved outcome')]
for k,(st,lab) in enumerate(items):
    x=12+(k%2)*48; yy=9.5-(k//2)*5.2
    box(ax,x,yy-1.6,5.5,3.2,r=0.6,**st)
    txt(ax,x+7.5,yy,lab,size=6.2,ha='left',color=SEC)
save(fig,'Figure_2')
