from figstyle import *
import numpy as np, pandas as pd
from matplotlib.colors import LinearSegmentedColormap
import os
df=pd.read_csv(os.environ.get('VARIANTS','data/variants_v1_6.csv'),keep_default_na=False)
df['typ']=df.method_type.map({'TRADITIONAL':'T','LEARNING_GUIDED':'ML'})
df['Gp']=df.primary_mechanism.replace({'GU-offline':'GU'})
df['Elist']=df.scopes.apply(lambda s: [x for x in s.split('|') if x])
Gs=['G1','G2','G3','G4','G5','GU']; Es=['E0','E1','E2','E3','E4']
Glab=['G1  Order preserved','G2  Recovery restores domain','G3  Safe elimination','G4  Valid relaxation or bound','G5  Explicitly heuristic','GU  Unassigned']
Elab=['E0\nOffline','E1\nPricing','E2\nCG/root','E3\nPartial\ntree','E4\nComplete\ntree']
def mats(sub):
    M=np.array([[sum(e in l for l in sub[sub.Gp==g].Elist) for e in Es] for g in Gs])
    V=np.array([len(sub[sub.Gp==g]) for g in Gs])
    noE=np.array([sum(len(l)==0 for l in sub[sub.Gp==g].Elist) for g in Gs])
    return M,V,noE
T=mats(df[df.typ=='T']); L=mats(df[df.typ=='ML']); A=mats(df)
assert T[1].sum()==72 and L[1].sum()==74 and A[0].sum()==239 and A[1].sum()==146
cmap=LinearSegmentedColormap.from_list('b',['#EEF5FC','#CBE1F5','#8EBDEA','#3F8DD6','#1A5A9B'])
vmax=max(T[0].max(),L[0].max())
W,H=190,84
fig,ax=canvas(W,H)
cw,ch,gap=9.4,6.6,1.6
gy=14; rows=6
def ry(i): return gy+(rows-1-i)*ch+(0 if i==5 else gap)
top=ry(0)+ch
BAR='#A9BCCD'
for i,lab in enumerate(Glab):
    txt(ax,36.5,ry(i)+ch/2,lab,size=6.8,ha='right',color=TEXT if i<5 else SEC)
def panel(gx,M,V,noE,title,memb):
    for i,g in enumerate(Gs):
        for j,e in enumerate(Es):
            v=M[i,j]; c=cmap(v/vmax) if v>0 else '#FFFFFF'
            ax.add_patch(Rectangle((gx+j*cw,ry(i)),cw,ch,fc=c,ec='white',lw=0.9,zorder=2))
            dark=v/vmax>0.5
            txt(ax,gx+j*cw+cw/2,ry(i)+ch/2,str(v),size=7 if v else 6.4,
                color=('white' if dark else TEXT) if v else '#C4C0BA',weight='bold' if dark else 'normal')
    ax.add_patch(Rectangle((gx,gy),5*cw,top-gy,fc='none',ec='#D9D6D1',lw=0.5,zorder=1))
    ax.plot([gx,gx+5*cw],[ry(5)+ch+gap/2]*2,color=SEC,lw=0.5,ls=(0,(2,1.5)),zorder=3)
    for j,lab in enumerate(Elab):
        txt(ax,gx+j*cw+cw/2,gy-1.0,lab,size=6.2,va='top',color=TEXT,ls=1.05)
    mb=M.sum(0); bmax=64; bh=11
    base=top+1.8
    for j in range(5):
        h=bh*mb[j]/bmax
        ax.add_patch(Rectangle((gx+j*cw+1.7,base),cw-3.4,h,fc=BAR,ec='none',zorder=2))
        txt(ax,gx+j*cw+cw/2,base+h+1.1,str(mb[j]),size=6.3,color=TEXT)
    ax.plot([gx,gx+5*cw],[base,base],color=SEC,lw=0.5,zorder=3)
    txt(ax,gx,base+bh+5.4,f'Scope memberships, n = {memb}',size=6.2,ha='left',color=SEC)
    rx=gx+5*cw+2.2; rmax=30; rw=12
    for i in range(6):
        w=rw*V[i]/rmax
        ax.add_patch(Rectangle((rx,ry(i)+1.5),max(w,0.25),ch-3.0,fc=BAR if i<5 else '#D6D3CE',ec='none',zorder=2))
        lab=str(V[i])+('*' if noE[i] else '')
        txt(ax,rx+w+0.9,ry(i)+ch/2,lab,size=6.3,ha='left',color=TEXT)
    ax.plot([rx,rx],[gy,top],color=SEC,lw=0.5,zorder=3)
    txt(ax,rx,top+1.2,'Variants',size=6.2,ha='left',va='bottom',color=SEC)
    txt(ax,gx-0.3,H-2.2,title,size=7.8,weight='bold',ha='left',va='top')
panel(39,*T,'(a) Traditional variants, n = 72',T[0].sum())
panel(117,*L,'(b) Learning-guided variants, n = 74',L[0].sum())
# colour key
kx,ky=6,top+7.5
txt(ax,kx,ky+4.2,'Shading: scope memberships',size=6.0,ha='left',color=SEC)
for k,v in enumerate([1,5,10,15,20,26]):
    ax.add_patch(Rectangle((kx+k*4.4,ky-1.4),4.4,2.8,fc=cmap(v/vmax),ec='white',lw=0.5))
    txt(ax,kx+k*4.4+2.2,ky-2.4,str(v),size=5.6,color=SEC,va='top')
save(fig,'Figure_3')
print(T[0].sum(),L[0].sum(),vmax)
