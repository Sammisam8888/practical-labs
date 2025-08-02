class Node:
    def __init__(self,paths=[]):
        self.paths=paths

nodes={}
n=int(input("Enter the number of nodes : "))

print("Enter the name of nodes : ")
for i in range(n):
    name = input(f"Name {i+1}: ")
    nodes[name] = Node()

print("Enter the paths : ")
for i in range(n):
    name = input(f"Name {i+1}: ")
    paths = input(f"Paths {i+1}: ").split()
    nodes[name].paths = paths

start = input("Enter the initial node : ")
stop=input("Enter the final node : ")

if start not in nodes or stop not in nodes:
    print("Invalid start or stop node")
    exit(0)

visited = set()
queue = [start]
visited.add(start)
found=0
print("BFS path traversal : ", end=" ")
while queue:
    node = queue.pop(0)
    
    for path in nodes[node].paths:
        if path not in visited:
            visited.add(path)
            queue.append(path)
            
    if node == stop:
        print(node, end="*\n")
        found=1
        break
    else :
        print(node, end="->")
    
if (found==0):
    print("Path not found from source to destination state")