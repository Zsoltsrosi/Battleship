import time
import os


def win_screen(player):
    os.system('clear')
    if player == "Player 1":
        print('''
                             ____    ___                                           _      __      __                     
                            /\  _`\ /\_ \                                        /' \    /\ \  __/\ \                    
                            \ \ \L\ \//\ \      __     __  __     __   _ __     /\_, \   \ \ \/\ \ \ \    ___     ___    
                             \ \ ,__/ \ \ \   /'__`\  /\ \/\ \  /'__`\/\`'__\   \/_/\ \   \ \ \ \ \ \ \  / __`\ /' _ `\  
                              \ \ \/   \_\ \_/\ \L\.\_\ \ \_\ \/\  __/\ \ \/       \ \ \   \ \ \_/ \_\ \/\ \L\ \/\ \/\ \ 
                               \ \_\   /\____\ \__/.\_\\/`____ \ \____\\ \_\          \ \_\   \ `\___x___/\ \____/\ \_\ \_
                                \/_/   \/____/\/__/\/_/ `/___/> \/____/ \/_/         \/_/    '\/__//__/  \/___/  \/_/\/_/
                                                           /\___/                                                        
                                                           \/__/                                                         
                                    
                ''')
    else:           
        print('''
                 ____    ___                                            ___       __      __                     
                /\  _`\ /\_ \                                         /'___`\    /\ \  __/\ \                    
                \ \ \L\ \//\ \      __     __  __     __   _ __      /\_\ /\ \   \ \ \/\ \ \ \    ___     ___    
                 \ \ ,__/ \ \ \   /'__`\  /\ \/\ \  /'__`\/\`'__\    \/_/// /__   \ \ \ \ \ \ \  / __`\ /' _ `\  
                  \ \ \/   \_\ \_/\ \L\.\_\ \ \_\ \/\  __/\ \ \/        // /_\ \   \ \ \_/ \_\ \/\ \L\ \/\ \/\ \ 
                   \ \_\   /\____\ \__/.\_\\/`____ \ \____\\ \_\         /\______/    \ `\___x___/\ \____/\ \_\ \_
                    \/_/   \/____/\/__/\/_/ `/___/> \/____/ \/_/       \/_____/      '\/__//__/  \/___/  \/_/\/_/
                                               /\___/                                                            
                                               \/__/                                                                   
                ''')    

                   
def is_win(player, board):
    x_count = 0
    for row in board:
        for collumn in row:
            if collumn == "X":
                x_count += 1

    if x_count != 0:
        return False
    else:        
        return True
                
                
                
def intro():
    """plays before starting the game"""
    l = []
    l.append(" ______     ______     ______   ______   __         ______     ______     __  __     __     ______  ")
    l.append("/\  == \   /\  __ \   /\__  _\ /\__  _\ /\ \       /\  ___\   /\  ___\   /\ \_\ \   /\ \   /\  == \ ")
    l.append("\ \  __<   \ \  __ \  \/_/\ \/ \/_/\ \/ \ \ \____  \ \  __\   \ \___  \  \ \  __ \  \ \ \  \ \  __/ ")
    l.append(" \ \_____\  \ \_\ \_\    \ \_\    \ \_\  \ \_____\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\  \ \_\   ")
    l.append("  \/_____/   \/_/\/_/     \/_/     \/_/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/   \/_/   ")
    l.append("                                                                                                    ")
    l.append("                                                  # #  ( )                                          ")
    l.append("                                               ___#_#___|__                                         ")
    l.append("                                           _  |____________|  _                                     ")
    l.append("                                    _=====| | |            | | |==== _                              ")
    l.append("                              =====| |.---------------------------. | |====                         ")
    l.append("                <--------------------'   .  .  .  .  .  .  .  .   '--------------/                  ")
    l.append("                  \                                                             /                   ")
    l.append("                   \___________________________________________________________/                    ")
    l.append("               wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                ")
    l.append("             wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww               ")
    l.append("                wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                 ")
    for i in range(1, len(l[0]) + 1):  # fly in from left animation
        os.system("clear")
        for j in l:
            print(j[-i:])
            time.sleep(0.003)  # slowing down

    time.sleep(1)
    input("""
                      +-++-++-++-++-+ +-++-++-++-++-+ +-++-+ +-++-++-++-++-+
                      |P||R||E||S||S| |E||N||T||E||R| |T||O| |S||T||A||R||T|
                      +-++-++-++-++-+ +-++-++-++-++-+ +-++-+ +-++-++-++-++-+""")

    for i in range(len(l[0])):  # flying out to the left
        os.system("clear")
        for j in l:
            print(j[i:])
            time.sleep(0.003)

