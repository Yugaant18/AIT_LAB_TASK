
import random

# Distance matrix between locations
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

locations = ['A', 'B', 'C', 'D']

best_route = None
best_distance = float('inf')

# Try 100 randomly generated routes
for _ in range(100):
    route = list(range(4))
    random.shuffle(route)

    total_distance = 0

    for i in range(3):
        total_distance += distance[route[i]][route[i + 1]]

    # Return to the starting location
    total_distance += distance[route[3]][route[0]]

    if total_distance < best_distance:
        best_distance = total_distance
        best_route = route[:]

print("Best route:")

for i in best_route:
    print(locations[i], end=" ")

print(locations[best_route[0]])
print("Minimum distance:", best_distance)
