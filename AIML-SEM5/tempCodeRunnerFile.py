import matplotlib.pyplot as plt
import networkx as nx

class waterjug:
    def __init__(self, jug1, jug2, target):
        self.jug1 = jug1
        self.jug2 = jug2
        self.target = target
        self.visited = set()
        self.parent = {}
        self.expansion_order = []  # Track the order of node expansion
        

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
        self.expansion_order = []  # Reset expansion order

        last_depth = -1
        while open_list:
            # Sort by f value (lowest first)
            open_list.sort(key=lambda x: x[2])
            node, depth, f_val = open_list.pop(0)

            if node in closed_set:
                continue
            closed_set.add(node)
            self.expansion_order.append(node)  # Track expansion order

            # Print/display at each step: show all expanded nodes so far
            if show_step_by_step:
                print(f"\nA* Step {len(closed_set)} (expanding node {node}):")
                print("Expanded nodes so far:")
                print(", ".join(str(n) for n in closed_set))

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

            for child in self.getchildren(*node):
                if child not in closed_set and child not in [n[0] for n in open_list]:
                    self.parent[child] = node
                    open_list.append([child, depth + 1, self.f(child, depth + 1)])
        # If no solution found
        return []

def plot_astar_traversal_progressive(traversal, parent, expansion_order):
    """
    Display the A* algorithm step by step, showing only nodes explored up to each step.
    """
    import matplotlib.pyplot as plt
    import networkx as nx
    
    snaps = []
    
    # Create snapshots for each expansion step
    for i in range(len(expansion_order)):
        # Nodes explored up to this step
        explored_so_far = set(expansion_order[:i+1])
        
        # Create graph with only explored nodes and their connections
        G = nx.DiGraph()
        
        # Add nodes that have been explored so far
        for node in explored_so_far:
            G.add_node(node)
        
        # Add edges between explored nodes
        for child, par in parent.items():
            if par is not None and child in explored_so_far and par in explored_so_far:
                G.add_edge(par, child)
        
        # Find solution path up to current node if it exists
        current_node = expansion_order[i]
        partial_solution = []
        if current_node in traversal:
            # Get path from start to current node
            sol_index = traversal.index(current_node)
            partial_solution = traversal[:sol_index+1]
        
        snap = {
            'G': G.copy(),
            'explored': explored_so_far.copy(),
            'solution_path': partial_solution.copy(),
            'current_node': current_node,
            'step': i+1
        }
        snaps.append(snap)

    total = len(snaps)
    cols = 3
    rows = (total + cols - 1) // cols
    plt.figure(figsize=(cols * 6, rows * 5), constrained_layout=True)

    def tree_layout(G, root, width=1., gap=0.2, y=0, x=0.5):
        if root not in G.nodes():
            return {}
        pos = {root: (x, y)}
        kids = list(G.successors(root))
        if not kids:
            return pos
        dx = width / len(kids) if len(kids) > 0 else width
        next_x = x - width / 2 + dx / 2
        for kid in kids:
            pos.update(tree_layout(G, kid, width=dx, gap=gap, y=y - gap, x=next_x))
            next_x += dx
        return pos

    for i, snap in enumerate(snaps):
        plt.subplot(rows, cols, i + 1)
        G_snap = snap['G']
        explored = snap['explored']
        solution_path = snap['solution_path']
        current_node = snap['current_node']
        step = snap['step']
        
        if len(G_snap.nodes()) == 0:
            continue
            
        pos = tree_layout(G_snap, (0, 0))
        
        # Color nodes based on their status
        node_colors = []
        for n in G_snap.nodes():
            if n == current_node:
                node_colors.append('lightblue')  # Currently expanding node
            elif n in solution_path:
                node_colors.append('lightgreen')  # Part of solution path
            else:
                node_colors.append('lightcoral')  # Explored but not in solution
        
        # Draw the graph
        nx.draw(G_snap, pos, with_labels=True, node_color=node_colors,
                node_size=700, font_size=8, edge_color='gray')
        
        # Highlight solution path edges if they exist
        if len(solution_path) > 1:
            path_edges = list(zip(solution_path, solution_path[1:]))
            # Only draw edges that exist in current graph
            valid_path_edges = [(u, v) for u, v in path_edges if G_snap.has_edge(u, v)]
            if valid_path_edges:
                nx.draw_networkx_edges(G_snap, pos, edgelist=valid_path_edges,
                                       edge_color='green', width=3)
        
        plt.title(f"A* Step {step} - Expanding {current_node}", fontsize=12)
        plt.axis('off')
    
    plt.suptitle("A* Water Jug Solution - Progressive Exploration", fontsize=16, y=1.02)
    plt.savefig("astar-progressive-exploration.png", dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    a = int(input("Enter capacity of Jug 1: "))
    b = int(input("Enter capacity of Jug 2: "))
    c = int(input("Enter the target amount: "))

    solver = waterjug(a, b, c)
    traversal = solver.astar(show_step_by_step=True)

    print("\nA* traversal path:")
    print(" -> ".join(str(state) for state in traversal))

    # Show progressive step-by-step exploration
    plot_astar_traversal_progressive(traversal, solver.parent, solver.expansion_order)