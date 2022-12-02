def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+", "-------+"*(len(board)), sep='')
    for j in range(0,(len(board))):
        print("|", "       |"*(len(board)), sep='')
        print("|", sep='', end="")
        for i in range(0,(len(board))-1):
            print(str(board [j] [i]).center(7," "),"|", sep='', end="")
        print(str(board [j] [(len(board))-1]).center(7," "),"|", sep='')
        print("|", "       |"*(len(board)), sep='')
        print("+", "-------+"*(len(board)), sep='')

    # print("+-------+-------+-------+")
    # print("|       |       |       |")
    # print("|   ",board [0] [0],"   |   ",board [0] [1],"   |   ",board [0] [2],"   |", sep='')
    # print("|       |       |       |")
    # print("+-------+-------+-------+")
    # print("|       |       |       |")
    # print("|   ",board [1] [0],"   |   ",board [1] [1],"   |   ",board [1] [2],"   |", sep='')
    # print("|       |       |       |")
    # print("+-------+-------+-------+")
    # print("|       |       |       |")
    # print("|   ",board [2] [0],"   |   ",board [2] [1],"   |   ",board [2] [2],"   |", sep='')
    # print("|       |       |       |")
    # print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    free_field = make_list_of_free_fields(board)
    move = int(input("Enter move (number): "))
    while move not in free_field:
        move = int(input("Not a valid move, try again:"))
    for row in board:
        if move in row:
            board [board.index(row)][row.index(move)] = 'o'
    # print(board)
    # count_rows = 0
    # while count_rows != 'found':
    #     for row in board:
    #         print(row)
    #         print(count_rows)
    #         if move in row and move != 'X' and move != 'o':
    #             board [count_rows] [row.index(move)] = 'o'
    #             count_rows = 'found'
    #             break
    #         elif count_rows == 2:
    #             move = int(input("Not a valid move, try again:"))
    #             count_rows = 0
    #             continue
    #         else:
    #             count_rows+=1
    #             continue
    return board



def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_field = []
    for number in range(1,((len(board))**2)+1):
        for row in board:
            if number in row:
                free_field.append(number)
    # print(free_field)
    return free_field

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    p_diagonal=0
    n_diagonal=0
    for row in range(0,(len(board))):
        c_count = 0
        #if c_count == 0:
        r_count = 0
        for column in range(0,(len(board))):
            if board[row][column] == sign:
                r_count += 1
                # print("r_count")
                # print(r_count)
                # if r_count == 3 or c_count == 3:
                #     print(sign, "won")
                #     print("test")
                #     finish = True
                #     return finish
                # if board[column][row] == sign:
                #     c_count +=1
                #     print("c_count")
                #     print(c_count)
                #     if r_count == 3 or c_count == 3:
                #         print(sign, "won")
                #         print("test")
                #         finish = True
                #         return finish
                # continue
            if board[column][row] == sign:
                c_count +=1
                # print("c_count")
                # print(c_count)
                # if r_count == 3 or c_count == 3:
                #     print(sign, "won")
                #     print("test")
                #     finish = True
                #     return finish
                # continue
            if row == column and board[row][column] == sign:
                n_diagonal+=1
            if (len(board)-1-row) == column and board[row][column] == sign:
                p_diagonal+=1
            # board[0][0] == sign and board[1][1] == sign and board [2][2] == sign or board[0][2] == sign and board[1][1] == sign and board [2][0] == sign:
            #     print(sign, "won")
            #     print("test")
            #     finish = True
            #     return finish
            if r_count == len(board) or c_count == len(board) or n_diagonal == len(board) or p_diagonal == len(board):
                print(sign, "won")
                finish = True
                return finish
    if make_list_of_free_fields(board) == []:
        print("Draw")
        return True

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_field = make_list_of_free_fields(board)
    random_move = randrange(1,((len(board)**2)+1))
    while random_move not in free_field:
        random_move = randrange(1,((len(board)**2)+1))
    for row in board:
        if random_move in row:
            board [board.index(row)][row.index(random_move)] = 'X'
    return board

from random import randrange



# board = [[[] for row in range(3)] for  column in range(3)]
# board [0] [0] = 1
# board [0] [1] = 2
# board [0] [2] = 3
# board [1] [0] = 4
# board [1] [1] = 'X'
# board [1] [2] = 6
# board [2] [0] = 7
# board [2] [1] = 8
# board [2] [2] = 9

board_size = input("Type the size of the board you want, board size needs to an integer number: ")
while board_size.isdigit() == False:
    board_size = input("Type a number for the board size. It needs to be atleast 3 and an integer. Number:")
board_size = int(board_size)
while board_size < 3:
    board_size = input("Board size needs be atleast 3. Type new board size: ")
    while board_size.isdigit() == False:
        board_size = input("Type an integer number for the board size. Number:")
    board_size = int(board_size)

board = [[[] for row in range(board_size)] for  column in range(board_size)]
number = 1
for j in range(0,board_size):
    for i in range(0,board_size):
        board [j][i] = number
        number+=1

board [1] [1] = 'X'


finish = False
display_board(board)
enter_move(board)
display_board(board)
draw_move(board)
display_board(board)
while finish != True:
    enter_move(board)
    display_board(board)
    finish = victory_for(board, 'o')
    if finish == True:
        break
    draw_move(board)
    display_board(board)
    finish = victory_for(board, 'X')
    if finish == True:
        break
