import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

# Normalize partition to avoid duplicates (sorted order)
def normalize(state):
    parts = list(map(int, state.split("+")))
    parts.sort()
    return "+".join(map(str, parts))

# Expand node into partitions (skip equal halves)
def expand_state(state):
    parts = list(map(int, state.split("+")))
    children = []
    for i, p in enumerate(parts):
        if p > 1:  # split p into two
            for j in range(1, p):
                if j == p - j:   # skip equal partitions
                    continue
                new_parts = parts[:i] + [j, p - j] + parts[i+1:]
                new_parts.sort()
                children.append("+".join(map(str, new_parts)))
    return list(set(children))  # unique children

# Build DAG instead of tree (shared children)
def build_graph(start):
    g = nx.DiGraph()
    vis = set()
    q = [normalize(start)]
    while q:
        current = q.pop(0)
        if current in vis:
            continue
        vis.add(current)
        for child in expand_state(current):
            child = normalize(child)
            g.add_edge(current, child)
            if child not in vis:
                q.append(child)
    return g

# Compute depth of each node (BFS)
def compute_levels(g, root):
    levels = {root: 0}
    q = [root]
    while q:
        current = q.pop(0)
        for child in g.successors(current):
            if child not in levels:
                levels[child] = levels[current] + 1
                q.append(child)
    return levels

# Minimax with terminal distinction (true terminal = -1, dead-end = +1)
def minimax(g, node, maximizing, memo, levels, max_depth):
    if node in memo:
        return memo[node]

    children = list(g.successors(node))

    if not children:  # terminal
        if levels[node] == max_depth:
            val = -1   # true terminal
        else:
            val = +1   # dead-end branch
        memo[node] = val
        return val

    vals = [minimax(g, c, not maximizing, memo, levels, max_depth) for c in children]
    val = max(vals) if maximizing else min(vals)
    memo[node] = val
    return val

# Draw graph up to a given level with dashed level lines & right labels
def draw_graph_upto_level(g, memo, levels, max_level, pos):
    plt.figure(figsize=(14, 10))
    nodes = [n for n, lvl in levels.items() if lvl <= max_level]
    edges = [(u, v) for u, v in g.edges if levels[u] <= max_level and levels[v] <= max_level]

    labels = {node: f"{node}\n{memo.get(node, '')}" for node in nodes}
    nx.draw(g, pos, with_labels=False, nodelist=nodes, edgelist=edges,
            node_color='lightblue', node_size=1800, arrows=True)
    nx.draw_networkx_labels(g, pos, labels, font_size=7)

    # dashed horizontal lines + right labels
    level_to_nodes = {lvl: [] for lvl in range(max_level + 1)}
    for node, lvl in levels.items():
        if lvl <= max_level:
            level_to_nodes[lvl].append(node)

    for lvl, nodes_at in level_to_nodes.items():
        if not nodes_at:
            continue
        ys = [pos[n][1] for n in nodes_at]
        xs = [pos[n][0] for n in nodes_at]
        y = sum(ys) / len(ys)
        xmin, xmax = min(xs), max(xs)
        plt.hlines(y, xmin - 100, xmax + 100, linestyles="dashed", colors="gray")
        role = "MIN" if lvl % 2 == 0 else "MAX"
        plt.text(xmax + 120, y, f"{role} level {lvl}",
                 fontsize=10, ha="left", va="center", color="red", fontweight="bold")

    plt.title(f"Minimax Partition Graph up to Level {max_level}")
    plt.show()

if __name__ == "__main__":
    print("Minimax Partition Graph (Unique States)\n")
    n = int(input("Enter a number (e.g., 9): "))
    start = str(n)

    g = build_graph(start)
    root = normalize(start)
    levels = compute_levels(g, root)
    max_depth = max(levels.values())

    memo = {}
    # even levels = MIN, so root is MIN -> maximizing=False
    root_val = minimax(g, root, False, memo, levels, max_depth)

    print("Root minimax value:", root_val)
    print("\nNode values:")
    for node, val in memo.items():
        role = "MIN" if levels[node] % 2 == 0 else "MAX"
        print(f"{node} ({role}) -> {val}")

    pos = graphviz_layout(g, prog='dot')
    for d in range(max_depth + 1):
        draw_graph_upto_level(g, memo, levels, d, pos)