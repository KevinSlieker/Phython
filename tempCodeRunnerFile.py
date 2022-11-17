board_size = 10

board = [[[] for row in range(board_size)] for  column in range(board_size)]
number = 1
for j in range(0,board_size):
    for i in range(0,board_size):
        board [j][i] = number
        number+=1
# board [0] [0] = 1
# board [0] [1] = 2
# board [0] [2] = 3
# board [1] [0] = 4
board [1] [1] = 'X'
# board [1] [2] = 6
# board [2] [0] = 7
# board [2] [1] = 8
# board [2] [2] = 9



print("+", "-------+"*board_size, sep='')
for j in range(0,board_size):
    print("|", "       |"*board_size, sep='')
    print("|", sep='', end="")
    for i in range(0,board_size-1):
        print(str(board [j] [i]).center(7," "),"|", sep='', end="")
    print(str(board [j] [board_size-1]).center(7," "),"|", sep='')
    print("|", "       |"*board_size, sep='')
    print("+", "-------+"*board_size, sep='')