import random

board = []
for i in range(3):
    for y in range(3):
        board.append("-")


def player_sign():
    random_number = random.randint(0, 1)
    if random_number == 0:
        player_one = "X"
        player_two = "Y"
    else:
        player_one = "Y"
        player_two = "X"

    print(f"Player 1: {player_one}\nPlayer 2: {player_two}")

    if player_one == "X":
        print("\nPlayer 1 starts first!\n")
    else:
        print("\nPlayer 2 starts first!\n")
    return player_one, player_two


def draw():
    print("\n|" + board[0] + "|" + board[1] + "|" + board[2] + "|\n" +
          "|" + board[3] + "|" + board[4] + "|" + board[5] + "|\n" +
          "|" + board[6] + "|" + board[7] + "|" + board[8] + "|\n")


def update_board(board, player_sign, player_number):
    while True:
        player_choice = int(input(f"Player {player_number}: Select field from 0 - 8: "))
        try:
            if board[player_choice] != "-":
                print("Can't do that. Try different placement.")
                draw()
                continue
            else:
                board[player_choice] = player_sign
                draw()
                return True
        except IndexError:
            print("Can't do that. Try different placement.")
            draw()
            continue


def check_winner(brd, sign, player_number):
    if ((brd[0] == sign and brd[1] == sign and brd[2] == sign) or
            (brd[3] == sign and brd[4] == sign and brd[5] == sign) or
            (brd[6] == sign and brd[7] == sign and brd[8] == sign) or
            (brd[0] == sign and brd[3] == sign and brd[6] == sign) or
            (brd[1] == sign and brd[4] == sign and brd[7] == sign) or
            (brd[2] == sign and brd[5] == sign and brd[8] == sign) or
            (brd[0] == sign and brd[4] == sign and brd[8] == sign) or
            (brd[2] == sign and brd[4] == sign and brd[6] == sign)):
        print(f"Player {player_number} Wins!")
        return True
    elif "-" not in board:
        print("No more fields available. It's a tie!")
        return True
    else:
        return False


def play():
    player_one, player_two = player_sign()
    draw()
    if player_one == "X":
        while True:
            update_board(board, player_one, 1)
            if check_winner(board, player_one, 1):
                break
            else:
                update_board(board, player_two, 2)
                if check_winner(board, player_two, 2):
                    break
                else:
                    continue
    else:
        while True:
            update_board(board, player_two, 2)
            if check_winner(board, player_two, 2):
                break
            else:
                update_board(board, player_one, 1)
                if check_winner(board, player_one, 1):
                    break
                else:
                    continue


if __name__ == "__main__":
    play()


