import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

def get_node(state, levels):
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



def minmax(state, depth, maximizingplayer, levels):
    if depth == 0 or state == levels :
        return evaluate(state)
    
    if maximizingplayer:
        bestscore = -1e9
        for child in get_node(state, levels):
            score = minmax(child, depth -1,False,levels)
            bestscore = max(bestscore, score)
        return bestscore
    else:
        bestscore = 1e9
        for child in get_node(state, levels):
            score = minmax(child, depth -1,True,levels)
            bestscore = min(bestscore, score)
        return bestscore
    
def evaluate(state):
    return state[0] - state[1]


def draw_graph(g, prev_node, start, goal, g_score, depth, current):
    pos = graphviz_layout(g, prog='dot')
    plt.figure(figsize=(10, 7))

    
    labels = {node: f"{node}\nh={heuristic(node, goal)}" for node in g.nodes()}
    nx.draw(g, pos, labels=labels, with_labels=True,
            node_color='lightyellow', node_size=700, font_size=8)

    
    edge_labels = {(u, v): g_score[v] for u, v in g.edges()}
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=7)

    
    if current in prev_node:
        path = []
        target = current
        while target is not None:
            path.append(target)
            target = prev_node[target]
        path.reverse()
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(g, pos, edgelist=edges, edge_color='green', width=3)

    
    nx.draw_networkx_nodes(g, pos, nodelist=[start], node_color='lightblue', node_size=800)

    
    if goal in g.nodes():
        nx.draw_networkx_nodes(g, pos, nodelist=[goal], node_color='lightcoral', node_size=800)

    plt.title(f"Minmax Search - Depth {depth}")
    plt.show()

def final_path(g, prev_node, start, goal, g_score):
    pos = graphviz_layout(g, prog='dot')
    plt.figure(figsize=(12, 9))

    labels = {node: f"{node}\nh={heuristic(node, goal)}" for node in g.nodes()}
    nx.draw(g, pos, labels=labels, with_labels=True,
            node_color='lightyellow', node_size=700, font_size=8)

    edge_labels = {(u, v): g_score[v] for u, v in g.edges()}
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=7)

    if goal in prev_node:
        path = []
        target = goal
        while target is not None:
            path.append(target)
            target = prev_node[target]
        path.reverse()
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(g, pos, edgelist=edges, edge_color='green', width=3)
        print("Final Solution Path:", " -> ".join(map(str, path)))

    
    nx.draw_networkx_nodes(g, pos, nodelist=[start], node_color='lightblue', node_size=800)

    
    if goal in g.nodes():
        nx.draw_networkx_nodes(g, pos, nodelist=[goal], node_color='lightcoral', node_size=800)

    plt.title("Final Minmax Path")
    plt.show()

if __name__ == "__main__":
    print("Water Jug Problem - Minmax Search\n")
    a=int(input("Enter level of water in Jug 1: "))
    b=int(input("Enter level of water in Jug 2: "))
    t=int(input("Enter target level:")); 
    gl=(t,0); st=(0,0)
    levels = (a, b)
    g, prev_node, g_score = minmax(st, gl, levels)
    final_path(g, prev_node, st, gl, g_score)