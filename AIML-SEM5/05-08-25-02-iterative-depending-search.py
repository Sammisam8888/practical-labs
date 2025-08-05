from collections import deque
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

    def iterative_depth(self):
        traversal = []
        
        return traversal

class display:
    def __init__(self, traversal, parent):
        self.G = nx.DiGraph()
        self.traversal = traversal
        self.parent = parent
        self.positions = {}
        self.drawgraph()

    def drawgraph(self):
        level_map = {}  # node -> level
        level_nodes = {}  # level -> list of nodes

        # Assign levels to each node
        for node in self.traversal:
            if node == (0, 0):
                level_map[node] = 0
                level_nodes[0] = [node]
            else:
                parent = self.parent.get(node)
                if parent:
                    level = level_map[parent] + 1
                    level_map[node] = level
                    if level not in level_nodes:
                        level_nodes[level] = []
                    level_nodes[level].append(node)

        self.G.clear()
        self.positions.clear()

        y_gap = 2  # vertical gap between levels
        x_gap = 2  # horizontal gap between nodes

        for level in sorted(level_nodes.keys()):
            nodes = level_nodes[level]
            start_x = - (len(nodes) - 1) * x_gap / 2  # center the level horizontally
            for i, node in enumerate(nodes):
                x = start_x + i * x_gap
                y = -level * y_gap
                self.positions[node] = (x, y)
                self.G.add_node(node)

        # Add edges from parent to children
        for node in self.traversal:
            parent = self.parent.get(node)
            if parent and parent in self.traversal:
                self.G.add_edge(parent, node)

        plt.figure(figsize=(14, 8))
        nx.draw(self.G, pos=self.positions, with_labels=True,
                node_color='lightblue', node_size=2000,
                font_size=10, font_weight='bold', arrows=True)
        plt.title("Iterative Depending Search Traversal Tree of Water Jug Problem")
        plt.show()

if __name__ == "__main__":
    a = int(input("Enter capacity of Jug 1: "))
    b = int(input("Enter capacity of Jug 2: "))
    c = int(input("Enter the target amount: "))

    solver = waterjug(a, b, c)
    traversal = solver.iterative_depth()

    print("\nIterative Depending Search traversal path:")
    print(" -> ".join(str(state) for state in traversal))

    display(traversal, solver.parent)
