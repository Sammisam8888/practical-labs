import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import heapq

class PQ:
    def __init__(s): s.q=[]
    def empty(s): return not s.q
    def put(s,i,p): heapq.heappush(s.q,(p,i))
    def get(s): return heapq.heappop(s.q)[1]

def nxt_states(st,lvl):
    x,y=st; a,b=lvl
    ns=[(a,y),(x,b),(0,y),(x,0)]
    m=min(x,b-y); ns.append((x-m,y+m))
    m=min(y,a-x); ns.append((x+m,y-m))
    return list(set(ns))

def h(st,gl): return abs(st[0]-gl[0])+abs(st[1]-gl[1])

def astar(st,gl,lvl):
    pq=PQ(); pq.put(st,0)
    gsc={st:0}; prev={st:None}; G=nx.DiGraph()
    G.add_node(st); d=0; draw(G,prev,st,gl,gsc,d,st); d+=1

    while not pq.empty():
        cur=pq.get()
        if cur==gl: draw(G,prev,st,gl,gsc,d,cur); break
        for ch in nxt_states(cur,lvl):
            t=gsc[cur]+1
            if ch not in gsc or t<gsc[ch]:
                gsc[ch]=t; f=t+h(ch,gl); prev[ch]=cur
                pq.put(ch,f); G.add_edge(cur,ch,weight=t)
        draw(G,prev,st,gl,gsc,d,cur); d+=1
    return G,prev,gsc

def draw(G,prev,st,gl,gsc,d,cur):
    pos=graphviz_layout(G,prog='dot'); plt.figure(figsize=(10,7))
    lbls={n:f"{n}\nh={h(n,gl)}" for n in G.nodes()}
    nx.draw(G,pos,labels=lbls,with_labels=True,node_color='lightyellow',node_size=700,font_size=8)
    nx.draw_networkx_edge_labels(G,pos,edge_labels={(u,v):gsc[v] for u,v in G.edges()},font_size=7)

    if cur in prev:
        p=[]; t=cur
        while t is not None: p.append(t); t=prev[t]
        p.reverse(); e=[(p[i],p[i+1]) for i in range(len(p)-1)]
        nx.draw_networkx_edges(G,pos,edgelist=e,edge_color='green',width=3)

    nx.draw_networkx_nodes(G,pos,nodelist=[st],node_color='lightblue',node_size=800)
    if gl in G.nodes(): nx.draw_networkx_nodes(G,pos,nodelist=[gl],node_color='lightcoral',node_size=800)
    plt.title(f"A* Search - Depth {d}"); plt.show()

def final(G,prev,st,gl,gsc):
    pos=graphviz_layout(G,prog='dot'); plt.figure(figsize=(12,9))
    lbls={n:f"{n}\nh={h(n,gl)}" for n in G.nodes()}
    nx.draw(G,pos,labels=lbls,with_labels=True,node_color='orange',node_size=700,font_size=8)
    nx.draw_networkx_edge_labels(G,pos,edge_labels={(u,v):gsc[v] for u,v in G.edges()},font_size=7)

    if gl in prev:
        p=[]; t=gl
        while t is not None: p.append(t); t=prev[t]
        p.reverse(); e=[(p[i],p[i+1]) for i in range(len(p)-1)]
        nx.draw_networkx_edges(G,pos,edgelist=e,edge_color='green',width=3)
        print("Final Path:", " -> ".join(map(str,p)))

    nx.draw_networkx_nodes(G,pos,nodelist=[st],node_color='lightblue',node_size=800)
    if gl in G.nodes(): nx.draw_networkx_nodes(G,pos,nodelist=[gl],node_color='lightcoral',node_size=800)
    plt.title("Final A* Path"); plt.show()

if __name__=="__main__":
    print("Water Jug Problem - A* Search\n")
    a=int(input("Enter level of water in Jug 1: "))
    b=int(input("Enter level of water in Jug 2: "))
    print("Enter start state (x,y):"); st=tuple(map(int,input().split(",")))
    print("Enter goal state (x,y):"); gl=tuple(map(int,input().split(",")))
    G,prev,gsc=astar(st,gl,(a,b)); final(G,prev,st,gl,gsc)
