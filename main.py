#

# Board
# Display Board
# Play Game
# Check win
# Check rows, columns, and diagonals
# Check tie
# Flip players

# Global Vars
game_still_going = True


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# We need to create a function to display the board


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# We want to play a game, play_game() will be the main driver of the game


def play_game():

    # Display initial board
    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()


def handle_turn():
    position = input("Please choose a number 1-9 for position!")

    # Because the input is string and the array starts with 0 we do this
    position = int(position) - 1

    board[position] = "X"

    display_board()


def check_if_game_over():

    check_if_win()

    check_if_tie()


def check_if_win():


def check_if_tie():
    # Check if all the spaces are not -
    return

def flip_player():
    return





play_game()
