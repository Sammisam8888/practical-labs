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
        states.append((self.jug1, y))
        states.append((x, self.jug2))
        states.append((0, y))
        states.append((x, 0))
        pour = min(x, self.jug2 - y)
        states.append((x - pour, y + pour))
        pour = min(y, self.jug1 - x)
        states.append((x + pour, y - pour))
        return [state for state in states if self.check(*state)]

    def fvalue(self, state):
        x, y = state
        return abs(x - self.target) + abs(y - 0) 

    def hillclimb(self):
        stack=[]
        traversal=[]
        traversalf=[]
        rejected=[(0,0)]
        rejectedf=[self.fvalue((0,0))]
        stack.append((0,0))
        while stack:
            top=stack.pop()
            traversal.append(top)
            traversalf.append(self.fvalue(top))
            self.visited.add(top)
            if (top[0]==self.target and top[1]==0) or (top[1]==self.target and top[0]==0):
                return (traversal,traversalf,rejected,rejectedf)
            
            nextstates=self.getchildren(*top)
            nextstates.sort(key=self.fvalue)

            for state in reversed(nextstates):  
                if state not in self.visited:
                    rejected.append(state)
                    rejectedf.append(self.fvalue(state))
                    self.visited.add(state)
                    stack.append(state)
                    self.parent[state] = top

        return (traversal,traversalf,rejected,rejectedf)

class display:
    def __init__(self, traversal, parent, traversalf, rejected, rejectedf):
        self.traversal = traversal
        self.traversalf = traversalf
        self.parent = parent
        self.rejected = rejected
        self.rejectedf = rejectedf

        self.draw_two_graphs()

    def draw_two_graphs(self):
        fig, axs = plt.subplots(1, 2, figsize=(18, 8))
        axs[0].set_title("Rejected Nodes (Rejected & Rejected f)")
        axs[1].set_title("Traversal Nodes (Traversal & Traversal f)")

        # Draw rejected graph
        G_rejected = nx.DiGraph()
        pos_rejected = self.get_positions(self.rejected, self.parent)
        for node in self.rejected:
            G_rejected.add_node(node)
            parent = self.parent.get(node)
            if parent:
                G_rejected.add_edge(parent, node)
        labels_rejected = {node: f"{node}\nf={self.rejectedf[i]}" for i, node in enumerate(self.rejected)}

        nx.draw(G_rejected, pos=pos_rejected, ax=axs[0], with_labels=True, labels=labels_rejected,
                node_color='lightcoral', node_size=1500, font_size=9, font_weight='bold', arrows=True)

        # Draw traversal graph
        G_traversal = nx.DiGraph()
        pos_traversal = self.get_positions(self.traversal, self.parent)
        for node in self.traversal:
            G_traversal.add_node(node)
            parent = self.parent.get(node)
            if parent:
                G_traversal.add_edge(parent, node)
        labels_traversal = {node: f"{node}\nf={self.traversalf[i]}" for i, node in enumerate(self.traversal)}

        nx.draw(G_traversal, pos=pos_traversal, ax=axs[1], with_labels=True, labels=labels_traversal,
                node_color='peachpuff', node_size=1500, font_size=9, font_weight='bold', arrows=True)

        plt.show()

    def get_positions(self, nodes, parent):
        # Assign levels based on BFS distance from root (0,0)
        levelmap = {}
        levelnodes = {}

        if not nodes:
            return {}

        root = (0,0)
        levelmap[root] = 0
        levelnodes[0] = [root]

        # We build levels using parents and nodes given
        for node in nodes:
            if node == root:
                continue
            p = parent.get(node)
            if p is not None and p in levelmap:
                level = levelmap[p] + 1
            else:
                # Orphan node or root itself, assign level 0 if missing
                level = 0
            levelmap[node] = level
            if level not in levelnodes:
                levelnodes[level] = []
            levelnodes[level].append(node)

        positions = {}
        ygap = 2
        xgap = 2
        for level in sorted(levelnodes.keys()):
            nodes_at_level = levelnodes[level]
            startx = - (len(nodes_at_level) - 1) * xgap / 2
            for i, node in enumerate(nodes_at_level):
                x = startx + i * xgap
                y = -level * ygap
                positions[node] = (x, y)
        return positions


if __name__ == "__main__":
    a = int(input("Enter capacity of Jug 1: "))
    b = int(input("Enter capacity of Jug 2: "))
    c = int(input("Enter the target amount: "))

    solver = waterjug(a, b, c)
    traversal, traversalf, rejected, rejectedf = solver.hillclimb()

    print("\nHill Climb traversal path:")
    print(" -> ".join(str(state) for state in traversal))

    display(traversal, solver.parent, traversalf, rejected, rejectedf)
