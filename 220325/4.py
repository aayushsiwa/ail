import math

# Constants for the players
PLAYER_X = 'X'  # Maximizing player (AI)
PLAYER_O = 'O'  # Minimizing player (Human)
EMPTY = ' '

# Check if a player has won
def check_winner(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != EMPTY:
            return board[a]  # Return winner ('X' or 'O')

    return None  # No winner yet

# Check if the board is full
def is_draw(board):
    return EMPTY not in board and check_winner(board) is None

# Evaluate the board for Minimax
def evaluate(board, depth):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 10 - depth  # Prefer faster wins
    elif winner == PLAYER_O:
        return depth - 10  # Prefer slower losses
    return 0  # Draw

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board, depth)
    
    # If game over, return the score
    if score != 0 or is_draw(board):
        return score

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                best_score = max(best_score, minimax(board, depth + 1, False, alpha, beta))
                board[i] = EMPTY  # Undo move
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Beta cutoff
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                best_score = min(best_score, minimax(board, depth + 1, True, alpha, beta))
                board[i] = EMPTY  # Undo move
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Alpha cutoff
        return best_score

# Find the best move for AI
def best_move(board):
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_X  # AI makes a move
            score = minimax(board, 0, False, -math.inf, math.inf)  # Alpha-Beta Pruning
            board[i] = EMPTY  # Undo move
            
            if score > best_score:
                best_score = score
                move = i

    return move

# Display the board
def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)

# Play the game
def play():
    board = [EMPTY] * 9
    print("Tic-Tac-Toe Game!")
    
    while True:
        print_board(board)
        
        # Player O's turn (human)
        valid_move = False
        while not valid_move:
            try:
                move = int(input("Enter your move (0-8): "))
                if board[move] == EMPTY:
                    valid_move = True
                    board[move] = PLAYER_O
                else:
                    print("Cell already occupied! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter a number between 0-8.")

        if check_winner(board):
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI's turn
        ai_move = best_move(board)
        board[ai_move] = PLAYER_X
        print(f"AI chooses move {ai_move}")

        if check_winner(board):
            print_board(board)
            print("AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play()
