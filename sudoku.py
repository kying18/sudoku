from pprint import pprint


def turn_puzzle(puzzle):
    # rewrith the sudoku as list of lists, where each inner list is a colume in our sudoku puzzle
    turned_puzzle = []
    for c in range(9):
        turned_row = []
        for r in range(9):
            turned_row += [puzzle[r][c]]
        turned_puzzle += [turned_row]
    return turned_puzzle

def list_of_squares(puzzle):
    # rewrith the sudoku as list of lists, where each inner lists are the small square (3x3) in our sudoku puzzle
    insideout_board = [[0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0]]
    for r in range(9):
        for c in range(9):
            insideout_board[c//3+3*(r//3)][c%3+3*(r%3)] = puzzle[r][c]
    return insideout_board

def find_next_empty(puzzle, row):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(row,9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, turned_puzzle, insideout_puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # for a guess to be valid, then we need to follow the sudoku rules
    # that number must not be repeated in the row, column, or 3x3 square that it appears in

    # let's start with the row
#     row_vals = puzzle[row]
    if guess in puzzle[row]:
        return False # if we've repeated, then our guess is not valid!

    # check the square secondly
#     square_vals = insideout_puzzle[col//3+3*(row//3)]
    if guess in insideout_puzzle[col//3+3*(row//3)]:
        return False
    
    # finaly check the column
#     col_vals = turned_puzzle[col]
    if guess in turned_puzzle[col]:
        return False
    
    return True

def solve_sudoku(puzzle, turned_puzzle, insideout_puzzle, row=0):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)
    
    # step 1: find the next empty spot in the sudoku, from left to right and top to bottom 
    row, col = find_next_empty(puzzle, row)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:  # this is true if our find_next_empty function returns None, None
        return True 
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
        # step 3: check if this is a valid guess
        if is_valid(puzzle, turned_puzzle, insideout_puzzle, guess, row, col):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            turned_puzzle[col][row] = guess
            insideout_puzzle[col//3+3*(row//3)][col%3+3*(row%3)] = guess
            # step 4: then we recursively call our solver!
            if solve_sudoku(puzzle, turned_puzzle, insideout_puzzle, row):
                return True
        
    # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
    puzzle[row][col] = -1
    turned_puzzle[col][row] = -1
    insideout_puzzle[col//3+3*(row//3)][col%3+3*(row%3)] = -1

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    # rewrith the sudoku in two different basis, to reduce the time of the is_valid() function takes
    turned_board = turn_puzzle(example_board)
    insideout_board = list_of_squares(example_board)
    print(solve_sudoku(example_board, turned_board, insideout_board))
    pprint(example_board)
