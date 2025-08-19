
import matplotlib.pyplot as plt
import networkx as nx

class waterjug:
    def __init__(self, jug1, jug2, target):
        self.jug1 = jug1
        self.jug2 = jug2
        self.target = target
        self.visited = set()
        self.parent = {}
        

    def check(self, x, y):
        return 0 <= x <= self.jug1 and 0 <= y <= self.jug2

    def getchildren(self, x, y):
        states = []

        # Fill Jug1
        states.append((self.jug1, y))
        # Fill Jug2
        states.append((x, self.jug2))
        # Empty Jug1
        states.append((0, y))
        # Empty Jug2
        states.append((x, 0))
        # Pour Jug1 -> Jug2
        pour = min(x, self.jug2 - y)
        states.append((x - pour, y + pour))
        # Pour Jug2 -> Jug1
        pour = min(y, self.jug1 - x)
        states.append((x + pour, y - pour))

        return [state for state in states if self.check(*state)]


    def h(self, state):
        x, y = state
        if x > 0 and x<self.jug1 and y > 0 and y<self.jug2:
            return 2
        elif (x>0 and x<self.jug1) or (y>0 and y<self.jug2):
            return 4
        elif (x==0 and y==0) or (x==self.jug1 and y==self.jug2):
            return 10
        elif (x==0 and y==self.jug2) or ( x==self.jug1 and y==0):
            return 8

    def f(self, node,depth):
        return depth+self.h(node)

    def astar(self, show_step_by_step=False):
        open_list = []  # [(state, depth, f)]
        closed_set = set()
        start = (0, 0)
        open_list.append([start, 0, self.f(start, 0)])
        self.parent = {start: None}


        last_depth = -1
        while open_list:
            # Sort by f value (lowest first)
            open_list.sort(key=lambda x: x[2])
            node, depth, f_val = open_list.pop(0)

            if node in closed_set:
                continue
            closed_set.add(node)

            # Print/display at each step: show all expanded nodes so far
            if show_step_by_step:
                print(f"\nA* Step {len(closed_set)} (expanding node {node}):")
                print("Expanded nodes so far:")
                print(", ".join(str(n) for n in closed_set))

            # Print/display at each new depth (optional, can keep or remove)
            # if show_step_by_step and depth != last_depth:
            #     last_depth = depth
            #     # Reconstruct path to current node
            #     traversal = []
            #     curr = node
            #     while curr is not None:
            #         traversal.append(curr)
            #         curr = self.parent[curr]
            #     traversal.reverse()
            #     print(f"\nTraversal at depth {depth}:")
            #     print(" -> ".join(str(state) for state in traversal))
            #     # Optionally, display the graph for this depth
            #     # display(traversal, self.parent, closed_set.copy())

            # Check if target is reached in either jug
            if node[0] == self.target or node[1] == self.target:
                # Reconstruct patha
                traversal = []
                curr = node
                while curr is not None:
                    traversal.append(curr)
                    curr = self.parent[curr]
                traversal.reverse()
                return traversal

            for child in self.getchildren(*node):
                if child not in closed_set and child not in [n[0] for n in open_list]:
                    self.parent[child] = node
                    open_list.append([child, depth + 1, self.f(child, depth + 1)])
        # If no solution found
        return []

def plot_astar_traversal(traversal, parent, closed_set=None):
    """
    Display the traversal path of the A* algorithm step by step, showing the graph after each node in the solution path is added.
    """
    import matplotlib.pyplot as plt
    import networkx as nx
    if closed_set is None:
        closed_set = set()
    snaps = []
    for i in range(1, len(traversal)+1):
        partial_path = traversal[:i]
        G = nx.DiGraph()
        all_nodes = set(parent.keys()) | set(parent.values())
        all_nodes.discard(None)
        for node in all_nodes:
            G.add_node(node)
        for child, par in parent.items():
            if par is not None:
                G.add_edge(par, child)
        snap = {
            'G': G.copy(),
            'sol_path': partial_path.copy(),
            'closed': closed_set.copy(),
            'step': i-1
        }
        snaps.append(snap)

    total = len(snaps)
    cols = 3
    rows = (total + cols - 1) // cols
    plt.figure(figsize=(cols * 6, rows * 5), constrained_layout=True)

    def tree_layout(G, root, width=1., gap=0.2, y=0, x=0.5):
        pos = {root: (x, y)}
        kids = list(G.successors(root))
        if not kids:
            return pos
        dx = width / len(kids)
        next_x = x - width / 2 - dx / 2
        for kid in kids:
            next_x += dx
            pos.update(tree_layout(G, kid, width=dx, gap=gap, y=y - gap, x=next_x))
        return pos

    for i, snap in enumerate(snaps):
        plt.subplot(rows, cols, i + 1)
        G_snap = snap['G']
        sol_path = snap['sol_path']
        closed = snap['closed']
        step = snap['step']
        pos = tree_layout(G_snap, (0, 0))
        node_colors = []
        for n in G_snap.nodes():
            if n in sol_path:
                node_colors.append('lightgreen')
            elif n in closed:
                node_colors.append('lightgreen')
            else:
                node_colors.append('pink')
        nx.draw(G_snap, pos, with_labels=True, node_color=node_colors,
                node_size=700, font_size=8, edge_color='gray')
        path_edges = list(zip(sol_path, sol_path[1:]))
        nx.draw_networkx_edges(G_snap, pos, edgelist=path_edges,
                               edge_color='black', width=2)
        plt.title(f"A* Step {step+1}", fontsize=12)
        plt.axis('off')
    plt.suptitle("A* Water Jug Solution Path Step by Step", fontsize=16, y=1.02)
    plt.savefig("19-08-25-01-astar-stepbystep.png")
    plt.show()


if __name__ == "__main__":
    a = int(input("Enter capacity of Jug 1: "))
    b = int(input("Enter capacity of Jug 2: "))
    c = int(input("Enter the target amount: "))

    solver = waterjug(a, b, c)
    traversal = solver.astar(show_step_by_step=True)

    print("\nA* traversal path:")
    print(" -> ".join(str(state) for state in traversal))

    # Show step-by-step traversal for A*
    plot_astar_traversal(traversal, solver.parent)
