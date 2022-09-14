class Sudoku:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        
    def find_next_empty(self):
        # finds the next row, col on the puzzle that's not filled yet --> rep with -1
        # return row, col tuple (or (None, None) if there is none)

        # keep in mind that we are using 0-8 for our indices
        for r in range(9):
            for c in range(9): # range(9) is 0, 1, 2, ... 8
                if self.puzzle[r][c] == -1:
                    return r, c

        return None, None  # if no spaces in the puzzle are empty (-1)

    def print_board(self):
        print(f'''+-------+-------+-------+
| {self.puzzle[0][0]} {self.puzzle[0][1]} {self.puzzle[0][2]} | {self.puzzle[0][3]} {self.puzzle[0][4]} {self.puzzle[0][5]} | {self.puzzle[0][6]} {self.puzzle[0][7]} {self.puzzle[0][8]} |
| {self.puzzle[1][0]} {self.puzzle[1][1]} {self.puzzle[1][2]} | {self.puzzle[1][3]} {self.puzzle[1][4]} {self.puzzle[1][5]} | {self.puzzle[1][6]} {self.puzzle[1][7]} {self.puzzle[1][8]} |
| {self.puzzle[2][0]} {self.puzzle[2][1]} {self.puzzle[2][2]} | {self.puzzle[2][3]} {self.puzzle[2][4]} {self.puzzle[2][5]} | {self.puzzle[2][6]} {self.puzzle[2][7]} {self.puzzle[2][8]} |
+-------+-------+-------+
| {self.puzzle[3][0]} {self.puzzle[3][1]} {self.puzzle[3][2]} | {self.puzzle[3][3]} {self.puzzle[3][4]} {self.puzzle[3][5]} | {self.puzzle[3][6]} {self.puzzle[3][7]} {self.puzzle[3][8]} |
| {self.puzzle[4][0]} {self.puzzle[4][1]} {self.puzzle[4][2]} | {self.puzzle[4][3]} {self.puzzle[4][4]} {self.puzzle[4][5]} | {self.puzzle[4][6]} {self.puzzle[4][7]} {self.puzzle[4][8]} |
| {self.puzzle[5][0]} {self.puzzle[5][1]} {self.puzzle[5][2]} | {self.puzzle[5][3]} {self.puzzle[5][4]} {self.puzzle[5][5]} | {self.puzzle[5][6]} {self.puzzle[5][7]} {self.puzzle[5][8]} |
+-------+-------+-------+
| {self.puzzle[6][0]} {self.puzzle[6][1]} {self.puzzle[6][2]} | {self.puzzle[6][3]} {self.puzzle[6][4]} {self.puzzle[6][5]} | {self.puzzle[6][6]} {self.puzzle[6][7]} {self.puzzle[6][8]} |
| {self.puzzle[7][0]} {self.puzzle[7][1]} {self.puzzle[7][2]} | {self.puzzle[7][3]} {self.puzzle[7][4]} {self.puzzle[7][5]} | {self.puzzle[7][6]} {self.puzzle[7][7]} {self.puzzle[7][8]} |
| {self.puzzle[8][0]} {self.puzzle[8][1]} {self.puzzle[8][2]} | {self.puzzle[8][3]} {self.puzzle[8][4]} {self.puzzle[8][5]} | {self.puzzle[8][6]} {self.puzzle[8][7]} {self.puzzle[8][8]} |
+-------+-------+-------+''')
        
    def is_valid(self, guess, row, col):
        # figures out whether the guess at the row/col of the puzzle is a valid guess
        # returns True or False

        # for a guess to be valid, then we need to follow the sudoku rules
        # that number must not be repeated in the row, column, or 3x3 square that it appears in

        # let's start with the row
        row_vals = self.puzzle[row]
        if guess in row_vals:
            return False # if we've repeated, then our guess is not valid!

        # now the column
        # col_vals = []
        # for i in range(9):
        #     col_vals.append(puzzle[i][col])
        col_vals = [self.puzzle[i][col] for i in range(9)]
        if guess in col_vals:
            return False

        # and then the square
        row_start = (row // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
        col_start = (col // 3) * 3

        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if self.puzzle[r][c] == guess:
                    return False

        return True

    def solve_sudoku(self):
        # solve sudoku using backtracking!
        # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
        # return whether a solution exists
        # mutates puzzle to be the solution (if solution exists)

        # step 1: choose somewhere on the puzzle to make a guess
        row, col = self.find_next_empty()

        # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
        if row is None:  # this is true if our find_next_empty function returns None, None
            return True 

        # step 2: if there is a place to put a number, then make a guess between 1 and 9
        for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
            # step 3: check if this is a valid guess
            if self.is_valid(guess, row, col):
                # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
                self.puzzle[row][col] = guess
                # step 4: then we recursively call our solver!
                if self.solve_sudoku():
                    return True

            # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
            self.puzzle[row][col] = -1

        # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
        return False

if __name__ == '__main__':
    game = Sudoku([
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ])
    if game.solve_sudoku() is False:
        print("This puzzle is unsolvable!")
    game.print_board()
