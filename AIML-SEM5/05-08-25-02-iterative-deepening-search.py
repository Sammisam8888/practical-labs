import matplotlib.pyplot as plt
import networkx as nx

class waterjug:
    def __init__(self, jug1, jug2, target):
        self.jug1 = jug1
        self.jug2 = jug2
        self.target = target
        self.visited = set()
        self.parent = {}
        self.depthcutoff=0
        

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

    
    def iterativedeepening(self):
        def dls(node, depth):
            traversal.append(node)
            if (node[0] == self.target and node[1] == 0) or (node[1] == self.target and node[0] == 0):
                return True
            if depth == 0:
                return False
            for state in self.getchildren(*node):
                if state not in visited:
                    visited.add(state)
                    self.parent[state] = node
                    if dls(state, depth - 1):
                        return True
            return False

        start = (0, 0)
        traversal = []

        for self.depthcutoff in range(1, 50):  # prevent infinite loop
            visited = {start}
            if dls(start, self.depthcutoff):
                return traversal

        return traversal

class display:
    def __init__(self, traversal, parent):
        self.G = nx.DiGraph()
        self.traversal = traversal
        self.parent = parent
        self.positions = {}
        self.drawgraph()

    def drawgraph(self):
        levelmap = {}  # node -> level
        levelnodes = {}  # level -> list of nodes

        # Assign level for root
        root = (0, 0)
        levelmap[root] = 0
        levelnodes[0] = [root]

        # Process nodes in traversal order
        for node in self.traversal:
            if node == root:
                continue
            parent = self.parent.get(node)
            if parent and parent in levelmap:  # only assign if parent's level is known
                level = levelmap[parent] + 1
                levelmap[node] = level
                levelnodes.setdefault(level, []).append(node)

        self.G.clear()
        self.positions.clear()

        ygap = 2
        xgap = 2

        for level in sorted(levelnodes.keys()):
            nodes = levelnodes[level]
            startx = - (len(nodes) - 1) * xgap / 2
            for i, node in enumerate(nodes):
                x = startx + i * xgap
                y = -level * ygap
                self.positions[node] = (x, y)
                self.G.add_node(node)

        # Add edges from parent to children
        for node, parent in self.parent.items():
            if parent in self.positions and node in self.positions:
                self.G.add_edge(parent, node)

        plt.figure(figsize=(14, 8))
        nx.draw(self.G, pos=self.positions, with_labels=True,
                node_color='peachpuff', node_size=2000,
                font_size=10, font_weight='bold', arrows=True)
        plt.title("Iterative Deepening Traversal of Water Jug Problem")
        plt.show()

if __name__ == "__main__":
    a = int(input("Enter capacity of Jug 1: "))
    b = int(input("Enter capacity of Jug 2: "))
    c = int(input("Enter the target amount: "))

    solver = waterjug(a, b, c)
    traversal = solver.iterativedeepening()

    print("\nIterative Deepening traversal path:")
    d=[]
    for state in traversal:
        if state not in d:
            d.append(state)
    print(" -> ".join(str(state) for state in d))

    display(traversal, solver.parent)
