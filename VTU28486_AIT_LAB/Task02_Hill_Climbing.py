
# Task 2: Network Signal Strength using Hill Climbing

signals = [20, 35, 50, 45, 60, 55]

current = 0
path = [signals[current]]

while current < len(signals) - 1:
    if signals[current + 1] > signals[current]:
        current += 1
        path.append(signals[current])
    else:
        break

print("Path:", path)
print("Best Signal:", signals[current])
