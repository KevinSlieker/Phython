def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board [0] [0],"   |   ",board [0] [1],"   |   ",board [0] [2],"   |", sep='')
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board [1] [0],"   |   ",board [1] [1],"   |   ",board [1] [2],"   |", sep='')
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board [2] [0],"   |   ",board [2] [1],"   |   ",board [2] [2],"   |", sep='')
    print("|       |       |       |")
    print("+-------+-------+-------+")

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
    for number in range(1,10):
        for row in board:
            if number in row:
                free_field.append(number)
    # print(free_field)
    return free_field

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board == [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]:
        print()
    
    for row in range(0,3):
        c_count = 0
        r_count=0
        for column in range(0,3):
            if r_count == 3 or c_count == 3:
                print(sign, "won")
                break
            if board[row][column] == sign:
                r_count =+1
                continue
            if board[column][row] == sign:
                c_count+=1
                continue

            



    for row in board:
        if row == [sign, sign, sign]:
            print(sign, "won")
    return

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_field = make_list_of_free_fields(board)
    random_move = randrange(1,9)
    while random_move not in free_field:
        random_move = randrange(1,9)
    for row in board:
        if random_move in row:
            board [board.index(row)][row.index(random_move)] = 'X'
    return board

from random import randrange



board = [[[] for row in range(3)] for  column in range(3)]
board [0] [0] = 1
board [0] [1] = 2
board [0] [2] = 3
board [1] [0] = 4
board [1] [1] = 'X'
board [1] [2] = 6
board [2] [0] = 7
board [2] [1] = 8
board [2] [2] = 9
print(board)

display_board(board)
enter_move(board)
display_board(board)
draw_move(board)
display_board(board)
