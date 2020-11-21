import time

start_time = time.time()

row1 = [0,1,0,0,3,4,0,0,0]
row2 = [0,0,0,0,7,0,0,2,0]
row3 = [3,4,2,0,0,0,0,0,0]
row4 = [4,3,8,0,0,0,0,0,0]
row5 = [0,0,0,0,0,0,5,6,0]
row6 = [0,0,0,0,4,9,0,0,0]
row7 = [8,0,0,7,0,0,0,0,9]
row8 = [0,0,0,9,0,5,1,0,7]
row9 = [9,0,3,0,0,0,0,0,0]
board = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
print(board)

### RULES! ###
# unique int (1-9) in row
# unique int (1-9) in column
# unique int (1-9) in sector

###
# ARTEFACT FROM TESTING #
###
#Result check
# Check rows
#def row_check(board):
#    row_result = []
#    row_hope = [True, True, True, True, True, True, True, True, True]
#    for i in range(9):
#        row_result.append({1, 2, 3, 4, 5, 6, 7, 8, 9} == set(board[i]))
#    print(row_result == row_hope)
#
# Check columns
#def column_check(board):
#    column_result = []
#    column_hope = [True, True, True, True, True, True, True, True, True]
#    columns = {i:[] for i in range(9)}
#    board_sv = []
#    for i in range(9):
#        for j in range(9):
#            board_sv.append(board[j][i])
#    x = 0
#    y = len(board_sv)
#    board_to_columns = []
#    for i in range(x, y, 9):
#        x = i
#        board_to_columns.append(board_sv[x:x+9])
#    for i in range(9):
#        columns[i] = board_to_columns[i]
#        column_result.append({1, 2, 3, 4, 5, 6, 7, 8, 9} == set(columns[i]))
#    print(column_result == column_hope)
#
###
# ARTEFACT FROM TESTING #
###

# Find empty cell
cell = [0,0]
def find_empty_cell(board, cell):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                cell[0] = row
                cell[1] = column
                return True
    return False

# Check values in row/column
def check_values_row_column(board, cell, value):
    for i in range(9):
        if board[cell[0]][i] == value or board[i][cell[1]] == value:
            return True
    return False

# Check values in sector
# [0,0]-[2,2]
# [0,3]-[2,5]  - cell[x]//3 == 0, 1, 2 - (cell[x]//3)*3 == 0, 3, 6
# [0,6]-[2,8]  - cell[y]//3 == 0, 1, 2 - (cell[x]//3)*3 == 0, 3, 6 ->[0:0][0:3][0:6], [3:0][3:3][3:6], [6:0][6:3][6:6]

# [3,0]-[5,2]
# [3,3]-[5,5]
# [3,6]-[5,8]

# [6,0]-[8,2]
# [6,3]-[8,5]
# [6,6]-[8,8]

def check_values_sector(board, cell, value):
    for i in range((cell[0]//3)*3, ((cell[0]//3)*3)+3):
        for j in range((cell[1]//3)*3, ((cell[1]//3)*3)+3):
            if board[i][j] == value:
                return True
    return False

def solve(board):
    cell = [0,0]
    if find_empty_cell(board, cell) == False:
        print("done")
        print(board)
        return True
    else:
        for value in range(1,10):
            if check_values_row_column(board, cell, value) == False and check_values_sector(board, cell, value) == False:
                board[cell[0]][cell[1]] = value

                if solve(board):
                    return True
                else:
                    board[cell[0]][cell[1]] = 0
        return False

solve(board)
print("--- {} seconds ---".format(time.time() - start_time))
