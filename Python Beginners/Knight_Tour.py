# Size of the chessboard (8x8 for a standard chessboard)
N = 8

# Utility function to check if the move is valid
def is_safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

# Utility function to print the solution
def print_solution(board):
    for row in board:
        for col in row:
            print(f"{col:2}", end=" ")
        print()

# Solves the Knight's Tour problem using backtracking
def solve_knights_tour():
    # Initialize the chessboard with -1
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # The knight's possible movements (x, y)
    # Move sequences correspond to 8 possible L-shaped moves for a knight
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Starting position for the knight
    board[0][0] = 0  # Start at the top-left corner (0, 0)

    # Start the knight tour from the initial position (0, 0)
    if not solve_knights_tour_util(0, 0, 1, board, move_x, move_y):
        print("No solution exists")
    else:
        print_solution(board)

# Recursive utility function to solve the Knight's Tour problem
def solve_knights_tour_util(x, y, move_i, board, move_x, move_y):
    # Base case: if all squares are visited, return True
    if move_i == N * N:
        return True

    # Try all next moves from the current x, y position
    for k in range(8):
        next_x = x + move_x[k]
        next_y = y + move_y[k]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = move_i
            if solve_knights_tour_util(next_x, next_y, move_i + 1, board, move_x, move_y):
                return True
            # Backtrack if the move doesn't lead to a solution
            board[next_x][next_y] = -1

    return False

# Driver code
if __name__ == "__main__":
    solve_knights_tour()