def init_board1():
    board_player1_ships = [["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    return board_player1_ships


def init_board2():
    board_player2_ships = [["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    return board_player2_ships


def print_ship_board(board, player):
    os.system("clear")
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
    ship_count_size2 = 2
    ship_count_size1 = 1
    while ship_count_size2 > 0 or ship_count_size1 > 0:
        print()
        ships = [f"1. Destroyer (size: 2 amount left: {ship_count_size2})", f"2. Submarine (size: 1 amount left: {ship_count_size1})"]
        for i in ships:
            print(i)
        print() 
        if ship_count_size2 > 0 and ship_count_size1 > 0:
            ship = input("%s choose ship size, 1 or 2: " % player)
        elif ship_count_size2 > 0 and ship_count_size1 == 0:
            ship = input("%s choose ship size, 2: " % player)
        elif ship_count_size1 > 0 and ship_count_size2 == 0:
            ship = input("%s choose ship size, 1: " % player)
        if ship == str(2) and ship_count_size2 > 0:
            ship_size = 2
            row, col = get_ship_move(board, player)
            ship_direction = input("Vertical or Horizontal placement (v/h)").lower()
            okay_placement = check_next_to_ship(row, col, board, player, ship_size, ship_direction)
            if ship_direction == 'v':
                try:
                    if okay_placement is True:
                        board[row][col] = "X"
                        board[row + 1][col] = "X"
                        ship_count_size2 -= 1
                        print_ship_board(board, player)
                    else:
                        print_ship_board(board, player) 
                        print("Ships too close")
                except IndexError:
                    board[row][col] = "0"
                    print_ship_board(board, player) 
                    print("Invalid input")  
            
            elif ship_direction == 'h':
                try:
                    if okay_placement is True:
                        board[row][col] = "X"
                        board[row][col + 1] = "X"
                        ship_count_size2 -= 1
                        print_ship_board(board, player) 
                    else:
                        print_ship_board(board, player) 
                        print("Ships too close")
                except IndexError:
                    board[row][col] = "0"
                    print_ship_board(board, player) 
            else:
                    print_ship_board(board, player) 
                    print("Invalid input")
                # print("Invalid input")  
        elif ship == str(1) and ship_count_size1 > 0:
            ship_size = 1
            row, col = get_ship_move(board, player)
            okay_placement = check_next_to_ship(row, col, board, player, ship_size)
            if okay_placement is True:
                if board[row][col] == "0":
                    board[row][col] = "X"
                    ship_count_size1 -= 1
                    print_ship_board(board, player) 

            else:
                print_ship_board(board, player) 
                print("Ships too close")
        else:
            print_ship_board(board, player) 
            print('Invalid input')
        

def check_next_to_ship(row, col, board, player, ship_size, ship_direction=None):
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
        elif ship_size == 1:
            if board[row + 1][col] == "0" and board[row][col + 1] == "0":
                if board[row][col - 1] == "0":
                    if board[row - 1][col] == "0":
                        return True
            else:
                return False
    except IndexError:
        return True


def print_game_board_player1(board2, player="Player 1"):
    print(player, end='\t\t\t')
    yield
    print('', end='')
    yield
    print("    1   2   3   4   5", end='')
    yield
    print('', end='')
    yield
    count = 0
    for letter in ["A", "B", "C", "D", "E"]:
        print(letter, end=" ")
        for index in [0, 1, 2, 3, 4]:
            if index < 6:
                if board2[count][index] == '0' or board2[count][index] == 'X':
                    print("  0", end=" ")
                if board2[count][index] == 'M':
                    print("  {}".format('M'), end=" ")
                if board2[count][index] == 'H':
                    print("  {}".format('H'), end=" ")
                if board2[count][index] == 'S':
                    print("  {}".format('S'), end=" ")
        yield
        if letter != str("E"):
            print('',end='')
            yield
        count += 1
    print("", end='')
    yield


def print_game_board_player2(board1, player="Player 2"):
    print(player, end='')
    yield
    print('', end='')
    yield
    print("\t\t    1   2   3   4   5", end='')
    yield
    print('', end='')
    yield
    count = 0
    for letter in ["A", "B", "C", "D", "E"]:
        print(letter.rjust(10), end=" ")
        for index in [0, 1, 2, 3, 4]:
            if index < 6:
                if board1[count][index] == '0' or board1[count][index] == 'X':
                    print("  0", end=" ")
                if board1[count][index] == 'M':
                    print("  {}".format('M'), end=" ")
                if board1[count][index] == 'H':
                    print("  {}".format('H'), end=" ")
                if board1[count][index] == 'S':
                    print("  {}".format('S'), end=" ")
        yield
        if letter != str("E"):
            print('',end='')
            yield
        count += 1
    print("", end='')
    yield


def print_both_boards(board1, board2):
    os.system('clear')
    player_1_board, player_2_board = print_game_board_player1(board2), print_game_board_player2(board1)

    while True:
        try:
            next(player_1_board)
            print(' ', end='')
            next(player_2_board)
            print()
        except StopIteration:
            break


def get_ship_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    while True:
        print()
        move = input("%s choose coordinates:  " % player)
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
        print()
        move = input("%s choose coordinates:  " %player)
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
                        if board[row][col] == "M" or board[row][col] == "H":
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
        print('You have hit a ship!')
        time.sleep(2)
    else:
        board[row][col] = "M"
        print('You missed!')
        time.sleep(2)


def valid_coordinate(a, b):
    if -1 < a < 5 and -1 < b < 5:
        return True
    else:
        return False

        
def check_sunken_ship(board, player):
    sunken = 1
    for (i, row) in enumerate(board):
        for (j, col) in enumerate(row):
            sunk = False
            if col == 'H':
                if valid_coordinate(i + 1, j) and board[i + 1][j] == 'X':
                    sunk = False
                elif valid_coordinate(i, j - 1) and board[i][j - 1] == 'X':
                    sunk = False
                elif valid_coordinate(i, j + 1) and board[i][j + 1] == 'X':
                    sunk = False
                elif valid_coordinate(i - 1, j) and board[i - 1][j] == 'X':
                    sunk = False
                else:
                    sunk = True
            if sunk:
                board[i][j] = 'S'
                if sunken > 0:
                    print("You have sunk a ship!")
                    time.sleep(2)
                    sunken -= 1
                


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




def ship_placement_phase(player_index):
    while player_index < 3:
        player = choose_player(player_index)
        board = choose_ship_board(player)
        print_ship_board(board, player)
        place_ship(board, player)
        player_index += 1
        os.system("clear")
        input("Ready? (Press any key) ")
        os.system("clear")


def game_play(player_index):
    winner = False
    while winner is False:
        player = choose_player(player_index)
        board = choose_game_board(player)
        print_both_boards(board1, board2)
        row, col = get_move(board, player)
        mark(board, row, col, player)
        check_sunken_ship(board, player)
        print_both_boards(board1, board2)
        time.sleep(1)
        winner = is_win(player, board)
        player_index += 1
    win_screen(player)


# def start_menu():



board1 = init_board1()
board2 = init_board2()



def main_menu():
    player_index = 1
    # intro()
    # start_menu()
    ship_placement_phase(player_index)
    game_play(player_index)
   


if __name__ == '__main__':
    main_menu()
