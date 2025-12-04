def print_grid(grid):
    for row in grid:
        print(row)

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    empty_cell = find_empty(grid)

    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

print("Enter the Sudoku puzzle (9 rows, numbers separated by spaces):")

puzzle = []
for i in range(9):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    if len(row) != 9:
        print("❌ Each row must contain exactly 9 numbers!")
        exit()
    puzzle.append(row)

if solve_sudoku(puzzle):
    print("\nSolved Sudoku:")
    print_grid(puzzle)
else:
    print("No solution exists.")
