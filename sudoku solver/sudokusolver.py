#grid = [[0 for j in range(9)] for i in range(9)]
import time

def not_complete(board):
    for i in board:
        if 0 in i:
            return True
    return False

#will return True if the inputted number is not in the row
def check_row(board, row_num, num):
    if num in board[row_num]:
        return False
    else:
        return True


#will return True if inputted number is not in the column
def check_col(board, col_num, num):
    not_in_col = True
    for i in range(9):
        if num == board[i][col_num]:
            not_in_col = False
    return not_in_col

def get_box_values(board, row, col):
    values = []
    if row<3:
        if col<3:
            for i in range(3):
                values.append(board[i][0:3])
        elif col<6:
            for i in range(3):
                values.append(board[i][3:6])
        elif col<9:
            for i in range(3):
                values.append(board[i][6:9])
    elif row<6:
        if col<3:
            for i in range(3,6):
                values.append(board[i][0:3])
        elif col<6:
            for i in range(3,6):
                values.append(board[i][3:6])
        elif col<9:
            for i in range(3,6):
                values.append(board[i][6:9])
    elif row<9:
        if col<3:
            for i in range(6,9):
                values.append(board[i][0:3])
        elif col<6:
            for i in range(6,9):
                values.append(board[i][3:6])
        elif col<9:
            for i in range(6,9):
                values.append(board[i][6:9])
    return values

#returns True if inputted number not in box
def check_box(board, row, col, num):
    box_values = get_box_values(board, row, col)

    for row in box_values:
        if num in row:

            return False

    return True

def find_possibilities(board,pos):
    possibilities = []
    for i in range(1,10):
        if check_box(board, pos[0], pos[1], i) and check_row(board, pos[0], i) and check_col(board, pos[1], i):
            possibilities.append(i)

    return possibilities

def solver(board):
    if not not_complete(board):
        return board
    else:
        for x in range(9):
            for y in range(9):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break
        
        possibilities = find_possibilities(board, [i,j])
        for choice in possibilities:
            board[i][j] = choice

            value = solver(board)
            if value != None:
                return board
        board[i][j] = 0
