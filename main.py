from logo import logo
from random import choice
import time


def board(moves):
    current_board = f" {moves['7']} | {moves['8']} | {moves['9']} \n" \
                    f" - | - | - \n" \
                    f" {moves['4']} | {moves['5']} | {moves['6']} \n" \
                    f" - | - | - \n" \
                    f" {moves['1']} | {moves['2']} | {moves['3']} \n"
    print(current_board)


def get_mode():
    mode = input('Would you like to play a 1 or 2 player game? Please enter "1" or "2": ')
    if mode.isnumeric and int(mode) in range(1, 3):
        return mode
    else:
        print('Mode input is invalid, please try again')
        get_mode()


def valid_input(player_move):
    if player_move.isnumeric() and int(player_move) in range(1, 10):
        return True
    else:
        print("Invalid input provided, please try again.")
        return False


def check_move_available(player_move, moves):
    if moves[player_move] == " ":
        return True
    else:
        print("That space is already taken. Please try again.")
        return False


def check_win(marker, moves, player):
    if moves['7'] == moves['8'] == moves['9'] == marker \
            or moves['4'] == moves['5'] == moves['6'] == marker \
            or moves['1'] == moves['2'] == moves['3'] == marker \
            or moves['7'] == moves['4'] == moves['1'] == marker \
            or moves['8'] == moves['5'] == moves['2'] == marker \
            or moves['9'] == moves['6'] == moves['3'] == marker \
            or moves['1'] == moves['5'] == moves['9'] == marker \
            or moves['7'] == moves['5'] == moves['3'] == marker:
        print(f'Congratulations {player}, you are the winner!')
        return True
    elif " " not in moves.values():
        print("Unlucky this time. It's a draw!")
        return True
    else:
        return False


def tic_tac_toe():
    print(logo)
    print('Welcome to Tic-Tac-Toe! Use the numbers key pad to select your move, '
          'e.g. "7" is top left, "5" is centre and "3" is bottom right.\n')
    print(" 7 | 8 | 9 \n"
          " - | - | - \n"
          " 4 | 5 | 6 \n"
          " - | - | - \n"
          " 1 | 2 | 3 \n")
    print('If you wish to exit the game at any time, please enter "q".\n')

    mode = get_mode()
    player1 = input('Player 1, please enter your name: ')
    if mode == "2":
        player2 = input('Player 2, please enter your name: ')
    else:
        player2 = "Computer"

    moves = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' ', }

    player = player1
    game_on = True
    board(moves)

    while game_on:
        if player == player1 or mode == '2':
            player_move = input(f'{player}, select your move: ')
        else:
            time.sleep(0.75)
            available_spaces = [key for (key, value) in moves.items() if value == " "]
            player_move = choice(available_spaces)
            print(f'The Computer has chosen space {player_move}.')
        if player_move.lower() == 'q':
            print("Thanks for playing!")
            game_on = False
        elif valid_input(player_move) and check_move_available(player_move, moves):
            if player == player1:
                moves[player_move] = "X"
                if check_win("X", moves, player):
                    game_on = False
                player = player2
            else:
                moves[player_move] = "O"
                if check_win("O", moves, player):
                    game_on = False
                player = player1
            board(moves)

    if input('Would you like to play another game? ("y" or "n"): ').lower() == "y":
        tic_tac_toe()
    else:
        print("Thanks for playing!")


tic_tac_toe()
