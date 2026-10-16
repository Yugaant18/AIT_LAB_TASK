
from collections import deque

# File system represented using an adjacency list
graph = {
    "Root": ["A", "B"],
    "A": ["C", "D"],
    "B": ["E"],
    "C": [],
    "D": [],
    "E": []
}

visited = set()
queue = deque(["Root"])

print("File System Explorer using BFS:")
print("Folders in level-by-level order:")

while queue:
    node = queue.popleft()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

print()
