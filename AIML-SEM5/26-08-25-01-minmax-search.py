import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import io
from PIL import Image

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

def evaluate(state, goal):
    return -(abs(goal[0]-state[0]) + abs(goal[1]-state[1]))

def minimax_search(state, levels, goal, depth=4, maximizing=True, alpha=-1e9, beta=1e9, g=None, prev_node=None, g_score=None, d=0, step_images=None, visited=None):
    if g is None:
        g = nx.DiGraph()
    if prev_node is None:
        prev_node = {}
    if g_score is None:
        g_score = {}
    if step_images is None:
        step_images = []
    if visited is None:
        visited = set()

    # Early termination if goal found
    if state == goal:
        if state not in g.nodes():
            g.add_node(state)
            g_score[state] = evaluate(state, goal)
        return evaluate(state, goal), state, step_images

    # Avoid cycles and limit search
    if state in visited or depth == 0:
        if state not in g.nodes():
            g.add_node(state)
            g_score[state] = evaluate(state, goal)
        return evaluate(state, goal), state, step_images
    
    visited.add(state)
    g.add_node(state)
    g_score[state] = evaluate(state, goal)

    # Limit visualizations to prevent slowdown
    if len(step_images) < 15 and d <= 3:  # Only visualize first few levels
        try:
            step_images.append(draw(g, prev_node, state, goal, g_score, d, state))
        except:
            print(f"Skipping visualization at depth {d}")

    # Get valid children and limit exploration
    children = get_node(state, levels)
    children = [child for child in children if child not in visited][:4]  # Limit to 4 children max

    if maximizing:
        best_score = -1e9
        best_state = state
        for child in children:
            if child not in g.nodes():
                g.add_edge(state, child)
                if child not in prev_node:
                    prev_node[child] = state
                
                score, _, step_images = minimax_search(child, levels, goal, depth-1, False, alpha, beta, g, prev_node, g_score, d+1, step_images, visited)
                
                if score > best_score:
                    best_score = score
                    best_state = child
                
                alpha = max(alpha, score)
                if beta <= alpha:  # Alpha-beta pruning
                    break
                    
        visited.remove(state)
        return best_score, best_state, step_images
    else:
        best_score = 1e9
        best_state = state
        for child in children:
            if child not in g.nodes():
                g.add_edge(state, child)
                if child not in prev_node:
                    prev_node[child] = state
                
                score, _, step_images = minimax_search(child, levels, goal, depth-1, True, alpha, beta, g, prev_node, g_score, d+1, step_images, visited)
                
                if score < best_score:
                    best_score = score
                    best_state = child
                
                beta = min(beta, score)
                if beta <= alpha:  # Alpha-beta pruning
                    break
                    
        visited.remove(state)
        return best_score, best_state, step_images

def draw(G, prev, start, goal, g_score, d, cur):
    try:
        # Use simpler layout if graphviz fails
        try:
            pos = graphviz_layout(G, prog='dot')
        except:
            pos = nx.spring_layout(G, seed=42)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        lbls = {n: f"{n}\nV={g_score.get(n, 0)}" for n in G.nodes()}
        nx.draw(G, pos, labels=lbls, with_labels=True, node_color='lightpink', 
                node_size=1500, font_size=10, ax=ax)

        # Draw path if exists
        if cur in prev:
            p = []
            t = cur
            path_length = 0
            while t is not None and path_length < 10:  # Limit path length
                p.append(t)
                t = prev.get(t)
                path_length += 1
            p.reverse()
            if len(p) > 1:
                e = [(p[i], p[i+1]) for i in range(len(p)-1)]
                nx.draw_networkx_edges(G, pos, edgelist=e, edge_color='green', width=3, ax=ax)

        # Highlight special nodes
        nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color='lightblue', node_size=1800, ax=ax)
        if goal in G.nodes():
            nx.draw_networkx_nodes(G, pos, nodelist=[goal], node_color='lightcoral', node_size=1800, ax=ax)
        
        ax.set_title(f"Minimax Search - Step {d}")
        
        # Convert to image
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', dpi=80)
        buf.seek(0)
        img = Image.open(buf)
        plt.close(fig)
        return img
    except Exception as e:
        print(f"Error in draw at step {d}: {e}")
        # Return a blank image if drawing fails
        blank = Image.new('RGB', (800, 600), 'white')
        return blank

