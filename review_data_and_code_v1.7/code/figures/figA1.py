from figstyle import *
W,H=190,150
fig,ax=canvas(W,H)
HB='#DCEBF8'
def b(x,y,w,h,lines,fc=WHITE,ec=BORDER,lw=0.7,ls='-',bold_first=False,size=6.6,align='center'):
    box(ax,x,y,w,h,fc=fc,ec=ec,lw=lw,ls=ls,r=1.0)
    if align=='center':
        txt(ax,x+w/2,y+h/2,lines,size=size,ls=1.2)
    else:
        txt(ax,x+2.2,y+h/2,lines,size=size,ls=1.2,ha='left')
# columns
LM=(14,50); LX=(68,34); RM=(108,44); RX=(156,33)
# headers
box(ax,LM[0],136,LX[0]+LX[1]-LM[0],10,fc=HB,ec='none',r=1.0)
txt(ax,(LM[0]+LX[0]+LX[1])/2,141,'Logged Crossref discovery (11 October 2026)',size=7.2,weight='bold')
box(ax,RM[0],136,RX[0]+RX[1]-RM[0],10,fc='#ECEAE6',ec='none',r=1.0)
txt(ax,(RM[0]+RX[0]+RX[1])/2,141,'Author-assembled full-text frame',size=7.2,weight='bold')
# phase bands
for (y0,y1,lab) in [(112,134,'Identification'),(32,110,'Screening and eligibility'),(6,30,'Included')]:
    box(ax,2,y0,8,y1-y0,fc=HB,ec='none',r=1.0)
    txt(ax,6,(y0+y1)/2,lab,size=6.8,weight='bold',rotation=90,color=BLUE_D)
# Row 1
r1=(114,18)
b(LM[0],r1[0],LM[1],r1[1],'Records identified: n = 180\n(9 of 10 queries returned the first\n20 relevance-ranked records)')
b(LX[0],r1[0]+3,LX[1],r1[1]-6,'Duplicate DOI rows\nremoved: n = 10',align='left')
b(RM[0],r1[0],RM[1],r1[1],'Reports assembled for\nfull-text assessment: n = 101\n(100 study families)')
# Row 2
r2=(94,14)
b(LM[0],r2[0],LM[1],r2[1],'Distinct DOIs screened\nat title: n = 170')
b(LX[0],r2[0]-1,LX[1],r2[1]+2,'Excluded at title: n = 52\nAlready in the frame: n = 39',align='left')
# Row 3
r3=(70,18)
b(LM[0],r3[0],LM[1],r3[1],'Leads assessed at title and\navailable abstract: n = 79')
b(LX[0],r3[0]-3,LX[1],r3[1]+6,'Not selected for this\ncritical sample: n = 74\n(Supplementary Table S1)\nCG as RL action space: n = 1\nEarlier report of S018: n = 1',align='left',size=6.3)
# Row 4
r4=(48,14)
b(LM[0],r4[0],LM[1],r4[1],'Supplied and read in full,\nadded to the frame: n = 3\n(S102, S103, S104)')
b(RM[0],r4[0]-2,RM[1],r4[1]+4,'Reports assessed in full\ntext: n = 104 (103 families;\n1 linked erratum)')
b(RX[0],r4[0],RX[1],r4[1],'Adjacent surveys\nexcluded from method\ncoding: n = 4',align='left',size=6.3)
# Row 5
r5=(30,12)
# targeted update box
b(RX[0],r5[0]-2,RX[1],r5[1]+4,'Targeted search\n(14 Oct 2026): +1 core\nfamily (S105); +2 reports\nof included families',align='left',size=6.1)
b(RM[0],r5[0],RM[1],r5[1],'Families retained: n = 99\n(79 core, 8 supporting,\n12 background)')
# Included
b(RM[0],8,RX[0]+RX[1]-RM[0],18,'Study families included: n = 100\n80 core + 8 supporting families: 146 coded variants (Table A.1)\n12 background families (context only)',fc=BLUE_L,ec='#9CC5EE',lw=0.8,size=6.6)
# arrows
cxl=LM[0]+LM[1]/2; cxr=RM[0]+RM[1]/2
arrow(ax,(cxl,r1[0]),(cxl,r2[0]+r2[1]))
arrow(ax,(cxl,r2[0]),(cxl,r3[0]+r3[1]))
arrow(ax,(cxl,r3[0]),(cxl,r4[0]+r4[1]))
for yy in [r1[0]+r1[1]/2, r2[0]+r2[1]/2, r3[0]+r3[1]/2]:
    arrow(ax,(LM[0]+LM[1],yy),(LX[0],yy))
arrow(ax,(LM[0]+LM[1],r4[0]+r4[1]/2),(RM[0],r4[0]+r4[1]/2))
arrow(ax,(cxr,r1[0]),(cxr,r4[0]+r4[1]+2))
arrow(ax,(RM[0]+RM[1],r4[0]+r4[1]/2),(RX[0],r4[0]+r4[1]/2))
arrow(ax,(cxr,r4[0]-2),(cxr,r5[0]+r5[1]))
arrow(ax,(cxr,r5[0]),(cxr,26))
arrow(ax,(RX[0]+RX[1]/2,r5[0]-2),(RX[0]+RX[1]/2,26))
# note box for non-recoverable quantities (within screening band, lower-left)
b(LM[0],33.5,LX[0]+LX[1]-LM[0],11.5,'Not recorded and therefore not reported: whole-web hit counts, cross-source\nduplicates and a global title-screening denominator across all sources.\nThe sample is targeted and critical, not an exhaustive census.',fc=PANEL,ec=BORDER,ls=(0,(3,2)),align='left',size=6.2)
save(fig,'Figure_A1')
