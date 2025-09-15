import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D
import io
from PIL import Image

# ------------ Build Game Tree ------------
def build_tree():
    G = nx.DiGraph()
    roles = ["MAX", "MIN", "MAX", "MIN"]
    leaves = [3,4,2,1,7,8,9,10,2,11,1,12,14,9,13,16]

    def build(name, depth, idx=0):
        role, value = (roles[depth], None) if depth < 4 else ("LEAF", leaves[idx])
        G.add_node(name, depth=depth, role=role, value=value,
                   alpha=-float("inf"), beta=float("inf"),
                   pruned=False, visited=False)
        if depth == 4: 
            return idx + 1
        for i in [0, 1]:
            child = f"{name}{i}"
            G.add_edge(name, child, visited=False, pruned=False)
            idx = build(child, depth+1, idx)
        return idx

    build("N", 0)
    return G, "N"

# ------------ Layout ------------
def binary_pos(G, root, width=8):
    pos = {}
    def dfs(n, d, x, w):
        pos[n] = (x, -d)
        ch = list(G.successors(n))
        if ch: [dfs(ch[i], d+1, x+(-1)**i*w/2, w/2) for i in range(2)]
    dfs(root, 0, 0, width)
    return pos

# ------------ Mark pruned subtree ------------
def mark_subtree(G, node):
    G.nodes[node]["pruned"] = True
    for p in G.predecessors(node): 
        G.edges[p, node]["pruned"] = True
    [mark_subtree(G, c) for c in G.successors(node)]

def mark_pruned(G, parent, stop_child):
    kids = list(G.successors(parent))
    [mark_subtree(G, c) for c in kids[kids.index(stop_child)+1:]]

# ------------ Alpha-Beta with step-by-step visualization ------------
def alphabeta(G, node, alpha, beta, maximizing, pos, step_images, step_count=[0]):
    G.nodes[node]["visited"] = True
    G.nodes[node]["alpha"] = alpha
    G.nodes[node]["beta"] = beta
    
    # Generate step image
    step_count[0] += 1
    step_images.append(draw_step(G, pos, step_count[0], f"Visiting node {node}"))
    
    kids = list(G.successors(node))
    if not kids: 
        return G.nodes[node]["value"]

    val = -float("inf") if maximizing else float("inf")
    for c in kids:
        G.edges[node, c]["visited"] = True
        
        # Generate step image for edge visit
        step_count[0] += 1
        step_images.append(draw_step(G, pos, step_count[0], f"Exploring edge {node} -> {c}"))
        
        v = alphabeta(G, c, alpha, beta, not maximizing, pos, step_images, step_count)
        val = max(val, v) if maximizing else min(val, v)
        
        # Update alpha/beta
        if maximizing:
            alpha = max(alpha, val)
        else:
            beta = min(beta, val)
        
        G.nodes[node]["alpha"] = alpha
        G.nodes[node]["beta"] = beta
        
        # Generate step image for alpha/beta update
        step_count[0] += 1
        step_images.append(draw_step(G, pos, step_count[0], f"Updated {node}: α={alpha}, β={beta}"))
        
        if beta <= alpha: 
            mark_pruned(G, node, c)
            # Generate step image for pruning
            step_count[0] += 1
            step_images.append(draw_step(G, pos, step_count[0], f"Pruning at {node}: β({beta}) ≤ α({alpha})"))
            break
    
    G.nodes[node]["value"] = val
    return val

