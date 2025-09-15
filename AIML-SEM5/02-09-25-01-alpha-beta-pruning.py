"""
Algorithm Alpha Beta Pruning :



Dry Run :


"""

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D

def bt():
    G=nx.DiGraph();rl=["MAX","MIN","MAX","MIN"];lv=[3,4,2,1,7,8,9,10,2,11,1,12,14,9,13,16]
    def b(n,d,i=0):
        r,v=(rl[d],None) if d<4 else("LEAF",lv[i])
        G.add_node(n,depth=d,role=r,value=v,alpha=-float("inf"),beta=float("inf"),pruned=False)
        if d==4:return i+1
        for k in[0,1]:G.add_edge(n,n+str(k));i=b(n+str(k),d+1,i)
        return i
    b("N",0);return G,"N"

def bpos(G,r,w=8):
    p={}
    def dfs(n,d,x,h):
        p[n]=(x,-d);ch=list(G.successors(n))
        if ch:[dfs(ch[i],d+1,x+(-1)**i*h/2,h/2)for i in[0,1]]
    dfs(r,0,0,w);return p

def msb(G,n):G.nodes[n]["pruned"]=True;[G.edges[p,n].update(pruned=True)for p in G.predecessors(n)];[msb(G,c)for c in G.successors(n)]
def mpr(G,p,sc):kids=list(G.successors(p));[msb(G,c)for c in kids[kids.index(sc)+1:]]

def ab(G,n,a,b,mx):
    G.nodes[n]["visited"]=True;ch=list(G.successors(n))
    if not ch:return G.nodes[n]["value"]
    v=-float("inf")if mx else float("inf")
    for c in ch:
        G.edges[n,c]["visited"]=True;val=ab(G,c,a,b,not mx)
        v=max(v,val)if mx else min(v,val)
        a,b=(max(a,v),b)if mx else(a,min(b,v))
        if b<=a: mpr(G,n,c);break
    G.nodes[n].update({"value":v,"alpha":a,"beta":b});return v

def draw(G,p,res):
    plt.figure(figsize=(14,7));lbls={};cols=[]
    for n,d in G.nodes(data=True):
        if d["role"]=="LEAF":lbl=f"LEAF\n{d['value']}"
        else:
            v=d["value"] if d["value"]is not None else"-"
            a="∞"if d["alpha"]==float("inf")else("-∞"if d["alpha"]==-float("inf")else d["alpha"])
            b="∞"if d["beta"]==float("inf")else("-∞"if d["beta"]==-float("inf")else d["beta"])
            lbl=f"{d['role']}\nv={v}\nα={a}\nβ={b}"
        lbls[n]=lbl
        cols.append("lightpink" if d["pruned"] else "lightyellow" if d["role"]=="MAX" else "lightblue" if d["role"]=="MIN" else "gold")
    pe=[(u,v)for u,v,d in G.edges(data=True)if d.get("pruned")]
    ve=[(u,v)for u,v,d in G.edges(data=True)if d.get("visited")and not d.get("pruned")]
    oe=[(u,v)for u,v,d in G.edges(data=True)if not d.get("visited")and not d.get("pruned")]
    nx.draw_networkx_edges(G,p,edgelist=oe,arrows=False,alpha=0.25)
    nx.draw_networkx_edges(G,p,edgelist=ve,arrows=False,width=2)
    nx.draw_networkx_edges(G,p,edgelist=pe,style="dashed",edge_color="red",arrows=False,width=2)
    nx.draw_networkx_nodes(G,p,node_size=1600,node_color=cols,edgecolors="k")
    nx.draw_networkx_labels(G,p,lbls,font_size=8,font_weight="bold")
    h=[Line2D([0],[0],color='k',lw=2,label='evaluated edge'),
       Line2D([0],[0],color='red',lw=2,ls='--',label='pruned edge'),
       Line2D([0],[0],marker='o',mfc='lightpink',mec='k',ms=8,ls='None',label='pruned node'),
       Line2D([0],[0],marker='o',mfc='lightyellow',mec='k',ms=8,ls='None',label='MAX node'),
       Line2D([0],[0],marker='o',mfc='lightblue',mec='k',ms=8,ls='None',label='MIN node'),
       Line2D([0],[0],marker='o',mfc='gold',mec='k',ms=8,ls='None',label='LEAF node')]
    plt.legend(handles=h,loc='upper right')
    plt.title(f"Alpha-Beta Pruning\nFinal value at root = {res}",fontsize=14,weight="bold")
    plt.axis("off");plt.show()

if __name__=="__main__":
    n=int(input("Enter value of root : "))
    G,r=bt();p=bpos(G,r,8);res=ab(G,r,-float("inf"),float("inf"),1)
    draw(G,p,res);print("Final optimal value:",res)
