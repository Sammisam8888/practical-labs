import matplotlib.pyplot as plt
import networkx as nx

capA = 4
capB = 3
goal = 2

parent = {}
G = nx.DiGraph()
path = []
seen_global = set()
G.add_node((0, 0))

snaps = []  # snapshots for each depth

def ids():
    d = 0
    while True:
        seen_local = set()
        found = dls((0, 0), d, seen_local)
        seen_global.update(seen_local)

        if d > 0:  # Skip depth 0 snapshot
            snaps.append({
                'G': G.copy(),
                'seen': seen_global.copy(),
                'path': path.copy(),
                'depth': d
            })

        if found:
            trace(found)
            break
        d += 1
    plot_snaps()

def dls(state, limit, seen_local):
    if state in seen_local:
        return None
    seen_local.add(state)

    a, b = state
    if a == goal or b == goal:
        return state
    if limit == 0:
        return None

    moves = [
        (capA, b),  # fill A
        (a, capB),  # fill B
        (0, b),     # empty A
        (a, 0),     # empty B
        (a - min(a, capB - b), b + min(a, capB - b)),  # pour A→B
        (a + min(b, capA - a), b - min(b, capA - a))   # pour B→A
    ]

    for nxt in moves:
        if nxt not in seen_local:
            if nxt not in parent:
                parent[nxt] = state
                G.add_node(nxt)
                G.add_edge(state, nxt)
            found = dls(nxt, limit - 1, seen_local)
            if found:
                return found
    return None

def trace(goal_state):
    path.clear()
    cur = goal_state
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    path.reverse()

def plot_snaps():
    total = len(snaps)
    cols = 3
    rows = (total + cols - 1) // cols
    plt.figure(figsize=(cols * 6, rows * 5), constrained_layout=True)

    for i, snap in enumerate(snaps):
        plt.subplot(rows, cols, i + 1)
        G_snap = snap['G']
        seen = snap['seen']
        sol_path = snap['path']
        depth = snap['depth']

        pos = tree_layout(G_snap, (0, 0))

        node_colors = []
        for n in G_snap.nodes():
            if n in sol_path:
                node_colors.append('lightblue')
            elif n in seen:
                node_colors.append('lightgreen')
            else:
                node_colors.append('magma')

        nx.draw(G_snap, pos, with_labels=True, node_color=node_colors,
                node_size=700, font_size=8, edge_color='gray')

        path_edges = list(zip(sol_path, sol_path[1:]))
        nx.draw_networkx_edges(G_snap, pos, edgelist=path_edges,
                               edge_color='black', width=2)

        plt.title(f"Depth Limit = {depth}", fontsize=12)
        plt.axis('off')

    # plt.tight_layout()
    plt.suptitle("IDS Water Jug Search Trees by Depth Limit", fontsize=16, y=1.02)
    plt.savefig("05-08-25-02-iterative-deepening-output.png")
    plt.show()

def tree_layout(G, root, width=1., gap=0.2, y=0, x=0.5):
    pos = {root: (x, y)}
    kids = list(G.successors(root))
    if not kids:
        return pos
    dx = width / len(kids)
    next_x = x - width / 2 - dx / 2
    for kid in kids:
        next_x += dx
        pos.update(tree_layout(G, kid, width=dx, gap=gap,
                               y=y - gap, x=next_x))
    return pos

ids()