# ------------ Draw Step ------------
def draw_step(G, pos, step_num, description):
    fig, ax = plt.subplots(figsize=(14, 8))
    labels, node_colors = {}, []

    for n, nd in G.nodes(data=True):
        if nd['role'] == "LEAF":
            lbl = f"LEAF\n{nd['value']}"
        else:
            v = nd['value'] if nd['value'] is not None else "-"
            a = "∞" if nd['alpha'] == float("inf") else ("-∞" if nd['alpha'] == -float("inf") else nd['alpha'])
            b = "∞" if nd['beta'] == float("inf") else ("-∞" if nd['beta'] == -float("inf") else nd['beta'])
            lbl = f"{nd['role']}\nv={v}\nα={a}\nβ={b}"
        labels[n] = lbl

        # Coloring based on state
        if nd["pruned"]:
            node_colors.append("lightgrey")
        elif nd["visited"]:
            if nd["role"] == "MAX":
                node_colors.append("deepskyblue")
            elif nd["role"] == "MIN":
                node_colors.append("lightcoral")
            else:  # LEAF
                node_colors.append("gold")
        else:
            if nd["role"] == "MAX":
                node_colors.append("lightblue")
            elif nd["role"] == "MIN":
                node_colors.append("lightgreen")
            else:  # LEAF
                node_colors.append("orange")

    # Draw edges with different styles
    pe = [(u,v) for u,v,d in G.edges(data=True) if d.get("pruned")]
    ve = [(u,v) for u,v,d in G.edges(data=True) if d.get("visited") and not d.get("pruned")]
    oe = [(u,v) for u,v,d in G.edges(data=True) if not d.get("visited") and not d.get("pruned")]

    nx.draw_networkx_edges(G, pos, edgelist=oe, arrows=False, alpha=0.25, ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=ve, arrows=False, width=2, ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=pe, style='dashed', edge_color='red', arrows=False, width=2.0, ax=ax)
    nx.draw_networkx_nodes(G, pos, node_size=1600, node_color=node_colors, edgecolors='k', ax=ax)
    nx.draw_networkx_labels(G, pos, labels, font_size=8, font_weight="bold", ax=ax)

    # Legend
    handles = [
        Line2D([0],[0],color='k',lw=2,label='evaluated edge'),
        Line2D([0],[0],color='red',lw=2,ls='--',label='pruned edge'),
        Line2D([0],[0],marker='o',mfc='lightgrey',mec='k',ms=8,ls='None',label='pruned node'),
        Line2D([0],[0],marker='o',mfc='deepskyblue',mec='k',ms=8,ls='None',label='visited MAX'),
        Line2D([0],[0],marker='o',mfc='lightcoral',mec='k',ms=8,ls='None',label='visited MIN'),
        Line2D([0],[0],marker='o',mfc='gold',mec='k',ms=8,ls='None',label='visited LEAF')
    ]
    ax.legend(handles=handles, loc='upper right')
    ax.set_title(f"Alpha-Beta Pruning - Step {step_num}\n{description}", fontsize=12, weight='bold')
    ax.axis('off')
    
    # Convert to image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=100)
    buf.seek(0)
    img = Image.open(buf)
    plt.close(fig)
    return img

# ------------ Draw Final Tree ------------
def draw_final(G, pos, result):
    fig, ax = plt.subplots(figsize=(14, 8))
    labels, node_colors = {}, []

    for n, nd in G.nodes(data=True):
        if nd['role'] == "LEAF":
            lbl = f"LEAF\n{nd['value']}"
        else:
            v = nd['value'] if nd['value'] is not None else "-"
            a = "∞" if nd['alpha'] == float("inf") else ("-∞" if nd['alpha'] == -float("inf") else nd['alpha'])
            b = "∞" if nd['beta'] == float("inf") else ("-∞" if nd['beta'] == -float("inf") else nd['beta'])
            lbl = f"{nd['role']}\nv={v}\nα={a}\nβ={b}"
        labels[n] = lbl

        # Final coloring
        if nd["pruned"]:
            node_colors.append("lightgrey")
        elif nd["role"] == "MAX":
            node_colors.append("skyblue")
        elif nd["role"] == "MIN":
            node_colors.append("lightgreen")
        else:  # LEAF
            node_colors.append("orange")

    # Edges
    pe = [(u,v) for u,v,d in G.edges(data=True) if d.get("pruned")]
    ve = [(u,v) for u,v,d in G.edges(data=True) if d.get("visited") and not d.get("pruned")]
    oe = [(u,v) for u,v,d in G.edges(data=True) if not d.get("visited") and not d.get("pruned")]

    nx.draw_networkx_edges(G, pos, edgelist=oe, arrows=False, alpha=0.25, ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=ve, arrows=False, width=2, ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=pe, style='dashed', edge_color='red', arrows=False, width=2.0, ax=ax)
    nx.draw_networkx_nodes(G, pos, node_size=1600, node_color=node_colors, edgecolors='k', ax=ax)
    nx.draw_networkx_labels(G, pos, labels, font_size=8, font_weight="bold", ax=ax)

    handles = [
        Line2D([0],[0],color='k',lw=2,label='evaluated edge'),
        Line2D([0],[0],color='red',lw=2,ls='--',label='pruned edge'),
        Line2D([0],[0],marker='o',mfc='lightgrey',mec='k',ms=8,ls='None',label='pruned node'),
        Line2D([0],[0],marker='o',mfc='skyblue',mec='k',ms=8,ls='None',label='MAX node'),
        Line2D([0],[0],marker='o',mfc='lightgreen',mec='k',ms=8,ls='None',label='MIN node'),
        Line2D([0],[0],marker='o',mfc='orange',mec='k',ms=8,ls='None',label='LEAF node')
    ]
    ax.legend(handles=handles, loc='upper right')
    ax.set_title(f"Alpha-Beta Pruning - Final Result\nOptimal value at root = {result}", fontsize=14, weight='bold')
    ax.axis('off')
    
    # Convert to image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=100)
    buf.seek(0)
    img = Image.open(buf)
    plt.close(fig)
    return img

