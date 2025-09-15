# kmeans_visual_steps_improved.py
import math
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def parse_input_points(s):
    try:
        parts = s.strip().split()
        return [float(p) for p in parts]
    except:
        raise ValueError("Enter space separated numeric values for data points.")

def initialize_centroids(data, k, provided=None):
    if provided:
        if len(provided) != k:
            raise ValueError("Number of provided centroids must equal k.")
        return [float(c) for c in provided]
    # default: choose first k distinct values (or random if not enough)
    uniq = []
    for x in data:
        if x not in uniq:
            uniq.append(x)
            if len(uniq) == k:
                break
    if len(uniq) < k:
        # fallback: extend by random picks
        import random
        while len(uniq) < k:
            uniq.append(random.choice(data))
    return [float(x) for x in uniq[:k]]

def assign_points(data, centroids):
    assignments = []
    distances = []
    for x in data:
        dists = [abs(x - c) for c in centroids]
        cluster = int(min(range(len(dists)), key=lambda i: dists[i]))
        assignments.append(cluster)
        distances.append(dists)
    return assignments, distances

def update_centroids(data, assignments, k, old_centroids):
    new_centroids = []
    for j in range(k):
        cluster_points = [x for x, a in zip(data, assignments) if a == j]
        if cluster_points:
            new_centroids.append(sum(cluster_points) / len(cluster_points))
        else:
            # empty cluster: keep old centroid (common strategy) 
            new_centroids.append(old_centroids[j])
    return new_centroids

def kmeans_1d(data, k, init_centroids=None, max_iter=100, tol=1e-6):
    centroids = initialize_centroids(data, k, init_centroids)
    history = []
    for it in range(1, max_iter+1):
        assignments, distances = assign_points(data, centroids)
        new_centroids = update_centroids(data, assignments, k, centroids)

        # record iteration snapshot
        snapshot = {
            "iter": it,
            "centroids": centroids[:],
            "assignments": assignments[:],
            "distances": distances[:]  # list of lists
        }
        history.append(snapshot)

        # check convergence: assignments stable OR centroids moved little
        if new_centroids == centroids:
            break
        if all(abs(nc - c) <= tol for nc, c in zip(new_centroids, centroids)):
            centroids = new_centroids
            break
        centroids = new_centroids

    # final snapshot of converged centroids (optional print)
    final_assignments, final_distances = assign_points(data, centroids)
    history.append({
        "iter": len(history)+1,
        "centroids": centroids[:],
        "assignments": final_assignments[:],
        "distances": final_distances[:]
    })
    return history

