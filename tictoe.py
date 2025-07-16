# Friendly move names to board positions
positions = {
    "top left": 0, "top": 1, "top right": 2,
    "left": 3, "center": 4, "right": 5,
    "bottom left": 6, "bottom": 7, "bottom right": 8
}

# Function to print the board
def show_board(b):
    print(f"{b[0]} | {b[1]} | {b[2]}")
    print("--+---+--")
    print(f"{b[3]} | {b[4]} | {b[5]}")
    print("--+---+--")
    print(f"{b[6]} | {b[7]} | {b[8]}\n")

# Check if a player has won
def check_win(b, player):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),
            (1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[i] == b[j] == b[k] == player for i,j,k in wins)

# Minimax algorithm with full depth simulation
def minimax(board, is_ai):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if ' ' not in board:
        return 0  # Draw

    if is_ai:
        best = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = ' '
                best = max(best, score)
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = ' '
                best = min(best, score)
        return best

# AI chooses the move with best Minimax score
def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Start the game
board = [' '] * 9
print("You = X | AI = O")
print("Type your move like: top left, center, bottom right")

while True:
    show_board(board)
    move = input("Your move: ").strip().lower()

    if move not in positions:
        print("Invalid input. Try again.\n")
        continue

    idx = positions[move]
    if board[idx] != ' ':
        print("That spot is taken. Try again.\n")
        continue

    board[idx] = 'X'

    if check_win(board, 'X'):
        show_board(board)
        print(" You win!")
        break
    if ' ' not in board:
        show_board(board)
        print(" It's a draw!")
        break

    ai_idx = best_move(board)
    board[ai_idx] = 'O'
    print("🤖 AI played.\n")

    if check_win(board, 'O'):
        show_board(board)
        print(" AI wins!")
        break
    if ' ' not in board:
        show_board(board)
        print(" It's a draw!")
        break


