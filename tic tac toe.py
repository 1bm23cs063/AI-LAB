def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column
            return True
    if all([board[i][i] == player for i in range(3)]):  # Diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Other diagonal
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_bot_move(board):
    # Bot is 'O', player is 'X'
    bot = "O"
    player = "X"

    # 1. Check if bot can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = bot
                if check_winner(board, bot):
                    return row, col
                board[row][col] = " "  # Undo move

    # 2. Check if player can win next move, block them
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board, player):
                    board[row][col] = " "  # Undo move
                    return row, col
                board[row][col] = " "  # Undo move

    # 3. Otherwise, pick first empty spot
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return row, col

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Human is X, bot is O

    while True:
        print_board(board)

        if current_player == "X":
            print(f"Player {current_player}'s turn.")
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
            except ValueError:
                print("Please enter valid integers for row and column.")
                continue

            if row not in range(3) or col not in range(3):
                print("Row and column must be 0, 1, or 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken. Try again.")
                continue
        else:
            print("Bot is thinking...")
            row, col = get_bot_move(board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            if current_player == "X":
                print("Congratulations! You win!")
            else:
                print("Bot wins! Better luck next time.")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