# ---------- Improved Visualization helper ----------
def draw_kmeans_history(data, history, filename="kmeans_steps_improved.png"):
    n_steps = len(history)
    # layout grid
    cols = 2 if n_steps > 1 else 1
    rows = math.ceil(n_steps / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(cols*10, rows*6))
    if not isinstance(axes, (list, tuple, np.ndarray)):
        axes = [axes]
    axes = (axes.flatten() if hasattr(axes, "flatten") else axes)

    # Improved color schemes with better visibility
    cluster_colors = ['#FFE5E5', '#E5FFE5', '#E5E5FF', '#FFFFE5', '#FFE5FF', '#E5FFFF']  # Light pastel colors
    edge_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']    # Darker edge colors
    
    for idx, snap in enumerate(history):
        ax = axes[idx]
        centroids = snap["centroids"]
        assignments = snap["assignments"]
        distances = snap["distances"]
        k = len(centroids)

        # Build networkx graph: point nodes p0..pn-1, centroids C0..Ck-1
        G = nx.DiGraph()
        n = len(data)
        # node names
        p_nodes = [f"p{i}" for i in range(n)]
        c_nodes = [f"C{j}" for j in range(k)]
        # add nodes
        for i, pn in enumerate(p_nodes):
            G.add_node(pn)
        for j, cn in enumerate(c_nodes):
            G.add_node(cn)

        # add edges from point to its assigned centroid
        edge_labels = {}
        for i, pn in enumerate(p_nodes):
            assigned = assignments[i]
            cn = c_nodes[assigned]
            G.add_edge(pn, cn)
            edge_labels[(pn, cn)] = f"{distances[i][assigned]:.2f}"

        # Improved positioning with NO overlapping
        pos = {}
        
        # Calculate proper spacing to avoid overlaps
        minx, maxx = min(data), max(data)
        data_range = maxx - minx if maxx != minx else 10.0
        
        # Create a layout that spreads all points horizontally to avoid overlaps
        sorted_indices = sorted(range(len(data)), key=lambda i: data[i])
        
        # Calculate minimum spacing needed (based on node size)
        min_spacing = max(1.0, data_range / max(8, len(data)))  # Ensure minimum spacing
        
        # Position points with guaranteed no overlap
        used_positions = set()
        for idx, i in enumerate(sorted_indices):
            x_value = data[i]
            
            # Find a free position near the actual value
            base_x = x_value
            offset = 0
            step = min_spacing / 2
            
            # Try positions around the actual value until we find a free spot
            while True:
                test_x = base_x + offset
                # Check if this position is far enough from all used positions
                if not any(abs(test_x - used_x) < min_spacing for used_x in used_positions):
                    pos[f"p{i}"] = (test_x, 0.0)
                    used_positions.add(test_x)
                    break
                
                # Alternate between positive and negative offsets
                if offset <= 0:
                    offset = -offset + step
                else:
                    offset = -offset
        
        # Position centroids higher up with more spacing
        for j, c in enumerate(centroids):
            pos[f"C{j}"] = (c, 2.0)

        # Set background color
        ax.set_facecolor('#F8F9FA')
        
        # Draw nodes with improved colors and spacing
        node_colors = []
        node_edge_colors = []
        for i in range(len(data)):
            cluster_idx = assignments[i] % len(cluster_colors)
            node_colors.append(cluster_colors[cluster_idx])
            node_edge_colors.append(edge_colors[cluster_idx])
        
        # Centroid colors
        centroid_colors = [cluster_colors[j % len(cluster_colors)] for j in range(k)]
        centroid_edge_colors = [edge_colors[j % len(edge_colors)] for j in range(k)]

        # Draw points with better visibility
        nx.draw_networkx_nodes(G, pos,
                               nodelist=p_nodes,
                               node_color=node_colors,
                               edgecolors=node_edge_colors,
                               linewidths=2,
                               node_size=800,
                               ax=ax)
        
        # Draw centroids (bigger, square shape)
        nx.draw_networkx_nodes(G, pos,
                               nodelist=c_nodes,
                               node_color=centroid_colors,
                               edgecolors=centroid_edge_colors,
                               linewidths=3,
                               node_shape="s",
                               node_size=1200,
                               ax=ax)

        # Improved labels with better formatting
        p_labels = {f"p{i}": f"{data[i]:.1f}" for i in range(len(data))}
        c_labels = {f"C{j}": f"C{j}\n{centroids[j]:.2f}" for j in range(k)}
        labels = {**p_labels, **c_labels}
        
        # Draw labels with better contrast
        nx.draw_networkx_labels(G, pos, labels=labels, 
                               font_size=10, font_weight='bold',
                               font_color='black', ax=ax)

        # Draw edges with better visibility
        edge_list = list(G.edges())
        edge_colors_for_edges = []
        for edge in edge_list:
            point_idx = int(edge[0][1:])  # Extract point index from 'p0', 'p1', etc.
            cluster_idx = assignments[point_idx] % len(edge_colors)
            edge_colors_for_edges.append(edge_colors[cluster_idx])
        
        nx.draw_networkx_edges(G, pos, 
                              edgelist=edge_list,
                              edge_color=edge_colors_for_edges,
                              arrows=False, 
                              width=2,
                              alpha=0.7,
                              ax=ax)
        
        # Draw edge labels with corrected positioning
        nx.draw_networkx_edge_labels(G, pos, 
                                    edge_labels=edge_labels, 
                                    font_size=9, 
                                    font_weight='bold',
                                    bbox=dict(boxstyle="round,pad=0.1", 
                                             facecolor='white', 
                                             edgecolor='gray',
                                             alpha=0.8),
                                    ax=ax)

        # Improved aesthetics
        ax.set_title(f"K-means Step {snap['iter']}\nCentroids: {', '.join(f'{c:.3f}' for c in centroids)}", 
                    fontsize=14, fontweight='bold', pad=20)
        
        # Better axis limits with more padding to accommodate spread-out points
        all_x_positions = [pos[f"p{i}"][0] for i in range(len(data))]
        x_min, x_max = min(all_x_positions), max(all_x_positions)
        x_range = x_max - x_min if x_max != x_min else 2.0
        ax.set_xlim(x_min - 0.3 * x_range, x_max + 0.3 * x_range)
        ax.set_ylim(-0.7, 2.7)
        
        # Remove y-axis ticks and add grid for better readability
        ax.set_yticks([])
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.set_xlabel('Data Values (spread to avoid overlap)', fontweight='bold', fontsize=11)
        
        # Add a subtle border
        for spine in ax.spines.values():
            spine.set_edgecolor('#CCCCCC')
            spine.set_linewidth(1.5)

    # Hide unused subplots
    for j in range(len(history), len(axes)):
        if j < len(axes):
            fig.delaxes(axes[j])

    plt.tight_layout(pad=2.0)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Saved improved visualization as {filename}")
    plt.show()

# ---------- Main interactive section ----------
if __name__ == "__main__":
    print("K-means (1-D) with improved step-by-step visualization\n")
    s = input("Enter data points (space separated, e.g. '5 12 7 4 3 11 19 25 13 14'): ").strip()
    data = parse_input_points(s)
    if len(data) == 0:
        raise SystemExit("No data provided.")

    k = int(input("Enter number of clusters k (e.g. 2): ").strip())
    init = input(f"Enter {k} initial centroids (space separated) or press Enter to auto-pick: ").strip()
    init_centroids = None
    if init:
        pcs = init.split()
        if len(pcs) != k:
            print("Number of centroids given doesn't match k — ignoring and auto-picking.")
        else:
            init_centroids = [float(x) for x in pcs]

    history = kmeans_1d(data, k, init_centroids)
    
    # Print textual step-by-step
    print("\nK-means Iterations (text):")
    for snap in history:
        it = snap["iter"]
        cent = snap["centroids"]
        assg = snap["assignments"]
        clusters = {j: [] for j in range(len(cent))}
        for x, a in zip(data, assg):
            clusters[a].append(x)
        print(f"\nStep {it}: centroids = {[round(c, 4) for c in cent]}")
        for j in sorted(clusters.keys()):
            print(f"  C{j} = {clusters[j]}")

    # Draw improved visualization
    draw_kmeans_history(data, history)