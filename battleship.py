import time

def init_board1():
    board1 = [["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    return board1


def init_board2():
    board2 = [["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    return board2


def print_board(board, player):
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
    okay_placement = False
    while ship_count >= 0:
        ship = int(input(" %s choose ship size, 2 or 3: " % player))
        if ship == 2:
            ship_size = 2
            row, col = get_move(board, player)
            ship_direction = input("Vertical or Horizontal placement (v/h)").lower()
            check_next_to_ship(row, col, board, player, ship_size, ship_direction)
            if ship_direction == 'v':
                if okay_placement is True:
                    if board[row + 1][col] == "0":
                        board[row][col] = "X"
                        board[row + 1][col] = "X"
                        ship_count -= 1
                        print(ship_count)
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
        if ship == 3:
            row, col = get_move(board, player)
            ship_direction = input("Vertical or Horizontal placement (v/h)").lower()
            check_next_to_ship(row, col, board, player, ship_size, ship_direction)
            if ship_direction == 'v':
                if okay_placement is True:
                    if board[row + 1][col] == "0" and board[row + 2][col] == "0":
                        board[row][col] = "X"
                        board[row + 1][col] = "X"
                        board[row + 2][col] = "X"
                        ship_count -= 1
                        print(ship_count)
                    else:
                        print("Invalid input")
            elif ship_direction == 'h':
                if okay_placement is True:
                    if board[row][col + 1] == "0" and board[row][col + 2] == "0":
                        board[row][col] = "X"
                        board[row][col + 1] = "X"
                        board[row][col + 2] = "X"
                        ship_count -= 1
                        print(ship_count)
                    else:
                        print("Invalid input")
            
        print_board(board, player)
        time.sleep(2)
            
            

            

def check_next_to_ship(row, col, board, player, ship_size, ship_direction):
    okay_placement = False
    try:
        if ship_size == 2 and ship_direction == 'v':          
            if board[row + 1][col] == "0" and board[row + 1][col + 1] == "0" and board[row][col + 1] == "0":
                if board[row + 2][col] == "0" and board[row + 1][col - 1] == "0" and board[row][col - 1] == "0":
                    if board[row - 1][col] == "0":
                        print(okay_placement)
                        return okay_placement is True
                        
                    else:
                        print(okay_placement)
                        return okay_placement is False
        elif ship_size == 2 and ship_direction == 'h':
            if board[row][col + 1] == "0" and board[row][col + 2] == "0" and board[row][col - 1] == "0":
                if board[row + 1][col] == "0" and board[row + 1][col + 1] == "0" and board[row - 1][col] == "0":
                    if board[row - 1][col + 1] == "0":
                        print(okay_placement)
                        return okay_placement is True
                    else:
                        print(okay_placement)
                        return okay_placement is False
        elif ship_size == 3 and ship_direction == 'v':
            if board[row + 1][col] == "0" and board[row + 1][col + 1] == "0" and board[row][col + 1] == "0":
                if board[row + 2][col] == "0" and board[row + 1][col - 1] == "0" and board[row][col - 1] == "0":
                    if board[row - 1][col] == "0" and board[row + 3][col] == "0" and board[row + 2][col + 1] == "0" and board[row + 2][col - 1] == "0":
                        print(okay_placement)
                        return okay_placement is True
                    else:
                        print(okay_placement)
                        return okay_placement is False
        elif ship_size == 3 and ship_direction == 'h':
            if board[row][col + 1] == "0" and board[row][col + 2] == "0" and board[row][col - 1] == "0":
                if board[row + 1][col] == "0" and board[row + 1][col + 1] == "0" and board[row - 1][col] == "0":
                    if board[row - 1][col + 1] == "0" and board[row][col + 3] == "0" and board[row + 1][col + 2] == "0" and board[row - 1][col + 2] == "0":
                        return okay_placement is True
                    else:
                        return okay_placement is False
    except IndexError:
        print("Invalid Input")


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    while True:
        move = input("%s make your move!" % player)
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


def choose_player(player_index):
    if int(player_index) % 2 == 1:
        player = "Player One"
    else:
        player = "Player Two"  
    return player


def mark(board, row, col, player):
    if player == "Player One":
        board[row][col] = "X"
    else:
        board[row][col] = "X"
    

def choose_board(player):
    if player == "Player One":
        board = board1
    else:
        board = board2
    return board

board1 = init_board1()
board2 = init_board2()

def main_menu():
    player_index = 1
    while player_index < 3:
        player = choose_player(player_index)
        board = choose_board(player)
        print_board(board, player)
        place_ship(board, player)
        player_index += 1
    while True:
        player = choose_player(player_index)
        board = choose_board(player)
        print_board(board, player)
        time.sleep(1)
        row, col = get_move(board, player)
        mark(board, row, col, player)
        player_index += 1


if __name__ == '__main__':
    main_menu()
