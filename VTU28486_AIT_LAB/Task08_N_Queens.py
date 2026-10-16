
# Task 8: N-Queens Problem using Backtracking

N = 4

def print_solution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def is_safe(board, row, col):
    # Check the same row on the left
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, N),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    # All queens have been placed
    if col >= N:
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queens(board, col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False

def solve_n():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_n_queens(board, 0):
        print("Solution does not exist")
        return

    print("N-Queens Solution:")
    print_solution(board)

solve_n()
