class Node:
    def __init__(self, paths=None):
        if paths is None:
            paths = []
        self.paths = paths

nodes = {}
n = int(input("Enter the number of nodes: "))

print("Enter the names of nodes:")
for i in range(n):
    name = input(f"Name {i+1}: ")
    nodes[name] = Node()

print("Enter the paths:")
for i in range(n):
    name = input(f"From node {i+1} ({list(nodes.keys())[i]}): ")
    paths = input(f"Paths from {name} (space-separated): ").split()
    nodes[name].paths = paths

start = input("Enter the initial node: ")
stop = input("Enter the final node: ")

if start not in nodes or stop not in nodes:
    print("Invalid start or stop node.")
    exit(0)

visited = set()
queue = [start]
visited.add(start)

parent = {start: None}  # To store the path

found = False

while queue:
    node = queue.pop(0)
    if node == stop:
        found = True
        break
    for neighbor in nodes[node].paths:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
            parent[neighbor] = node

if found:
    # Reconstruct the path
    path = []
    current = stop
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    
    print("BFS path traversal:", " -> ".join(path), "*")
else:
    print("Path not found from source to destination state.")
