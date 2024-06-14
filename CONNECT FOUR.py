
# Define the game board
board = [[' ' for _ in range(7)] for _ in range(6)]

# Function to print the current state of the board
def print_board():
    for row in board:
        print('|'.join(row))
    print('---------------')
    print(' 0 1 2 3 4 5 6')  # Column numbers

# Function to check if a column is full
def is_column_full(col):
    return board[0][col] != ' '

# Function to drop a disc into a column
def drop_disc(col, symbol):
    for row in range(5, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = symbol
            return True
    return False

# Function to check if a player has won
def check_win(symbol):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if all(board[row][col+i] == symbol for i in range(4)):
                return True

    # Check vertical
    for col in range(7):
        for row in range(3):
            if all(board[row+i][col] == symbol for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if all(board[row+i][col+i] == symbol for i in range(4)):
                return True

    # Check diagonal (top-right to bottom-left)
    for row in range(3):
        for col in range(3, 7):
            if all(board[row+i][col-i] == symbol for i in range(4)):
                return True

    return False

# Main game loop
def main():
    print_board()
    players = ['X', 'O']
    current_player = 0

    while True:
        symbol = players[current_player]
        column = int(input(f"Player {symbol}, choose a column (0-6): "))

        # Check for valid input
        if column < 0 or column > 6:
            print("Out of range, try again [0-6].")
            continue
        if is_column_full(column):
            print("This column is full. Try another column.")
            continue

        # Drop the disc into the column
        if drop_disc(column, symbol):
            print_board()

            # Check for win condition
            if check_win(symbol):
                print(f"Player {symbol} wins!")
                break

            # Check for draw condition
            if all(board[0][col] != ' ' for col in range(7)):
                print("It's a draw!")
                break

            # Switch to the other player
            current_player = (current_player + 1) % 2

# Run the game
if __name__ == "__main__":
    main()

