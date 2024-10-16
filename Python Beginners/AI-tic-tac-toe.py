import random
import time


# For displaying the game board
def display(grid):
    for row in range(3):
        print(" | ", end="")
        for column in range(3):
            if grid[row][column] == 0:
                print(" ", end="")
            else:
                print(grid[row][column], end="")
            print(" | ", end="")
        print("")


# For checking available moves
def available_moves(grid):
    moves = []
    for row in range(3):
        for column in range(3):
            if grid[row][column] not in ["X", "O"]:
                moves.append(grid[row][column])
    return moves


# For checking who's the winner
def check_winner(grid, player):
    # Checking for row or column win
    for i in range(3):
        if all(grid[i][j] == player for j in range(3)) or all(
                grid[j][i] == player for j in range(3)):
            return True

    # Checking for diagonal win
    if all(grid[i][i] == player for i in range(3)) or all(grid[i][2 - i] == player for i in range(3)):
        return True

    return False


# For checking whether the board is full
def no_move_remaining(grid):
    count = 0
    for row in range(3):
        for column in range(3):
            if grid[row][column] in ["X", "O"]:
                count = count + 1
    if count == 9:
        return True
    return False


def make_move(positions, pattern, position, move):
    for row in range(3):
        for column in range(3):
            if positions[row][column] == position:
                pattern[row][column] = move
                return True
    return False


# Unbeatable AI player
def ai_move(positions, pattern):
    # Checking for available positions
    available_positions = available_moves(positions)

    # Checking two-way win situation
    if 1 not in available_positions and 9 not in available_positions and len(available_positions) == 6:
        return random.choice([2, 8])

    if 3 not in available_positions and 7 not in available_positions and len(available_positions) == 6:
        return random.choice([4, 6])

    # Checking for a winning move
    for position in available_positions:
        temp_pattern = [row[:] for row in pattern]
        if make_move(positions, temp_pattern, position, "O") and check_winner(temp_pattern, "O"):
            return position

    # If no winning move, checking to block user's move
    for position in available_positions:
        temp_pattern = [row[:] for row in pattern]
        if make_move(positions, temp_pattern, position, "X") and check_winner(temp_pattern, "X"):
            return position

    # Strategic moves
    strategic_moves = [5, 1, 3, 7, 9, 2, 4, 6, 8]
    for position in strategic_moves:
        if position in available_positions:
            return position

    # If no strategic move is possible, make a random move
    return random.choice(available_positions)


# Template for the positions on the board
positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("The position for each box is as follows : ")
display(positions)

pattern = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

choice = input("Do you wish to start the game?(Y/N) : ")
if choice == "Y":
    chance = "user"
else:
    chance = "ai"

while True:
    # User's move
    if chance == "user":
        user_move = int(input("Enter your move position: "))
        if user_move in available_moves(positions):
            make_move(positions, pattern, user_move, "X")
            make_move(positions, positions, user_move, "X")
            display(pattern)
            print()

            if check_winner(pattern, "X"):
                print("Congratulations! You win!")
                break

            elif no_move_remaining(pattern):
                print("Its a tie!")
                break

            chance = "ai"

        else:
            print("Invalid move! Please enter an available position")
            chance = "user"

    # AI player's move
    else:
        print("AI player is thinking", end="")
        time.sleep(0.2)
        print(".",end="")
        time.sleep(0.2)
        print(".", end="")
        time.sleep(0.2)
        print(".")
        time.sleep(0.3)
        ai_position = ai_move(positions, pattern)
        make_move(positions, pattern, ai_position, "O")
        make_move(positions, positions, ai_position, "O")
        display(pattern)
        print()

        if check_winner(pattern, "O"):
            print("AI wins!")
            break

        elif no_move_remaining(pattern):
            print("Its a tie!")
            break

        chance = "user"