def final_path(G, prev_node, start, goal, g_score):
    try:
        try:
            pos = graphviz_layout(G, prog='dot')
        except:
            pos = nx.spring_layout(G, seed=42)
            
        fig, ax = plt.subplots(figsize=(10, 8))
        lbls = {n: f"{n}\nV={g_score.get(n, 0)}" for n in G.nodes()}
        nx.draw(G, pos, labels=lbls, with_labels=True, node_color='orange', 
                node_size=1500, font_size=10, ax=ax)

        if goal in prev_node:
            path = []
            t = goal
            while t is not None and len(path) < 20:
                path.append(t)
                t = prev_node.get(t)
            path.reverse()
            if len(path) > 1:
                e = [(path[i], path[i+1]) for i in range(len(path)-1)]
                nx.draw_networkx_edges(G, pos, edgelist=e, edge_color='green', width=3, ax=ax)
            print("Final Path:", " -> ".join(map(str, path[:10])))  # Limit output

        nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color='lightblue', node_size=1800, ax=ax)
        if goal in G.nodes():
            nx.draw_networkx_nodes(G, pos, nodelist=[goal], node_color='lightcoral', node_size=1800, ax=ax)
        ax.set_title("Final Minimax Path")
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', dpi=80)
        buf.seek(0)
        img = Image.open(buf)
        plt.close(fig)
        return img
    except Exception as e:
        print(f"Error in final_path: {e}")
        blank = Image.new('RGB', (1000, 800), 'white')
        return blank

def combine_images(images):
    if not images:
        return None
    
    # Filter out None images
    images = [img for img in images if img is not None]
    if not images:
        return None
    
    n_images = len(images)
    cols = min(3, n_images)
    rows = (n_images + cols - 1) // cols
    
    max_width = max(img.width for img in images)
    max_height = max(img.height for img in images)
    
    combined_width = cols * max_width
    combined_height = rows * max_height
    combined_img = Image.new('RGB', (combined_width, combined_height), 'white')
    
    for i, img in enumerate(images):
        row = i // cols
        col = i % cols
        x = col * max_width + (max_width - img.width) // 2
        y = row * max_height + (max_height - img.height) // 2
        combined_img.paste(img, (x, y))
    
    return combined_img

if __name__ == "__main__":
    print("Water Jug Problem - Optimized Minimax Search\n")
    a = int(input("Enter capacity of Jug 1: "))
    b = int(input("Enter capacity of Jug 2: "))
    t = int(input("Enter target level: "))

    levels = (a, b)
    start = (0, 0)
    goal = (t, 0)
    
    print(f"\nSearching from {start} to {goal} with jugs of capacity {levels}")
    print("This may take a moment...\n")

    try:
        g = nx.DiGraph()
        prev_node = {}
        g_score = {}
        step_images = []

        score, best_state, step_images = minimax_search(
            start, levels, goal, depth=4, maximizing=True, 
            g=g, prev_node=prev_node, g_score=g_score, step_images=step_images
        )
        
        print(f"Search completed! Best score: {score}, Best state: {best_state}")
        
        # Generate final path image
        final_img = final_path(g, prev_node, start, goal, g_score)
        step_images.append(final_img)
        
        # Combine all images
        print(f"Generated {len(step_images)} visualization steps")
        combined_image = combine_images(step_images)
        
        if combined_image:
            plt.figure(figsize=(16, 12))
            plt.imshow(combined_image)
            plt.axis('off')
            plt.title("Minimax Search Algorithm - All Steps Combined", fontsize=14, pad=20)
            plt.tight_layout()
            plt.show()
            
            combined_image.save("minimax_water_jug_combined.png")
            print("\nCombined image saved as 'minimax_water_jug_combined.png'")
        else:
            print("No images to combine")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Try with smaller jug capacities or target values.")