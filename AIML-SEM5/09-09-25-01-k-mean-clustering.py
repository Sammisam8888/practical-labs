# write a program to implement k-means clustering algorithm.

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

# kmeans_visual_steps.py
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

# ---------- Visualization helper ----------
def draw_kmeans_history(data, history, filename="kmeans_steps.png"):
    n_steps = len(history)
    # layout grid
    cols = 2 if n_steps > 1 else 1
    rows = math.ceil(n_steps / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(cols*7, rows*4))
    if not isinstance(axes, (list, tuple, np.ndarray)):
        axes = [axes]
    axes = (axes.flatten() if hasattr(axes, "flatten") else axes)

    cmap = plt.get_cmap("tab10")
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

        # create positions: x = numeric coordinate, y = 0 for points, y = 1 for centroids
        pos = {}
        # slight jitter for overlapping identical points
        value_counts = {}
        for i, x in enumerate(data):
            value_counts.setdefault(x, 0)
            jitter = (value_counts[x] * 0.08) - 0.08 * (value_counts[x] // 2)
            pos[f"p{i}"] = (x + jitter, 0.0)
            value_counts[x] += 1
        for j, c in enumerate(centroids):
            pos[f"C{j}"] = (c, 1.0)

        # draw nodes: data points colored by cluster
        node_colors = []
        for i in range(len(data)):
            clr = cmap(assignments[i] % 10)
            node_colors.append(clr)
        # centroid colors
        centroid_colors = [cmap(j % 10) for j in range(k)]

        # Draw on axis (using networkx drawing but passing ax)
        ax.set_title(f"K-means Step {snap['iter']}\ncentroids = {', '.join(f'{c:.3f}' for c in centroids)}")
        # draw points
        nx.draw_networkx_nodes(G, pos,
                               nodelist=p_nodes,
                               node_color=node_colors,
                               node_size=500,
                               ax=ax)
        # draw centroids (bigger)
        nx.draw_networkx_nodes(G, pos,
                               nodelist=c_nodes,
                               node_color=centroid_colors,
                               node_shape="s",
                               node_size=900,
                               ax=ax)

        # labels
        p_labels = {f"p{i}": f"{data[i]:.2f}" for i in range(len(data))}
        c_labels = {f"C{j}": f"C{j}\n{centroids[j]:.2f}" for j in range(k)}
        labels = {**p_labels, **c_labels}
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=9, ax=ax)

        # edges and edge labels
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle="-", arrows=False, ax=ax)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, ax=ax)

        # aesthetics
        ax.set_ylim(-0.6, 1.6)
        # set x limits slightly wider than data range
        minx, maxx = min(data), max(data)
        xrange = maxx - minx if maxx != minx else 1.0
        ax.set_xlim(minx - 0.1 * xrange, maxx + 0.1 * xrange)
        ax.set_yticks([])

    # hide unused subplots
    for j in range(len(history), rows*cols):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.savefig(filename)
    print(f"Saved visualization as {filename}")
    plt.show()

# ---------- Main interactive section ----------
if __name__ == "__main__":
    print("K-means (1-D) with step-by-step visualization (networkx + matplotlib)\n")
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

    # Draw combined image of all steps
    draw_kmeans_history(data, history)
