"""
Algorithm K-Mean-Clustering
input - dataset D with n no of tuples
output - k no of clusters

BEGIN
    Arbitrarily choose K objects from D as initial cluster means
    repeat
        Assign each tuple in D to its closest cluster
            (distance = |x - mean_of_cluster|)
        Update the cluster means i.e. calculate the mean of each cluster
    until no change in cluster assignment
END

Dry Run:
Let D = {5, 12, 7, 4, 3, 11, 19, 25, 13, 14}
Here K = 2 (two clusters)
Let initial centroids be C1 = 5, C2 = 12

Iteration 1:
D    DC1   DC2   Cluster
5    0     7     C1
12   7     0     C2
7    2     5     C1
4    1     8     C1
3    2     9     C1
11   6     1     C2
19   14    7     C2
25   20    13    C2
13   8     1     C2
14   9     2     C2

C1 = {5, 7, 4, 3} → mean = (5+7+4+3)/4 = 4.75
C2 = {12, 11, 19, 25, 13, 14} → mean = (12+11+19+25+13+14)/6 = 15.67

Iteration 2:
D    DC1     DC2     Cluster
5    0.25    10.67   C1
12   7.25    3.67    C2
7    2.25    8.67    C1
4    0.75    11.67   C1
3    1.75    12.67   C1
11   6.25    4.67    C2
19   14.25   3.33    C2
25   20.25   9.33    C2
13   8.25    2.67    C2
14   9.25    1.67    C2

C1 = {5, 7, 4, 3} → mean = 4.75  (no change)
C2 = {12, 11, 19, 25, 13, 14} → mean = 15.67 (no change)

Since there is no change in clusters → STOP

Final Clusters:
C1 = {5, 7, 4, 3}
C2 = {12, 11, 19, 25, 13, 14}
"""
import matplotlib.pyplot as plt,networkx as nx,math,random,numpy as np
def p(s):return [float(x) for x in s.strip().split()]
def i(d,k,c=None):
    if c:return [float(x) for x in c]
    u=[];[u.append(x) for x in d if x not in u];[u.append(random.choice(d)) for _ in range(k-len(u))];return [float(x) for x in u[:k]]
def a(d,c):
    r=[];dist=[];[r.append(min(range(len(c)),key=lambda i:abs(x-c[i]))) or dist.append([abs(x-v) for v in c]) for x in d];return r,dist
def u(d,r,k,o):
    return [sum([x for x,a in zip(d,r) if a==j])/len([x for x,a in zip(d,r) if a==j]) if [x for x,a in zip(d,r) if a==j] else o[j] for j in range(k)]
def kmeans(d,k,c0=None,m=100,tol=1e-6):
    c=i(d,k,c0);h=[]
    for it in range(1,m+1):
        r,dist=a(d,c);n=u(d,r,k,c)
        h.append({"iter":it,"c":c[:],"r":r[:],"dist":dist[:]})
        if n==c or all(abs(nc-cx)<=tol for nc,cx in zip(n,c)):c=n;break
        c=n
    r,dist=a(d,c)
    h.append({"iter":len(h)+1,"c":c[:],"r":r[:],"dist":dist[:]})
    return h
