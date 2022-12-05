row1 =  input("Type your row1: ") # "295743861" "195743862"
row2 =  input("Type your row2: ") # "431865927" "431865927"
row3 =  input("Type your row3: ") # "876192543" "876192543"
row4 =  input("Type your row4: ") # "387459216" "387459216"
row5 =  input("Type your row5: ") # "612387495" "612387495"
row6 =  input("Type your row6: ") # "549216738" "549216738"
row7 =  input("Type your row7: ") # "763524189" "763524189"
row8 =  input("Type your row8: ") # "928671354" "928671354"
row9 =  input("Type your row9: ") # "154938672" "254938671"

sudoku = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
numbers = ["1","2","3","4","5","6","7","8","9"]

check_c = 0
check_r = 0
check_t1 = 0
check_t2 = 0
check_t3 = 0
check = False
temp_numbers_row = []
temp_numbers_column = []
temp_numbers_tile1 = []
temp_numbers_tile2 = []
temp_numbers_tile3 = []
round = 0

for a in range(9):
    # print(check_t1)
    # print(check_t2)
    # print(check_t3)
    # print(check_c)
    # print(check_r)
    # print(temp_numbers_tile1)
    if round == 3:
        temp_numbers_tile1 = []
        temp_numbers_tile2 = []
        temp_numbers_tile3 = []
        round = 0
    temp_numbers_row = []
    temp_numbers_column = []
    round += 1
    for b in range(9):
        if sudoku[a][b] not in temp_numbers_row:
            temp_numbers_row.append(sudoku[a][b])
            temp_numbers_row.sort()
        if sudoku[b][a] not in temp_numbers_column:
            temp_numbers_column.append(sudoku[b][a])
            temp_numbers_column.sort()
        if b <= 2:
            if sudoku[a][b] not in temp_numbers_tile1:
                temp_numbers_tile1.append(sudoku[a][b])
                temp_numbers_tile1.sort()
                # print(temp_numbers_tile1)
        if b <= 5 and b > 2:
            if sudoku[a][b] not in temp_numbers_tile2:
                temp_numbers_tile2.append(sudoku[a][b])
                temp_numbers_tile2.sort()
        if b >= 6:
            if sudoku[a][b] not in temp_numbers_tile3:
                temp_numbers_tile3.append(sudoku[a][b])
                temp_numbers_tile3.sort()
        if temp_numbers_row == numbers:
            check_r += 1
        if temp_numbers_column == numbers:
            check_c += 1
        if temp_numbers_tile1 == numbers:
            check_t1 += 1
            temp_numbers_tile1 = []
        if temp_numbers_tile2 == numbers:
            check_t2 += 1
            temp_numbers_tile2 = []
        if temp_numbers_tile3 == numbers:
            check_t3 += 1
            temp_numbers_tile3 = []
        if check_c == 9 and check_r == 9 and check_t1 == 3 and check_t2 ==3 and check_t3 == 3:
            check = True
    
if check == True:
    print("Yes")
else:
    print("No")