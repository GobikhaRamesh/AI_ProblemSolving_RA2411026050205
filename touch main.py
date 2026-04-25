import math

# Create empty board
board = [" " for _ in range(9)]

# Print Board
def print_board():
    print()
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
    print()

# Check winner
def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_positions)

# Check draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Best move for AI
def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        board[move] = "O"

# Game loop
def play_game():
    print("🎮 Tic Tac Toe - You (X) vs AI (O)")
    print("Positions:")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")

    while True:
        print_board()

        try:
            user_move = int(input("Enter position (1-9): ")) - 1
            if user_move < 0 or user_move > 8 or board[user_move] != " ":
                print("❌ Invalid move! Try again.")
                continue
        except ValueError:
            print("❌ Please enter a number between 1 and 9.")
            continue

        board[user_move] = "X"

        if check_winner("X"):
            print_board()
            print("🎉 You win!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a draw!")
            break

        best_move()

        if check_winner("O"):
            print_board()
            print("🤖 AI wins!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a draw!")
            break

# Run game
if __name__ == "__main__":
    play_game()