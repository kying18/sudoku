import pyautogui
import time

grid=[]
while True:
    X= list(input("Row:"))
    ints=[]
    for n in X :
        ints.append(int(n))
    grid.append(ints)
    if len(grid)==9:
        break
    print("ROw :"+str(len(grid))+" complit")


time.sleep(3)



def find_next_empty(puzzle):
    #find the next row , col on the puzzle that's not filled yet --> 0
    #return row ,col tuple (or (none,none)if there is none)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]== 0:
                return r, c
    return None, None # if no spaces in the puzzle are empty(0)

def is_valif(puzzle,guess,row,col):
    #figuers out whtere the huess at the row,clo of the puzzle is a valid guess
    #return True if is valid , False otherwise
    #the row 
    row_vals=puzzle[row]
    if guess in row_vals:
        return False
    # the cloumn
    # column_vals=[]
    # for i in range(9):
    #     column_vals.append(puzzle[i][col])
    column_vals=[puzzle[i][col] for i in range(9)]
    if guess in column_vals:
        return False
    
    # the 3*3 Matrixs
    # we want to get where the 3x3 square starts
    # and iterate over the 3 values in the row/cloumn
    row_start=(row//3)*3 #1//3=0 ,5//3=1, 7//3=2
    col_start=(col//3)*3
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if guess== puzzle[r][c]:
                return False
    # if we get here , these checks pass
    return True


def solve_sudoku(puzzle):
    #solve sudoku uisig backtracking 
    #our puzzle is a list of list , where each inner list is a row in our sudoku puzzle 
    
    #step 1: choose somewhere on the puzzle to make a guess 
    row ,col = find_next_empty(puzzle)

    #step 1.1 :if there's nowhere left , then we're done cuz we only allowed valif inputs
    if row is None:
        return True
    
    #step 2 :if there is a place to put a number , then make a guess between 1 and 9 
    for guess in range(1,10):
        #step 3: check if is valid guess
        if is_valif(puzzle,guess,row,col):
            #step 3.1: if this is valid then place that guess on the puzzle
            puzzle[row][col]=guess
            #Now recurse using this puzzle!
            #step 4 :recursively call our function
            if solve_sudoku(puzzle):
                return True
        #step 5: if not valid or if our guess not solve the puzzel , theen we need to backtrack and try new number 
        puzzle[row][col]=0

    #step 6: if none of the numbers that we
    return False

def printe(matrix):
    final=[]
    str_final=[]
    for i in range(9):
        final.append(matrix[i])
    for lists in final:
        for num in lists:
            str_final.append(str(num))
    counter =[]
    for num in str_final:
        pyautogui.press(num)
        pyautogui.hotkey('right')
        counter.append(num)
        if len(counter)%9==0:
            pyautogui.hotkey('down')
            for i in range(8):
                pyautogui.hotkey('left')



print(solve_sudoku(grid))
printe(grid)
print(grid)
