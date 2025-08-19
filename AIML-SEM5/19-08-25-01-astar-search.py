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

    def astar(self):
        open_list = []  # [(state, depth, f)]
        closed_set = set()
        start = (0, 0)
        open_list.append([start, 0, self.f(start, 0)])
        self.parent = {start: None}

        while open_list:
            # Sort by f value (lowest first)
            open_list.sort(key=lambda x: x[2])
            node, depth, f_val = open_list.pop(0)

            if node in closed_set:
                continue
            closed_set.add(node)

            # Check if target is reached in either jug
            if node[0] == self.target or node[1] == self.target:
                # Reconstruct path
                traversal = []
                curr = node
                while curr is not None:
                    traversal.append(curr)
                    curr = self.parent[curr]
                traversal.reverse()
                return traversal
            
            """
            # printing out the display function in every iteration

            traversal = []
            curr = node
            while curr is not None:
                traversal.append(curr)
                curr = self.parent[curr]
            traversal.reverse()
            display(traversal, self.parent)
            self.parent = {start: None}
            """

            for child in self.getchildren(*node):
                if child not in closed_set and child not in [n[0] for n in open_list]:
                    self.parent[child] = node
                    open_list.append([child, depth + 1, self.f(child, depth + 1)])
        # If no solution found
        return []

class display:
    def __init__(self, traversal, parent, closed_set=None):
        self.G = nx.DiGraph()
        self.traversal = traversal  # solution path
        self.parent = parent
        self.closed_set = closed_set if closed_set is not None else set()
        self.positions = {}
        self.drawgraph()

    def drawgraph(self):
        # Collect all nodes from parent mapping (all generated nodes)
        all_nodes = set(self.parent.keys()) | set(self.parent.values())
        all_nodes.discard(None)
        # Build the graph
        self.G.clear()
        for node in all_nodes:
            self.G.add_node(node)
        for child, par in self.parent.items():
            if par is not None:
                self.G.add_edge(par, child)

        # Layout: use tree layout similar to IDS
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

        root = (0, 0)
        self.positions = tree_layout(self.G, root)

        # Color nodes: solution path (traversal), expanded (closed_set), others
        node_colors = []
        for n in self.G.nodes():
            if n in self.traversal:
                node_colors.append('lightgreen')
            elif n in self.closed_set:
                node_colors.append('lightgreen')
            else:
                node_colors.append('pink')

        plt.figure(figsize=(14, 8), constrained_layout=True)
        nx.draw(self.G, pos=self.positions, with_labels=True,
                node_color=node_colors, node_size=1200,
                font_size=10, font_weight='bold', arrows=True, edge_color='black')

        # Draw solution path edges in red
        path_edges = list(zip(self.traversal, self.traversal[1:]))
        nx.draw_networkx_edges(self.G, self.positions, edgelist=path_edges, edge_color='red', width=2)

        plt.title("A* Traversal Tree of Water Jug Problem\n(Blue: Solution Path, Green: Expanded, Gray: Others)")
        plt.axis('off')
        # plt.tight_layout()
        plt.savefig("19-08-25-01-astar-search-output.png")
        plt.show()

if __name__ == "__main__":
    a = int(input("Enter capacity of Jug 1: "))
    b = int(input("Enter capacity of Jug 2: "))
    c = int(input("Enter the target amount: "))

    solver = waterjug(a, b, c)
    traversal = solver.astar()

    print("\nA* traversal path:")
    print(" -> ".join(str(state) for state in traversal))

    display(traversal, solver.parent)
