import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
# intermediate deepening depth first search
# algorithm
# begin
# 1.put current depth cut off to 1
# 2.put the initial node into stack pointed by stack top
# 4.while stack  is not empty and the depth is within the depth cutoff{
# 5.   pop the stack to get stack top element
# 6.   if (stack.top==goal){
# 7.      return it and exit
# 8.  else otherwise{
# 9.      push the children of stack top in any order into the stack
# 10.increment the deptisempty cutoff by one and repeat step 2
# }    
# }           
# }

class Stack():
    def __init__(self):
        self.states = []

    def isempty(self):
        return len(self.states) == 0

    def push(self, coord):
        self.states.append(coord)
        

    def pop(self):
        if not self.isempty():
            return self.states.pop()
        else:
            return None

def nodes(state, levels):
    x, y = state
    xlevel, ylevel = levels
    node = []

    node.append((xlevel, y))           
    node.append((x, ylevel))            
    node.append((0, y))                 
    node.append((x, 0))                 
    nxt = min(x, ylevel - y)            
    node.append((x - nxt, y + nxt))
    nxt = min(y, xlevel - x)            
    node.append((x + nxt, y - nxt))

    return list(set(node))

def tree(g, prev_node, start, goal):
    pos = graphviz_layout(g, prog='dot')
    plt.figure(figsize=(12, 9))
    nx.draw(g, pos, with_labels=True, node_color='lightyellow', node_size=600, font_size=9, arrows=True)

    if goal in prev_node:
        path = []
        target = goal
        while target is not None:
            path.append(target)
            target = prev_node[target]
        path.reverse()
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(g, pos, edgelist=edges, edge_color='green', width=3)

    plt.title("IDDFS Tree")
    plt.show()
    
def iddfs(start, goal, levels,cutoff):
    s = Stack()
    s.push((start, 1))
    vis = set([start])
    prev_node = {start: None}
    g = nx.DiGraph()
    
    while not s.isempty():
        top,depth=s.pop()
        if top==goal:
            g, prev_node,True
        if(depth<cutoff):
            for child in nodes(top, levels):
                if child not in vis:
                    vis.add(child)
                    prev_node[child] = top
                    g.add_edge(top, child)
                    s.push((child,depth+1))
        
            
    return g, prev_node,False


if __name__ == "__main__":
    print("Water Jug Problem \n")
    jug1 = int(input("Enter level of water in Jug 1: "))
    jug2 = int(input("Enter level of water in Jug 2: "))

    print("Enter start state (x,y):")
    start = tuple(map(int, input().split(",")))

    print("Enter goal state (x,y):")
    goal = tuple(map(int, input().split(",")))

    
    cutoff=int(input("Enter depth cutoff: "))
    levels = (jug1, jug2)
    # g, prev_node = iddfs(start, goal, levels,cutoff)
    g, prev_node,b = iddfs(start, goal, levels,cutoff)
    print(b)
    print("\nNodes visited:")
    print(list(prev_node.keys()))

    if goal in prev_node:
        path = []
        target = goal
        while target:
            path.append(target)
            target = prev_node[target]
        path.reverse()
        print("Solution - path traversed:", " -> ".join(map(str, path)))
        tree(g, prev_node, start, goal)
    else:
        print("No solution.")