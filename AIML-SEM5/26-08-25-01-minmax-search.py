import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

def sp(n): return [(i, n-i) for i in range(1, n//2+1) if i != n-i]
def ch(st):
    r=[]
    for i,p in enumerate(st):
        if p>2:
            for s in sp(p):
                ns=list(st[:i]+st[i+1:]);ns.extend(s);ns.sort(reverse=True)
                r.append(tuple(ns))
    return r
def term(st): return all(p<=2 for p in st)
def util(st): return 1 if len(st)%2 else -1
def mm(st,maxp,m={}):
    if st in m: return m[st]
    if term(st): m[st]=util(st);return m[st]
    c=ch(st);m[st]=(max(mm(x,0,m) for x in c) if maxp else min(mm(x,1,m) for x in c));return m[st]

def hpos(G,r,w=1.,vg=0.4,vl=0,xc=0.5,pos=None,p=None):
    pos={r:(xc,vl)} if pos is None else {**pos,**{r:(xc,vl)}}
    n=list(G.successors(r))
    if n:
        dx=w/len(n);nx=xc-w/2-dx/2
        for v in n: nx+=dx;pos=hpos(G,v,w=dx,vg=vg,vl=vl-vg,xc=nx,pos=pos,p=r)
    return pos

def steps(st):
    G=nx.DiGraph();q=deque([(st,1)]);vis=set();val={};mm(st,1,val);res=[];lvl=0
    while q:
        sz=len(q);ex=[];ed=[]
        for _ in range(sz):
            s,mx=q.popleft()
            if s in vis: continue
            vis.add(s)
            for c in ch(s):
                G.add_edge(str(s),str(c));q.append((c,not mx));ed.append((str(s),str(c)))
            ex.append(s)
        if not ex: break
        lab={n:f"{n}\nVal={val[eval(n)]}" for n in G.nodes()}
        pos=hpos(G,str(st))
        col=[("gold" if node in [str(x) for x in ex] else "lightgreen" if val[eval(node)]==1 else "lightcoral" if val[eval(node)]==-1 else "lightblue") for node in G.nodes()]
        res.append((lvl,ex,dict(G.edges()),dict(pos),dict(lab),col,(lvl%2==0)));lvl+=1
    return res

def show(res):
    n=len(res);c=2;r=(n+1)//c
    fig,ax=plt.subplots(r,c,figsize=(14,r*5));ax=ax.flatten()
    for i,(lvl,ex,ed,pos,lab,col,ismax) in enumerate(res):
        G=nx.DiGraph();G.add_edges_from(ed)
        nx.draw(G,pos,labels=lab,node_size=700,node_color=col,font_size=6,ax=ax[i],arrows=True)
        ax[i].set_title(f"Step {i+1}: Expand Level {lvl}\nExpanded: {', '.join(map(str,ex))}",fontsize=10,fontweight="bold")
        ax[i].axis("off")
        ax[i].text(-0.15,0.5,f"{'MAX' if ismax else 'MIN'}'s Turn",transform=ax[i].transAxes,fontsize=9,fontweight="bold",va="center",ha="right",color="blue")
    for j in range(i+1,len(ax)): ax[j].axis("off")
    plt.tight_layout();plt.show()

if __name__=="__main__":
    n=int(input("Enter the starting pile size: "))
    show(steps((n,)))