def combine_images(images):
    """Combine all step images into a single composite image"""
    if not images:
        return None
    
    # Filter out None images
    images = [img for img in images if img is not None]
    if not images:
        return None
    
    n_images = len(images)
    cols = min(4, n_images)  # Maximum 4 columns for better fit
    rows = (n_images + cols - 1) // cols
    
    max_width = max(img.width for img in images)
    max_height = max(img.height for img in images)
    
    combined_width = cols * max_width
    combined_height = rows * max_height
    combined_img = Image.new('RGB', (combined_width, combined_height), 'white')
    
    for i, img in enumerate(images):
        row = i // cols
        col = i % cols
        x = col * max_width + (max_width - img.width) // 2
        y = row * max_height + (max_height - img.height) // 2
        combined_img.paste(img, (x, y))
    
    return combined_img

# ------------ Main Execution ------------
if __name__ == "__main__":
    print("Alpha-Beta Pruning Algorithm - Step by Step Visualization\n")
    
    # Build the game tree
    print("Building game tree...")
    G, root = build_tree()
    pos = binary_pos(G, root, width=8)
    
    # Initialize step images list
    step_images = []
    
    print("Running Alpha-Beta Pruning algorithm...")
    print("This will generate step-by-step visualizations...\n")
    
    # Run alpha-beta algorithm with visualization
    result = alphabeta(G, root, -float("inf"), float("inf"), True, pos, step_images)
    
    # Generate final result image
    final_img = draw_final(G, pos, result)
    step_images.append(final_img)
    
    print(f"Algorithm completed!")
    print(f"Final optimal value: {result}")
    print(f"Generated {len(step_images)} visualization steps")
    
    # Combine all images into one
    combined_image = combine_images(step_images)
    
    if combined_image:
        # Display the combined image
        plt.figure(figsize=(20, 16))
        plt.imshow(combined_image)
        plt.axis('off')
        plt.title("Alpha-Beta Pruning Algorithm - All Steps Combined", fontsize=16, pad=20)
        plt.tight_layout()
        plt.show()
        
        # Save the combined image
        combined_image.save("alphabeta_pruning_combined.png")
        print(f"\nCombined image saved as 'alphabeta_pruning_combined.png'")
        
        # Print summary
        pruned_nodes = [n for n, d in G.nodes(data=True) if d.get("pruned")]
        pruned_edges = [(u,v) for u,v,d in G.edges(data=True) if d.get("pruned")]
        print(f"Nodes pruned: {len(pruned_nodes)}")
        print(f"Edges pruned: {len(pruned_edges)}")
    else:
        print("No images to combine")