
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

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(neighbour)

print("File System Explorer using DFS:")
print("Folders in depth-first order:")

dfs("Root")
print()