def v(d,h):
    n=len(h);cols=2 if n>1 else 1;rows=math.ceil(n/cols);fig,ax=plt.subplots(rows,cols,figsize=(cols*10,rows*6));ax=ax.flatten() if hasattr(ax,"flatten") else [ax]
    cc=['#FFE5E5','#E5FFE5','#E5E5FF','#FFFFE5','#FFE5FF','#E5FFFF'];ec=['#FF6B6B','#4ECDC4','#45B7D1','#96CEB4','#FFEAA7','#DDA0DD']
    for idx,snap in enumerate(h):
        a0=ax[idx];c=snap["c"];r=snap["r"];dist=snap["dist"];k=len(c);G=nx.DiGraph()
        p_nodes=[f"p{i}" for i in range(len(d))];c_nodes=[f"C{j}" for j in range(k)]
        [G.add_node(nm) for nm in p_nodes+c_nodes];el={};[G.add_edge(p_nodes[i],c_nodes[r[i]]) or el.update({(p_nodes[i],c_nodes[r[i]]):f"{dist[i][r[i]]:.2f}"}) for i in range(len(d))]
        pos={};srt=sorted(range(len(d)),key=lambda i:d[i]);used=set();rng=max(d)-min(d) if max(d)!=min(d) else 10
        for ii,idx2 in enumerate(srt):
            x=d[idx2];o=0;step=max(1,rng/max(8,len(d)))/2
            while any(abs(x+o-u)<step*2 for u in used):o=-o+step if o<=0 else -o
            pos[p_nodes[idx2]]=(x+o,0);used.add(x+o)
        for j,ccen in enumerate(c):pos[c_nodes[j]]=(ccen,2)
        a0.set_facecolor('#F8F9FA')
        nx.draw_networkx_nodes(G,pos,nodelist=p_nodes,node_color=[cc[r[i]%len(cc)] for i in range(len(d))],edgecolors=[ec[r[i]%len(ec)] for i in range(len(d))],linewidths=2,node_size=800,ax=a0)
        nx.draw_networkx_nodes(G,pos,nodelist=c_nodes,node_color=[cc[j%len(cc)] for j in range(k)],edgecolors=[ec[j%len(ec)] for j in range(k)],linewidths=3,node_shape='s',node_size=1200,ax=a0)
        nx.draw_networkx_labels(G,pos,{**{p_nodes[i]:f"{d[i]:.1f}" for i in range(len(d))},**{c_nodes[j]:f"C{j}\n{c[j]:.2f}" for j in range(k)}},font_size=10,font_weight='bold',font_color='black',ax=a0)
        nx.draw_networkx_edges(G,pos,edgelist=list(G.edges()),edge_color=[ec[r[int(e[0][1:])%len(ec)] for e in G.edges()],arrows=False,width=2,alpha=0.7,ax=a0)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=el,font_size=9,font_weight='bold',bbox=dict(boxstyle="round,pad=0.1",facecolor='white',edgecolor='gray',alpha=0.8),ax=a0)
        a0.set_title(f"K-means Step {snap['iter']}\nCentroids: {', '.join(f'{x:.2f}' for x in c)}",fontsize=14,fontweight='bold',pad=20)
        xvals=[pos[p][0] for p in p_nodes];xr=max(xvals)-min(xvals) if max(xvals)!=min(xvals) else 2;a0.set_xlim(min(xvals)-0.3*xr,max(xvals)+0.3*xr);a0.set_ylim(-0.7,2.7);a0.set_yticks([]);a0.grid(True,alpha=0.3,linestyle='--');a0.set_xlabel('Data Values (spread to avoid overlap)',fontweight='bold',fontsize=11);[sp.set_edgecolor('#CCCCCC');sp.set_linewidth(1.5) for sp in a0.spines.values()]
    for j in range(len(h),len(ax)):fig.delaxes(ax[j])
    plt.tight_layout(pad=2);plt.show()
if __name__=="__main__":
    print("K-means (1-D) with improved step-by-step visualization\n")
    d=p(input("Enter data points (space separated, e.g. '5 12 7 4 3 11 19 25 13 14'): "))
    if len(d)==0:raise SystemExit("No data provided.")
    k=int(input("Enter number of clusters k (e.g. 2): "))
    init=input(f"Enter {k} initial centroids (space separated) or press Enter to auto-pick: ").strip();c0=None
    if init:c0s=init.split();c0=[float(x) for x in c0s] if len(c0s)==k else None
    h=kmeans(d,k,c0)
    print("\nK-means Iterations (text):")
    for s in h:
        it=s["iter"];c=s["c"];r=s["r"];clusters={j:[] for j in range(len(c))}
        [clusters[a].append(x) for x,a in zip(d,r)]
        print(f"\nStep {it}: centroids = {[round(x,4) for x in c]}")
        for j in sorted(clusters.keys()):print(f"  C{j} = {clusters[j]}")
    v(d,h)
