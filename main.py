#

# Board
# Display Board
# Play Game
# Check win
# Check rows, columns, and diagonals
# Check tie
# Flip players

# Global Vars



# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Who won? Or Tie?
winner = None

# Who's turn is it
current_player = "X"

# We need to create a function to display the board


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# We want to play a game, play_game() will be the main driver of the game


def play_game():

    # Display initial board
    display_board()

    # This is our game loop
    while game_still_going:

        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip the player
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner is None:
        print("Tie!")


def handle_turn(player):
    position = input("Please choose a number 1-9 for position!")

    # Because the input is string and the array starts with 0 we do this
    position = int(position) - 1

    board[position] = "X"

    display_board()


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    return


def check_rows():
    return


def check_columns():
    return


def check_for_tie():

    return


def flip_player():
    if current_player == "X":
        current_player == "O"
    else:
        current_player == "X"
    return


play_game()
