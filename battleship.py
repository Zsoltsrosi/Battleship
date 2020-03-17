import time


def init_board1():
    board_player1_ships = [["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    return board_player1_ships


def init_board2():
    board_player2_ships = [["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    return board_player2_ships


def print_ship_board(board, player):
    print("1".rjust(4) + "2".rjust(4) + "3".rjust(4) + "4".rjust(4) + "5".rjust(4) + "\n")
    print("A".ljust(2) + str(board[0][0]).center(3) + "|" + str(board[0][1]).center(3) + "|" + str(board[0][2]).center(3) + "|" + str(board[0][3]).center(3) + "|" + str(board[0][4]).center(3))
    print("  ---+---+---+---+---")
    print("B".ljust(2) + str(board[1][0]).center(3) + "|" + str(board[1][1]).center(3) + "|" + str(board[1][2]).center(3) + "|" + str(board[1][3]).center(3) + "|" + str(board[1][4]).center(3))
    print("  ---+---+---+---+---")
    print("C".ljust(2) + str(board[2][0]).center(3) + "|" + str(board[2][1]).center(3) + "|" + str(board[2][2]).center(3) + "|" + str(board[2][3]).center(3) + "|" + str(board[2][4]).center(3))
    print("  ---+---+---+---+---")
    print("D".ljust(2) + str(board[3][0]).center(3) + "|" + str(board[3][1]).center(3) + "|" + str(board[3][2]).center(3) + "|" + str(board[3][3]).center(3) + "|" + str(board[3][4]).center(3))
    print("  ---+---+---+---+---")
    print("E".ljust(2) + str(board[4][0]).center(3) + "|" + str(board[4][1]).center(3) + "|" + str(board[4][2]).center(3) + "|" + str(board[4][3]).center(3) + "|" + str(board[4][4]).center(3))


def place_ship(board, player):
    ship_count = 2
    while ship_count > 0:
        ship = input(" %s choose ship size, 2 or 3: " % player)
        if ship == str(2):
            ship_size = 2
            row, col = get_ship_move(board, player)
            ship_direction = input("Vertical or Horizontal placement (v/h)").lower()
            okay_placement = check_next_to_ship(row, col, board, player, ship_size, ship_direction)
            if ship_direction == 'v':
                if okay_placement is True:
                    if board[row + 1][col] == "0":
                        board[row][col] = "X"
                        board[row + 1][col] = "X"
                        ship_count -= 1
                        print(ship_count)
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")
            elif ship_direction == 'h':
                if okay_placement is True:
                    if board[row][col + 1] == "0":
                        board[row][col] = "X"
                        board[row][col + 1] = "X"
                        ship_count -= 1
                        print(ship_count)
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")
        if ship == str(3):
            ship_size = 3
            row, col = get_ship_move(board, player)
            ship_direction = input("Vertical or Horizontal placement (v/h)").lower()
            okay_placement = check_next_to_ship(row, col, board, player, ship_size, ship_direction)
            if ship_direction == 'v':
                if okay_placement is True:
                    if board[row + 1][col] == "0" and board[row + 2][col] == "0":
                        board[row][col] = "X"
                        board[row + 1][col] = "X"
                        board[row + 2][col] = "X"
                        ship_count -= 1
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")
            elif ship_direction == 'h':
                if okay_placement is True:
                    if board[row][col + 1] == "0" and board[row][col + 2] == "0":
                        board[row][col] = "X"
                        board[row][col + 1] = "X"
                        board[row][col + 2] = "X"
                        ship_count -= 1
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")

        print_ship_board(board, player)

            

def check_next_to_ship(row, col, board, player, ship_size, ship_direction):
    try:
        if ship_size == 2 and ship_direction == 'v':          
            if board[row + 1][col] == "0" and board[row + 1][col + 1] == "0" and board[row][col + 1] == "0":
                if board[row + 2][col] == "0" and board[row + 1][col - 1] == "0" and board[row][col - 1] == "0":
                    if board[row - 1][col] == "0":
                        return True
                    else:
                        return False
        elif ship_size == 2 and ship_direction == 'h':
            if board[row][col + 1] == "0" and board[row][col + 2] == "0" and board[row][col - 1] == "0":
                if board[row + 1][col] == "0" and board[row + 1][col + 1] == "0" and board[row - 1][col] == "0":
                    if board[row - 1][col + 1] == "0":
                        return True
                    else:
                        return False
        elif ship_size == 3 and ship_direction == 'v':
            if board[row + 1][col] == "0" and board[row + 1][col + 1] == "0" and board[row][col + 1] == "0":
                if board[row + 2][col] == "0" and board[row + 1][col - 1] == "0" and board[row][col - 1] == "0":
                    if board[row - 1][col] == "0" and board[row + 3][col] == "0" and board[row + 2][col + 1] == "0" and board[row + 2][col - 1] == "0":
                        return True
                    else:
                        return False
        elif ship_size == 3 and ship_direction == 'h':
            if board[row][col + 1] == "0" and board[row][col + 2] == "0" and board[row][col - 1] == "0":
                if board[row + 1][col] == "0" and board[row + 1][col + 1] == "0" and board[row - 1][col] == "0":
                    if board[row - 1][col + 1] == "0" and board[row][col + 3] == "0" and board[row + 1][col + 2] == "0" and board[row - 1][col + 2] == "0":
                        return True
                    else:
                        return False
    except IndexError:
        print("Invalid Input")


def print_game_board(board, player):
    print()
    print("    1   2   3   4   5")
    print("")
    count = 0
    for i in ["A", "B", "C", "D", "E"]:
        print(i, end=" ")
        for j in [0, 1, 2, 3, 4]:
            if j < 6:
                if board[count][j] == '0' or board[count][j] == 'X':
                    print("  0", end=" ")
                if board[count][j] == 'M':
                    print("  M ")
                if board[count][j] == 'H':
                    print("  H ")
        print()
        if i != str("E"):
            print()
        count += 1
    print("")

def get_ship_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    while True:
        move = input("%s choose coordinates" % player)
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
                        if board[row][col] != "0":
                            print("Please choose another coordinate!")
                        else:
                            return row, col

            except ValueError:
                print(wrong_input)


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    while True:
        move = input("%s choose coordinates" % player)
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
                        if board[row][col] == "M" or board[row][col] == "M":
                            print("Please choose another coordinate!")
                        else:
                            return row, col

            except ValueError:
                print(wrong_input)




def choose_player(player_index):
    if int(player_index) % 2 == 1:
        player = "Player 1"
    else:
        player = "Player 2"  
    return player


def mark(board, row, col, player):
    if board[row][col] == "X":
        board[row][col] = "H"
    else:
        board[row][col] = "M"
    

def choose_ship_board(player):
    if player == "Player 1":
        board = board1
    else:
        board = board2
    return board

def choose_game_board(player):
    if player == "Player 1":
        board = board2
    else:
        board = board1
    return board


board1 = init_board1()
board2 = init_board2()


def main_menu():
    player_index = 1
    while player_index < 3:
        player = choose_player(player_index)
        board = choose_ship_board(player)
        print_ship_board(board, player)
        place_ship(board, player)
        player_index += 1
    while True:
        player = choose_player(player_index)
        board = choose_game_board(player)
        print_game_board(board, player)
        time.sleep(1)
        row, col = get_move(board, player)
        mark(board, row, col, player)
        player_index += 1


if __name__ == '__main__':
    main_menu()
