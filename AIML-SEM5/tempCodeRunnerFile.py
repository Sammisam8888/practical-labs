import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import heapq
import io
from PIL import Image
import numpy as np

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
    G.add_node(st); d=0
    
    # List to store all generated images
    step_images = []
    
    step_images.append(draw(G,prev,st,gl,gsc,d,st)); d+=1

    while not pq.empty():
        cur=pq.get()
        if cur==gl: 
            step_images.append(draw(G,prev,st,gl,gsc,d,cur))
            break
        for ch in nxt_states(cur,lvl):
            t=gsc[cur]+1
            if ch not in gsc or t<gsc[ch]:
                gsc[ch]=t; f=t+h(ch,gl); prev[ch]=cur
                pq.put(ch,f); G.add_edge(cur,ch,weight=t)
        step_images.append(draw(G,prev,st,gl,gsc,d,cur)); d+=1
    
    # Generate final image
    final_img = final(G,prev,st,gl,gsc)
    step_images.append(final_img)
    
    return G,prev,gsc,step_images

def draw(G,prev,st,gl,gsc,d,cur):
    pos=graphviz_layout(G,prog='dot'); 
    fig, ax = plt.subplots(figsize=(10,7))
    lbls={n:f"{n}\nh={h(n,gl)}" for n in G.nodes()}
    nx.draw(G,pos,labels=lbls,with_labels=True,node_color='lightyellow',node_size=700,font_size=8,ax=ax)
    nx.draw_networkx_edge_labels(G,pos,edge_labels={(u,v):gsc[v] for u,v in G.edges()},font_size=7,ax=ax)

    if cur in prev:
        p=[]; t=cur
        while t is not None: p.append(t); t=prev[t]
        p.reverse(); e=[(p[i],p[i+1]) for i in range(len(p)-1)]
        nx.draw_networkx_edges(G,pos,edgelist=e,edge_color='green',width=3,ax=ax)

    nx.draw_networkx_nodes(G,pos,nodelist=[st],node_color='lightblue',node_size=800,ax=ax)
    if gl in G.nodes(): nx.draw_networkx_nodes(G,pos,nodelist=[gl],node_color='lightcoral',node_size=800,ax=ax)
    ax.set_title(f"A* Search - Step {d}")
    
    # Convert plot to image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=100)
    buf.seek(0)
    img = Image.open(buf)
    plt.close()
    return img

def final(G,prev,st,gl,gsc):
    pos=graphviz_layout(G,prog='dot'); 
    fig, ax = plt.subplots(figsize=(12,9))
    lbls={n:f"{n}\nh={h(n,gl)}" for n in G.nodes()}
    nx.draw(G,pos,labels=lbls,with_labels=True,node_color='orange',node_size=700,font_size=8,ax=ax)
    nx.draw_networkx_edge_labels(G,pos,edge_labels={(u,v):gsc[v] for u,v in G.edges()},font_size=7,ax=ax)

    if gl in prev:
        p=[]; t=gl
        while t is not None: p.append(t); t=prev[t]
        p.reverse(); e=[(p[i],p[i+1]) for i in range(len(p)-1)]
        nx.draw_networkx_edges(G,pos,edgelist=e,edge_color='green',width=3,ax=ax)
        print("Final Path:", " -> ".join(map(str,p)))

    nx.draw_networkx_nodes(G,pos,nodelist=[st],node_color='lightblue',node_size=800,ax=ax)
    if gl in G.nodes(): nx.draw_networkx_nodes(G,pos,nodelist=[gl],node_color='lightcoral',node_size=800,ax=ax)
    ax.set_title("Final A* Path")
    
    # Convert plot to image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=100)
    buf.seek(0)
    img = Image.open(buf)
    plt.close()
    return img

def combine_images(images):
    """Combine all step images into a single composite image"""
    if not images:
        return None
    
    # Calculate grid dimensions
    n_images = len(images)
    cols = min(3, n_images)  # Maximum 3 columns
    rows = (n_images + cols - 1) // cols
    
    # Get maximum dimensions
    max_width = max(img.width for img in images)
    max_height = max(img.height for img in images)
    
    # Create combined image
    combined_width = cols * max_width
    combined_height = rows * max_height
    combined_img = Image.new('RGB', (combined_width, combined_height), 'white')
    
    # Paste images
    for i, img in enumerate(images):
        row = i // cols
        col = i % cols
        x = col * max_width
        y = row * max_height
        
        # Center the image in its allocated space
        x_offset = (max_width - img.width) // 2
        y_offset = (max_height - img.height) // 2
        
        combined_img.paste(img, (x + x_offset, y + y_offset))
    
    return combined_img

if __name__=="__main__":
    print("Water Jug Problem - A* Search\n")
    a=int(input("Enter level of water in Jug 1: "))
    b=int(input("Enter level of water in Jug 2: "))
    print("Enter start state (x,y):"); st=tuple(map(int,input().split(",")))
    print("Enter goal state (x,y):"); gl=tuple(map(int,input().split(",")))
    
    G,prev,gsc,step_images=astar(st,gl,(a,b))
    
    # Combine all images into one
    combined_image = combine_images(step_images)
    
    if combined_image:
        # Display the combined image
        plt.figure(figsize=(20, 15))
        plt.imshow(combined_image)
        plt.axis('off')
        plt.title("A* Search Algorithm - All Steps Combined", fontsize=16, pad=20)
        plt.tight_layout()
        plt.show()
        
        # Optionally save the combined image
        combined_image.save("astar_water_jug_combined.png")
        print("\nCombined image saved as 'astar_water_jug_combined.png'")
    else:
        print("No images to combine")