# CSP using Backtracking for Frequency Assignment

graph = {
    'V1': ['V2', 'V3'],
    'V2': ['V1', 'V3', 'V4'],
    'V3': ['V1', 'V2', 'V4'],
    'V4': ['V2', 'V3']
}

colors = [1, 2, 3]
assignment = {}


def is_safe(vertex, color):
    for neighbor in graph[vertex]:
        if assignment.get(neighbor) == color:
            return False
    return True


def backtrack(vertices):
    if not vertices:
        return True

    vertex = vertices[0]

    for color in colors:
        if is_safe(vertex, color):
            assignment[vertex] = color

            if backtrack(vertices[1:]):
                return True

            del assignment[vertex]

    return False


vertices = list(graph.keys())

if backtrack(vertices):
    print("Valid Frequency Assignment:")
    for vertex in vertices:
        print(vertex, "->", assignment[vertex])
else:
    print("No valid assignment exists")