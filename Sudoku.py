def is_safe(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    startRow, startCol = 3*(row//3), 3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[startRow+i][startCol+j] == num:
                return False
    return True

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1,10):
                    if is_safe(board,i,j,num):
                        board[i][j] = num
                        if solve(board): return True
                        board[i][j] = 0
                return False
    return True

board = []
print("Enter Sudoku grid (9x9, 0 for empty):")
for _ in range(9):
    board.append(list(map(int,input().split())))

if solve(board):
    for row in board:
        print(row)
else:
    print("No solution")

# Complexity: O(9^(N*N)) worst-case
