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

        states.append((self.jug1, y))  # Fill Jug1
        states.append((x, self.jug2))  # Fill Jug2
        states.append((0, y))          # Empty Jug1
        states.append((x, 0))          # Empty Jug2

        pour = min(x, self.jug2 - y)   # Pour Jug1 -> Jug2
        states.append((x - pour, y + pour))

        pour = min(y, self.jug1 - x)   # Pour Jug2 -> Jug1
        states.append((x + pour, y - pour))

        return [state for state in states if self.check(*state)]

    def dfs(self):
        stack = []
        stack.append((0, 0))
        self.visited.add((0, 0))
        traversal = []

        found = None
        while stack:
            curr = stack.pop()
            traversal.append(curr)

            if self.target in curr:
                found = curr
                break

            for next_state in self.getchildren(*curr):
                if next_state not in self.visited:
                    self.visited.add(next_state)
                    self.parent[next_state] = curr
                    stack.append(next_state)

        return traversal

class display:
    def __init__(self, traversal, parent):
        self.G = nx.DiGraph()
        self.traversal = traversal
        self.parent = parent
        self.positions = {}
        self.drawgraph()

    def drawgraph(self):
        self.G.clear()
        self.positions.clear()

        x_gap = 2
        y_gap = 2
        x_pos_counter = [0]  # mutable to track current x position
        visited = set()

        def dfspos(node, depth):
            if node in visited:
                return
            visited.add(node)

            x = x_pos_counter[0]
            y = -depth * y_gap
            self.positions[node] = (x, y)
            self.G.add_node(node)

            x_pos_counter[0] += x_gap

            for child in self.traversal:
                if self.parent.get(child) == node:
                    self.G.add_edge(node, child)
                    dfspos(child, depth + 1)

        root = (0, 0)
        dfspos(root, 0)

        plt.figure(figsize=(14, 8))
        nx.draw(self.G, pos=self.positions, with_labels=True,
                node_color='lightgreen', node_size=2000,
                font_size=10, font_weight='bold', arrows=True)
        plt.title("DFS Traversal Tree of Water Jug Problem")
        plt.show()

if __name__ == "__main__":
    a = int(input("Enter capacity of Jug 1: "))
    b = int(input("Enter capacity of Jug 2: "))
    c = int(input("Enter the target amount: "))

    solver = waterjug(a, b, c)
    traversal = solver.dfs()

    print("\nDFS traversal path:")
    print(" -> ".join(str(state) for state in traversal))

    display(traversal, solver.parent)
