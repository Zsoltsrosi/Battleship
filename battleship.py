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


def logo():

    print('''
        ██████╗  █████╗ ████████╗████████╗██╗     ███████╗    ███████╗██╗  ██╗██╗██████╗ 
        ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝    ██╔════╝██║  ██║██║██╔══██╗
        ██████╔╝███████║   ██║      ██║   ██║     █████╗      ███████╗███████║██║██████╔╝
        ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝      ╚════██║██╔══██║██║██╔═══╝ 
        ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗    ███████║██║  ██║██║██║     
        ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     
        ''')
                
                
def intro():

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
            time.sleep(0.001) 

    time.sleep(1)
    input("""
                      +-++-++-++-++-+ +-++-++-++-++-+ +-++-+ +-++-++-++-++-+
                      |P||R||E||S||S| |E||N||T||E||R| |T||O| |S||T||A||R||T|
                      +-++-++-++-++-+ +-++-++-++-++-+ +-++-+ +-++-++-++-++-+""")

    for i in range(len(l[0])):  # flying out to the left
        os.system("clear")
        for j in l:
            print(j[i:])
            time.sleep(0.001)

def init_board1(length_input):
    board_player1_ships = [['0' for x in range(length_input)] for x in range(length_input)]
    return board_player1_ships


def init_board2(length_input):
    board_player2_ships = [['0' for x in range(length_input)] for x in range(length_input)]
    return board_player2_ships


def print_ship_board(board, player, length_input):
    os.system("clear")
    print()
    numbers = ("12345678910")
    if length_input < 10:
        print("    " + "   ".join(numbers[:length_input]))
    elif length_input == 10:
        print("    " + "   ".join(numbers[:length_input]) + '0')
    print("")
    count = 0
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for letter in range(length_input):
        print(alphabet[letter], end=" ")
        for index in range(length_input):
            if index < (length_input + 1):
                if board[count][index] == '0':
                    print("  0", end=" ")
                if board[count][index] == 'X':
                    print("  {}".format('X'), end=" ")
                if board[count][index] == 'H':
                    print("  {}".format('H'), end=" ")
                if board[count][index] == 'S':
                    print("  {}".format('S'), end=" ")
        print("")
        if letter != str("J"):
            print()
        count += 1
    print("")


