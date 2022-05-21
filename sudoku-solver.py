def find_next_empty(puzzle):
    # finds next r, c on puzzle that's not filled yet (if 0)
    # return row, col tuple

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c

    return None, None # if no spaces are empty

def is_valid(puzzle, guess, r, c):
    
    # check rows
    row_vals = puzzle[r]
    if guess in row_vals:
        return False

    # check cols
    for i in puzzle[r]:
        if guess == i:
            return False
    
    # check 3 x 3
    row_start = (r // 3) * 3
    col_start = (c // 3) * 3

    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if puzzle[i][j] == guess:
                return False

    return True

def sudoku_solver(puzzle):
    
    # choose somewhere on puzzle to make a guess
    row, col = find_next_empty(puzzle)

    if row == None:
        return True
    
    for guess in range(1, 10):
        # check if its valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if sudoku_solver(puzzle):
                return True

        # if not valid or the guess did not solve puzzle, 
        # then backtrack and try new number
        puzzle[row][col] = -1 # reset value
    
    # if unable to solve puzzle, return False
    return False
        

# test - sample:
s = [[0,0,4,0,0,0,0,6,7],
[3,0,0,4,7,0,0,0,5],
[1,5,0,8,2,0,0,0,3],
[0,0,6,0,0,0,0,3,1],
[8,0,2,1,0,5,6,0,4],
[4,1,0,0,0,0,9,0,0],
[7,0,0,0,8,0,0,4,6],
[6,0,0,0,1,2,0,0,0],
[9,3,0,0,0,0,7,1,0]]

print (sudoku_solver(s))