
import math

def minimax(tree, depth, maximizing, alpha, beta):
    if not isinstance(tree, list):
        return tree

    if maximizing:
        best = -math.inf

        for child in tree:
            value = minimax(child, depth + 1, False, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:
        best = math.inf

        for child in tree:
            value = minimax(child, depth + 1, True, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)

            if alpha >= beta:
                break

        return best


game_tree = [[3, 5], [2, 9], [4, 1]]

best_score = -math.inf
best_shot = 0

for i, shot in enumerate(game_tree):
    score = minimax(shot, 0, False, -math.inf, math.inf)
    print("Shot", i + 1, ":", score)

    if score > best_score:
        best_score = score
        best_shot = i + 1

print("Best shooting strategy: Shot", best_shot)
print("Best score:", best_score)
