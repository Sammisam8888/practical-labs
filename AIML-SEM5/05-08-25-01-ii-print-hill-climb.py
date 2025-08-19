import matplotlib.pyplot as plt
import networkx as nx
import math
import heapq

# Heuristic function (Manhattan distance)
def h(s, goal):
    return abs(s[0] - goal[0]) + abs(s[1] - goal[1])

# Next possible states
def nxt(s, ca, cb):
    a, b = s
    res = set()
    res.add((ca, b))      # Fill A
    res.add((a, cb))      # Fill B
    res.add((0, b))       # Empty A
    res.add((a, 0))       # Empty B
    p = min(a, cb - b)    # Pour A -> B
    res.add((a - p, b + p))
    p = min(b, ca - a)    # Pour B -> A
    res.add((a + p, b - p))
    return res

# Level-wise hill climbing
def hc_levelwise(ca, cb, goal):
    start = (0, 0)
    vis = set([start])
    G = nx.DiGraph()
    pq = [(h(start, goal), start)]
    level_nodes = [start]

    yield ("init", G.copy(), level_nodes, None)

    while level_nodes:
        next_level = []
        added_edges = []

        # Sort current level by heuristic (hill climbing order)
        level_nodes.sort(key=lambda x: h(x, goal))

        for cur in level_nodes:
            if cur == goal:
                yield ("goal", G.copy(), next_level + [cur], None)
                return

            for n in nxt(cur, ca, cb):
                if n not in vis:
                    G.add_edge(cur, n)
                    vis.add(n)
                    next_level.append(n)
                    added_edges.append((cur, n))

        # yield entire level after adding all nodes
        yield ("level", G.copy(), next_level, added_edges)
        level_nodes = next_level

    yield ("fail", G.copy(), [], None)

# Recursive position calculation for tree layout
def tree_pos(G, root=None, w=1.5, gap=0.5, y=0, x=0.5, pos=None, par=None):
    if not G.nodes:
        return {}
    if root is None:
        root = next(iter(G.nodes))
    if pos is None:
        pos = {root: (x, y)}
    else:
        pos[root] = (x, y)
    kids = list(G.successors(root))
    if par is not None and par in kids:
        kids.remove(par)
    if kids:
        dx = w / len(kids)
        nxpos = x - w / 2 - dx / 2
        for k in kids:
            nxpos += dx
            pos = tree_pos(G, root=k, w=dx, gap=gap, y=y-gap,
                           x=nxpos, pos=pos, par=root)
    return pos

# Draw all stages level by level
def draw_all_levels(ca, cb, goal):
    stages = list(hc_levelwise(ca, cb, goal))
    n = len(stages)

    cols = 3
    rows = math.ceil(n / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(cols*6, rows*5))
    if rows == 1:
        axes = [axes]
    axes = axes.flatten()

    final_status, final_path = None, []

    for i, (status, Gshow, level_nodes, added_edges) in enumerate(stages):
        final_status = status
        ax = axes[i]

        if not Gshow.nodes:
            axes[i].axis("off")
            continue

        root = next(iter(Gshow.nodes))
        pos = tree_pos(Gshow, root=root)

        node_colors = ["lightblue" for n in Gshow.nodes()]

        edge_colors, widths = [], []
        for e in Gshow.edges():
            if added_edges and e in added_edges:
                edge_colors.append("red")
                widths.append(3)
            else:
                edge_colors.append("gray")
                widths.append(1.2)

        node_labels = {n: str(n) for n in Gshow.nodes()}

        nx.draw(
            Gshow, pos, ax=ax,
            with_labels=True,
            labels=node_labels,
            node_size=900,
            node_color=node_colors,
            edge_color=edge_colors,
            width=widths,
            font_size=8,
            font_weight="bold",
            arrows=True,
            arrowsize=18
        )

        for node, (x, y) in pos.items():
            ax.text(x + 0.08, y, f"h={h(node, goal)}",
                    fontsize=7, color="black", weight="bold")

        ax.set_title(f"Step {i+1}: {status}", fontsize=11)

    for j in range(i+1, len(axes)):
        axes[j].axis("off")

    plt.suptitle(f"Hill Climbing – Water Jug (Goal = {goal})", fontsize=14, weight="bold", y=1.02)
    # plt.tight_layout()
    plt.savefig("05-08-25-01-hill-climb-search-output.png")
    plt.show()

    if final_status == "goal":
        print("\n✔ Reached goal!")
    else:
        print("\n❌ Failed to reach target.")

# Main
def main():
    ca = int(input("Enter Jug 1 capacity: "))
    cb = int(input("Enter Jug 2 capacity: "))
    gx = int(input("Enter Goal amount in Jug 1: "))
    gy = int(input("Enter Goal amount in Jug 2: "))
    goal = (gx, gy)

    if gx > ca or gy > cb:
        print("❌ Goal exceeds jug capacities.")
        return

    draw_all_levels(ca, cb, goal)

if __name__ == "__main__":
    main()