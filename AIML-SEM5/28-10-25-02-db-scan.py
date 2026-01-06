"""
Algorithm DBSCAN
Input: 
    D – dataset of points
    eps – maximum radius of the neighborhood
    minPts – minimum number of points to form a dense region
Output:
    Clusters of density-connected points

BEGIN
    Mark all points as UNVISITED
    cluster_id = 0
    for each point P in dataset D:
        if P is UNVISITED:
            mark P as VISITED
            N = points within eps of P
            if |N| < minPts:
                mark P as NOISE
            else:
                cluster_id = cluster_id + 1
                expandCluster(P, N, cluster_id)
END

Procedure expandCluster(P, N, cluster_id):
    assign P to cluster_id
    for each point P' in N:
        if P' is UNVISITED:
            mark P' as VISITED
            N' = points within eps of P'
            if |N'| ≥ minPts:
                N = N ∪ N'
        if P' is not yet assigned to any cluster:
            assign P' to cluster_id

"""

import math, random, matplotlib.pyplot as plt, networkx as nx

def dist(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def region_query(D, point, eps):
    return [i for i, p in enumerate(D) if dist(D[point], p) <= eps]

def expand_cluster(D, labels, point, cluster_id, eps, minPts, visited):
    neighbors = region_query(D, point, eps)
    if len(neighbors) < minPts:
        labels[point] = -1
        return False
    labels[point] = cluster_id
    i = 0
    while i < len(neighbors):
        n = neighbors[i]
        if not visited[n]:
            visited[n] = True
            new_neighbors = region_query(D, n, eps)
            if len(new_neighbors) >= minPts:
                neighbors += [x for x in new_neighbors if x not in neighbors]
        if labels[n] == 0 or labels[n] == -1:
            labels[n] = cluster_id
        i += 1
    return True

def dbscan(D, eps, minPts):
    labels = [0] * len(D)
    visited = [False] * len(D)
    cluster_id = 0
    steps = []

    for i in range(len(D)):
        if visited[i]:
            continue
        visited[i] = True
        if expand_cluster(D, labels, i, cluster_id + 1, eps, minPts, visited):
            cluster_id += 1
        steps.append(labels[:])
    return labels, steps, cluster_id

def visualize_dbscan(D, steps):
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#96CEB4', '#DDA0DD', '#FFD700']
    for step_idx, labels in enumerate(steps, start=1):
        plt.figure(figsize=(7, 6))
        G = nx.Graph()
        for i in range(len(D)):
            G.add_node(i, pos=(D[i][0], D[i][1]))

        for i in range(len(D)):
            for j in range(i + 1, len(D)):
                if dist(D[i], D[j]) <= eps:
                    G.add_edge(i, j)

        pos = nx.get_node_attributes(G, 'pos')
        cluster_ids = set([c for c in labels if c > 0])
        node_colors = [colors[c % len(colors)] if c > 0 else "#BBBBBB" for c in labels]
        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=800, font_weight='bold', font_color='black', edge_color="#CCCCCC")
        plt.title(f"DBSCAN Step {step_idx}: Cluster assignments {labels}", fontsize=14, fontweight='bold')
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True, alpha=0.3)
        plt.show()

if __name__ == "__main__":
    print("DBSCAN Algorithm Implementation (with Visualization)\n")
    n = int(input("Enter number of data points: "))
    D = []
    for i in range(n):
        x, y = map(float, input(f"Enter point {i + 1} (x y): ").split())
        D.append((x, y))
    eps = float(input("Enter epsilon (neighborhood distance): "))
    minPts = int(input("Enter minimum number of points (minPts): "))

    labels, steps, clusters = dbscan(D, eps, minPts)
    print(f"\nTotal Clusters Formed: {clusters}")
    for i, (p, l) in enumerate(zip(D, labels)):
        print(f"Point {p} -> {'Noise' if l == -1 else f'Cluster {l}'}")
    visualize_dbscan(D, steps)
