def init_board1():
    board1 = [["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    return board1


def init_board2():
    board2 = [["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    return board2


def print_board(board1, board2, player):
    if player == "Player One":
        print("1".rjust(4) + "2".rjust(4) + "3".rjust(4) + "4".rjust(4) + "5".rjust(4) + "\n")
        print("A".ljust(2) + str(board1[0][0]).center(3) + "|" + str(board1[0][1]).center(3) + "|" + str(board1[0][2]).center(3) + "|" + str(board1[0][3]).center(3) + "|" + str(board1[0][4]).center(3))
        print("  ---+---+---+---+---")
        print("B".ljust(2) + str(board1[1][0]).center(3) + "|" + str(board1[1][1]).center(3) + "|" + str(board1[1][2]).center(3) + "|" + str(board1[1][3]).center(3) + "|" + str(board1[1][4]).center(3))
        print("  ---+---+---+---+---")
        print("C".ljust(2) + str(board1[2][0]).center(3) + "|" + str(board1[2][1]).center(3) + "|" + str(board1[2][2]).center(3) + "|" + str(board1[2][3]).center(3) + "|" + str(board1[2][4]).center(3))
        print("  ---+---+---+---+---")
        print("D".ljust(2) + str(board1[3][0]).center(3) + "|" + str(board1[3][1]).center(3) + "|" + str(board1[3][2]).center(3) + "|" + str(board1[3][3]).center(3) + "|" + str(board1[3][4]).center(3))
        print("  ---+---+---+---+---")
        print("E".ljust(2) + str(board1[4][0]).center(3) + "|" + str(board1[4][1]).center(3) + "|" + str(board1[4][2]).center(3) + "|" + str(board1[4][3]).center(3) + "|" + str(board1[4][4]).center(3))

    else:
        print("1".rjust(4) + "2".rjust(4) + "3".rjust(4) + "4".rjust(4) + "5".rjust(4) + "\n")
        print("A".ljust(2) + str(board2[0][0]).center(3) + "|" + str(board2[0][1]).center(3) + "|" + str(board2[0][2]).center(3) + "|" + str(board2[0][3]).center(3) + "|" + str(board2[0][4]).center(3))
        print("  ---+---+---+---+---")
        print("B".ljust(2) + str(board2[1][0]).center(3) + "|" + str(board2[1][1]).center(3) + "|" + str(board2[1][2]).center(3) + "|" + str(board2[1][3]).center(3) + "|" + str(board2[1][4]).center(3))
        print("  ---+---+---+---+---")
        print("C".ljust(2) + str(board2[2][0]).center(3) + "|" + str(board2[2][1]).center(3) + "|" + str(board2[2][2]).center(3) + "|" + str(board2[2][3]).center(3) + "|" + str(board2[2][4]).center(3))
        print("  ---+---+---+---+---")
        print("D".ljust(2) + str(board2[3][0]).center(3) + "|" + str(board2[3][1]).center(3) + "|" + str(board2[3][2]).center(3) + "|" + str(board2[3][3]).center(3) + "|" + str(board2[3][4]).center(3))
        print("  ---+---+---+---+---")
        print("E".ljust(2) + str(board2[4][0]).center(3) + "|" + str(board2[4][1]).center(3) + "|" + str(board2[4][2]).center(3) + "|" + str(board2[4][3]).center(3) + "|" + str(board2[4][4]).center(3))


def get_move(board1, board2, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    while True:
        move = input("Make your move!")
        wrong_input = "Input form was incorrect, please try again"
        location = list(move)
        if move == 'quit':
            exit()
        else:
            try:
                if (len(move)) != 2:
                    print(wrong_input)
                elif location[0].isalpha() is False:
                    print(wrong_input)
                else:
                    row, col = (ord(location[0].lower()) - 97, int(location[1]))
                    if row >= 6 or col >= 6:
                        print("you're not on the board")
                    else:
                        col = col - 1
                        if player == "Player One":
                            if board1[row][col] != "0":
                                print("Please choose another coordinate!")
                            else:
                                return row, col
                        if player == "Player Two":
                            if board2[row][col] != "0":
                                print("Please choose another coordinate!")
                            else:
                                return row, col

            except ValueError:
                print(wrong_input)


def choose_player(player_index):
    if int(player_index) % 2 == 1:
        player = "Player One"
    else:
        player = "Player Two"  
    return player


def mark(board1, board2, row, col, player):
    if player == "Player One":
        board1[row][col] = "X"
    else:
        board2[row][col] = "X"


def main_menu():
    player_index = 1
    board1 = init_board1()
    board2 = init_board2()
    while True:
        player = choose_player(player_index)
        row, col = get_move(board1, board2, player)
        print_board(board1, board2, player)
        mark(board1, board2, row, col, player)
        player_index += 1


if __name__ == '__main__':
    main_menu()