def place_ship(board, player, length_input):
    ship_count_size2 = (length_input // 2)
    ship_count_size1 = (length_input // 2) - 1

    while ship_count_size2 > 0 or ship_count_size1 > 0:
        print()
        ships = [f"1. Submarine (size: 1 amount left: {ship_count_size1})", f"2. Destroyer (size: 2 amount left: {ship_count_size2})"]
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
            row, col = get_ship_move(board, player, length_input)
            ship_direction = input("Vertical or Horizontal placement (v/h)").lower()
            okay_placement = check_next_to_ship(row, col, board, player, ship_size, ship_direction)
            if ship_direction == 'v':
                try:
                    if okay_placement is True:
                        board[row][col] = "X"
                        board[row + 1][col] = "X"
                        ship_count_size2 -= 1
                        print_ship_board(board, player, length_input)
                    else:
                        print_ship_board(board, player, length_input) 
                        print("Ships too close")
                except IndexError:
                    board[row][col] = "0"
                    print_ship_board(board, player, length_input) 
                    print("Invalid input")  
            
            elif ship_direction == 'h':
                try:
                    if okay_placement is True:
                        board[row][col] = "X"
                        board[row][col + 1] = "X"
                        ship_count_size2 -= 1
                        print_ship_board(board, player, length_input) 
                    else:
                        print_ship_board(board, player, length_input) 
                        print("Ships too close")
                except IndexError:
                    board[row][col] = "0"
                    print_ship_board(board, player, length_input) 
            else:
                    print_ship_board(board, player, length_input) 
                    print("Invalid input")
                # print("Invalid input")  
        elif ship == str(1) and ship_count_size1 > 0:
            ship_size = 1
            row, col = get_ship_move(board, player, length_input)
            okay_placement = check_next_to_ship(row, col, board, player, ship_size)
            if okay_placement is True:
                if board[row][col] == "0":
                    board[row][col] = "X"
                    ship_count_size1 -= 1
                    print_ship_board(board, player, length_input) 

            else:
                print_ship_board(board, player, length_input) 
                print("Ships too close")
        else:
            print_ship_board(board, player, length_input) 
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


def print_game_board_player1(board2, length_input, player="Player 1"):
    print('', end='')
    yield
    print(player, end='\t')
    yield
    print('', end='')
    yield
    numbers = ("12345678910")
    if length_input < 10:
        print("    " + "   ".join(numbers[:length_input]), end='')
    elif length_input == 10:
        print("    " + "   ".join(numbers[:length_input]) + '0', end='')
    yield
    print('', end='')
    yield
    count = 0
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for letter in range(length_input):
        print(alphabet[letter], end=" ")
        for index in range(length_input):
            if index < (length_input + 1):
                if board2[count][index] == '0' or board2[count][index] == 'X':
                    print("  0", end=" ")
                if board2[count][index] == 'M':
                    print("  {}".format('M'), end=" ")
                if board2[count][index] == 'H':
                    print("  {}".format('H'), end=" ")
                if board2[count][index] == 'S':
                    print("  {}".format('S'), end=" ")
        yield
        if letter != str("J"):
            print('',end='')
            yield
        count += 1
    print('', end='')
    yield


def print_game_board_player2(board1, length_input, player="Player 2"):
    print('', end='')
    yield
    print(" ".rjust(length_input * 3) +player, end='')
    yield
    print('', end='')
    yield
    numbers = ("12345678910")
    if length_input < 10:
        print("".rjust(length_input+4) + "   ".join(numbers[:length_input]), end='')
    elif length_input == 10:
        print(" ".rjust(length_input+4) + "   ".join(numbers[:length_input]) + '0', end='')
    yield
    print('', end='')
    yield
    count = 0
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for letter in range(length_input):
        print((alphabet[letter].rjust(length_input)), end=" ")
        for index in range(length_input):
            if index < (length_input + 1):
                if board1[count][index] == '0' or board1[count][index] == 'X':
                    print("  0", end=" ")
                if board1[count][index] == 'M':
                    print("  {}".format('M'), end=" ")
                if board1[count][index] == 'H':
                    print("  {}".format('H'), end=" ")
                if board1[count][index] == 'S':
                    print("  {}".format('S'), end=" ")
        yield
        if letter != str("J"):
            print('',end='')
            yield
        count += 1
    print('', end='')
    yield


def print_both_boards(board1, board2, length_input):
    os.system('clear')
    player_1_board, player_2_board = print_game_board_player1(board2, length_input), print_game_board_player2(board1, length_input)

    while True:
        try:
            next(player_1_board)
            print(' ', end='')
            next(player_2_board)
            print()
        except StopIteration:
            break


def get_ship_move(board, player, length_input):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    while True:
        print()
        move = input("%s choose coordinates:  " % player).lower()
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
                    if row >= (length_input + 1) or col >= (length_input + 1):
                        print("you're not on the board")
                    else:
                        col = col - 1
                        if board[row][col] != "0":
                            print("Please choose another coordinate!")
                        else:
                            return row, col

            except ValueError:
                print(wrong_input)


def get_move(board, player, length_input):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    while True:
        print()
        move = input("%s choose coordinates:  " %player).lower()
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
                    if row >= (length_input + 1) or col >= (length_input + 1):
                        print("you're not on the board")
                    else:
                        col = col - 1
                        if board[row][col] == "M" or board[row][col] == "H" or board[row][col] == "S":
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
    elif board[row][col] == '0':
        board[row][col] = "M"
        print('You missed!')
        time.sleep(2)


def valid_coordinate(a, b, length_input):
    if -1 < a < length_input and -1 < b < length_input:
        return True
    else:
        return False

        
def check_sunken_ship(board, player, length_input):
    sunken = 1
    for (i, row) in enumerate(board):
        for (j, col) in enumerate(row):
            sunk = False
            if col == 'H':
                if valid_coordinate(i + 1, j, length_input) and board[i + 1][j] == 'X':
                    sunk = False
                elif valid_coordinate(i, j - 1, length_input) and board[i][j - 1] == 'X':
                    sunk = False
                elif valid_coordinate(i, j + 1, length_input) and board[i][j + 1] == 'X':
                    sunk = False
                elif valid_coordinate(i - 1, j, length_input) and board[i - 1][j] == 'X':
                    sunk = False
                else:
                    sunk = True
            if sunk:
                board[i][j] = 'S'
                if sunken > 0:
                    print("You have sunk a ship!")
                    time.sleep(2)
                    sunken -= 1
                

def choose_ship_board(player, board1, board2):
    if player == "Player 1":
        board = board1
    else:
        board = board2
    return board


def choose_game_board(player,board1, board2):
    if player == "Player 1":
        board = board2
    else:
        board = board1
    return board




def ship_placement_phase(player_index, length_input, board1, board2):
    while player_index < 3:
        player = choose_player(player_index)
        board = choose_ship_board(player,board1, board2)
        print_ship_board(board, player, length_input)
        place_ship(board, player, length_input)
        player_index += 1
        os.system("clear")
        input("Ready? (Press any key) ")
        os.system("clear")


def game_play(player_index, length_input, board1, board2):
    winner = False
    while winner is False:
        player = choose_player(player_index)
        board = choose_game_board(player, board1, board2)
        print_both_boards(board1, board2, length_input)
        row, col = get_move(board, player, length_input)
        mark(board, row, col, player)
        check_sunken_ship(board, player, length_input)
        print_both_boards(board1, board2, length_input)
        time.sleep(1)
        winner = is_win(player, board)
        player_index += 1
    win_screen(player)


def start_menu():
    logo()
    print("1. Play game")
    print("2. Quit")
    print()
    game_start_input = int(input("Pick game mode: "))
    if game_start_input == 1:
        return True
    elif game_start_input == 2:
        exit()
    else:
        print("Sorry, not sure what you meant by that")


def board_size():
    while True:
        board_size_given = input("Choose a board size (5 - 10):  ")
        correct_board_sizes = ["5", "6", "7", "8", "9", "10"]
        if board_size_given in correct_board_sizes:
            return int(board_size_given)
        else:
            print("Invalid input! (must be between 5-10)")


def main_menu():
    player_index = 1
    # intro()
    start_menu()
    length_input = board_size()
    board1 = init_board1(length_input)
    board2 = init_board2(length_input)
    ship_placement_phase(player_index, length_input, board1, board2)
    game_play(player_index, length_input, board1, board2)
   


if __name__ == '__main__':
    main_menu()
