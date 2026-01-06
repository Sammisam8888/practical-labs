"""
Algorithm K-Medoid-Clustering
input - dataset D with n no of tuples
output - k no of clusters

BEGIN
    Arbitrarily choose K objects from D as initial medoids
    repeat
        Assign each tuple to the nearest medoid
            (distance = |x - medoid|)
        For each cluster, find the object (medoid) minimizing total distance 
            to all other points in that cluster
    until no change in medoids
END

Dry Run:
Let D = {5, 12, 7, 4, 3, 11, 19, 25, 13, 14}
K = 2
Initial medoids: M1 = 5, M2 = 12
Iteration continues until medoids stabilize.
"""
import matplotlib.pyplot as plt, networkx as nx, math, random, numpy as np

def p(s): 
    return [float(x) for x in s.strip().split()]

def i(d, k, c=None):
    if c: return [float(x) for x in c]
    u = []
    [u.append(x) for x in d if x not in u]
    [u.append(random.choice(d)) for _ in range(k - len(u))]
    return [float(x) for x in u[:k]]

def assign_clusters(d, medoids):
    r = []
    dist = []
    for x in d:
        dists = [abs(x - m) for m in medoids]
        r.append(np.argmin(dists))
        dist.append(dists)
    return r, dist

def update_medoids(d, r, k, old_medoids):
    new_medoids = []
    for j in range(k):
        cluster_points = [x for x, a in zip(d, r) if a == j]
        if not cluster_points:
            new_medoids.append(old_medoids[j])
            continue
        min_sum = float('inf')
        medoid = old_medoids[j]
        for candidate in cluster_points:
            total_dist = sum(abs(candidate - x) for x in cluster_points)
            if total_dist < min_sum:
                min_sum = total_dist
                medoid = candidate
        new_medoids.append(medoid)
    return new_medoids

def kmedoids(d, k, c0=None, max_iter=100):
    medoids = i(d, k, c0)
    history = []
    for it in range(1, max_iter + 1):
        r, dist = assign_clusters(d, medoids)
        new_medoids = update_medoids(d, r, k, medoids)
        history.append({"iter": it, "m": medoids[:], "r": r[:], "dist": dist[:]})
        if new_medoids == medoids:
            break
        medoids = new_medoids
    return history

def v(d, h):
    n = len(h)
    cols = 2 if n > 1 else 1
    rows = math.ceil(n / cols)
    fig, ax = plt.subplots(rows, cols, figsize=(cols * 10, rows * 6))
    ax = ax.flatten() if hasattr(ax, "flatten") else [ax]
    cc = ['#FFE5E5','#E5FFE5','#E5E5FF','#FFFFE5','#FFE5FF','#E5FFFF']
    ec = ['#FF6B6B','#4ECDC4','#45B7D1','#96CEB4','#FFEAA7','#DDA0DD']

    for idx, snap in enumerate(h):
        a0 = ax[idx]
        m = snap["m"]; r = snap["r"]; dist = snap["dist"]; k = len(m)
        G = nx.DiGraph()
        p_nodes = [f"p{i}" for i in range(len(d))]
        m_nodes = [f"M{j}" for j in range(k)]
        [G.add_node(nm) for nm in p_nodes + m_nodes]
        el = {}
        [G.add_edge(p_nodes[i], m_nodes[r[i]]) or el.update({(p_nodes[i], m_nodes[r[i]]): f"{dist[i][r[i]]:.2f}"}) for i in range(len(d))]

        pos = {}
        srt = sorted(range(len(d)), key=lambda i: d[i])
        used = set()
        rng = max(d) - min(d) if max(d) != min(d) else 10
        for ii, idx2 in enumerate(srt):
            x = d[idx2]; o = 0; step = max(1, rng / max(8, len(d))) / 2
            while any(abs(x + o - u) < step * 2 for u in used):
                o = -o + step if o <= 0 else -o
            pos[p_nodes[idx2]] = (x + o, 0)
            used.add(x + o)
        for j, ccen in enumerate(m):
            pos[m_nodes[j]] = (ccen, 2)
        a0.set_facecolor('#F8F9FA')

        nx.draw_networkx_nodes(G, pos, nodelist=p_nodes,
                               node_color=[cc[r[i] % len(cc)] for i in range(len(d))],
                               edgecolors=[ec[r[i] % len(ec)] for i in range(len(d))],
                               linewidths=2, node_size=800, ax=a0)
        nx.draw_networkx_nodes(G, pos, nodelist=m_nodes,
                               node_color=[cc[j % len(cc)] for j in range(k)],
                               edgecolors=[ec[j % len(ec)] for j in range(k)],
                               linewidths=3, node_shape='s', node_size=1200, ax=a0)
        nx.draw_networkx_labels(G, pos,
                                {**{p_nodes[i]: f"{d[i]:.1f}" for i in range(len(d))},
                                 **{m_nodes[j]: f"M{j}\n{m[j]:.2f}" for j in range(k)}},
                                font_size=10, font_weight='bold', font_color='black', ax=a0)
        nx.draw_networkx_edges(G, pos, edgelist=list(G.edges()),
                               edge_color=[ec[r[int(e[0][1:])] % len(ec)] for e in G.edges()],
                               arrows=False, width=2, alpha=0.7, ax=a0)   # ✅ FIXED HERE
        nx.draw_networkx_edge_labels(G, pos, edge_labels=el, font_size=9, font_weight='bold',
                                     bbox=dict(boxstyle="round,pad=0.1", facecolor='white',
                                               edgecolor='gray', alpha=0.8), ax=a0)
        a0.set_title(f"K-Medoids Step {snap['iter']}\nMedoids: {', '.join(f'{x:.2f}' for x in m)}",
                     fontsize=14, fontweight='bold', pad=20)
        xvals = [pos[p][0] for p in p_nodes]
        xr = max(xvals) - min(xvals) if max(xvals) != min(xvals) else 2
        a0.set_xlim(min(xvals) - 0.3 * xr, max(xvals) + 0.3 * xr)
        a0.set_ylim(-0.7, 2.7)
        a0.set_yticks([])
        a0.grid(True, alpha=0.3, linestyle='--')
        a0.set_xlabel('Data Values (spread to avoid overlap)', fontweight='bold', fontsize=11)
        for sp in a0.spines.values():
            sp.set_edgecolor('#CCCCCC')
            sp.set_linewidth(1.5)

    for j in range(len(h), len(ax)):
        fig.delaxes(ax[j])
    plt.tight_layout(pad=2)
    plt.show()

if __name__ == "__main__":
    print("K-Medoids (1-D) with visual step-by-step representation\n")
    d = p(input("Enter data points (space separated): "))
    if len(d) == 0:
        raise SystemExit("No data provided.")
    k = int(input("Enter number of clusters k: "))
    init = input(f"Enter {k} initial medoids (space separated) or press Enter to auto-pick: ").strip()
    c0 = None
    if init:
        c0s = init.split()
        c0 = [float(x) for x in c0s] if len(c0s) == k else None
    h = kmedoids(d, k, c0)

    print("\nK-Medoids Iterations (text):")
    for s in h:
        it = s["iter"]
        m = s["m"]
        r = s["r"]
        clusters = {j: [] for j in range(len(m))}
        [clusters[a].append(x) for x, a in zip(d, r)]
        print(f"\nStep {it}: medoids = {[round(x,4) for x in m]}")
        for j in sorted(clusters.keys()):
            print(f"  M{j} = {clusters[j]}")
    v(d, h)
