
import heapq

# Grid: 0 = free cell, 1 = obstacle
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

pq = [(0, start)]
parent = {start: None}
g_cost = {start: 0}

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while pq:
    f, current = heapq.heappop(pq)

    if current == goal:
        break

    r, c = current

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if (0 <= nr < 5 and 0 <= nc < 5
                and grid[nr][nc] == 0):

            next_cell = (nr, nc)
            new_cost = g_cost[current] + 1

            if (next_cell not in g_cost
                    or new_cost < g_cost[next_cell]):

                g_cost[next_cell] = new_cost

                h = abs(nr - goal[0]) + abs(nc - goal[1])
                f = new_cost + h

                heapq.heappush(pq, (f, next_cell))
                parent[next_cell] = current

# Reconstruct the shortest path
path = []
current = goal

if current in parent:
    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Shortest Path:")
    print(path)
    print("Total Cost:", g_cost[goal])
else:
    print("No path found.")
