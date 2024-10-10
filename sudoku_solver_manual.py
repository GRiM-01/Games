def valid(grid, row, col, number):
    for x in range(9):
        if grid[row][x] == number:
            return False       

    for x in range(9):
        if grid[x][col] == number:
            return False

    corner_row = row - row % 3
    corner_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[corner_row + i][corner_col + j] == number:
                return False
                
    return True


def solveSudoku(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1) 
    
    for num in range(1, 10):
        if valid(grid, row, col, num): 
            grid[row][col] = num
            if solveSudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0  # Reset the cell if no number works
    
    return False  # Trigger backtracking if no valid number was found


sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solveSudoku(sudoku_grid, 0, 0):
    for row in sudoku_grid:
        print(row)
else:
    print("No solution exists")