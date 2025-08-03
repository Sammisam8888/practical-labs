import turtle
from collections import deque
import time

def get_children(x, y, jug1, jug2):
    children = []
    children.append((jug1, y))     # Fill Jug 1
    children.append((x, jug2))     # Fill Jug 2
    children.append((0, y))        # Empty Jug 1
    children.append((x, 0))        # Empty Jug 2
    pour = min(x, jug2 - y)
    children.append((x - pour, y + pour))  # Jug1 → Jug2
    pour = min(y, jug1 - x)
    children.append((x + pour, y - pour))  # Jug2 → Jug1
    return children

def bfswaterjug(jug1, jug2, target):
    visited = set()
    queue = deque()
    parent = dict()

    start = (0, 0)
    queue.append(start)
    visited.add(start)
    found = None

    while queue:
        current = queue.popleft()
        if target in current:
            found = current
            break
        for child in get_children(current[0], current[1], jug1, jug2):
            if child not in visited:
                visited.add(child)
                queue.append(child)
                parent[child] = current

    if not found:
        print("No solution found.")
        return

    # Build path
    path = []
    while found != (0, 0):
        path.append(found)
        found = parent[found]
    path.append((0, 0))
    path.reverse()

    print("\nBFS path traversal:", end=" ")
    for i in range(len(path)):
        if i == len(path) - 1:
            print(path[i], end=" *\n")
        else:
            print(path[i], end=" -> ")

    draw_tree(path)

def draw_tree(path):
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()

    radius = 35
    step_x = 100
    step_y = 100

    node_positions = {}
    x = 0
    y = 0

    for i, node in enumerate(path):
        pos = (x, y)
        node_positions[node] = pos

        t.penup()
        t.goto(x, y)
        t.pendown()

        # Draw circle
        t.fillcolor("lightblue")
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

        # Write state
        t.penup()
        t.goto(x, y + radius + 5)
        t.write(str(node), align="center", font=("Arial", 10, "bold"))

        # Draw edge to next node
        if i < len(path) - 1:
            x_next, y_next = x + step_x, y - step_y
            t.goto(x, y - radius)
            t.pendown()
            t.goto(x_next, y_next + radius)
            x, y = x_next, y_next

    t.hideturtle()
    screen.title("Water Jug BFS Tree")
    screen.mainloop()

if __name__ == "__main__":
    jug1 = int(input("Enter capacity of Jug 1: "))
    jug2 = int(input("Enter capacity of Jug 2: "))
    target = int(input("Enter the target amount: "))
    bfswaterjug(jug1, jug2, target)
