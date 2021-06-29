def print_puzzle(arr):
    for i in range (0, 9):
        for j in range (0, 9):
            print(arr[i][j], end=" ")
        print()
        
def find_empty(arr, l):
    for row in range(0, 9):
        for col in range(0, 9):
            if(arr[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False

def used_row(arr, row, num):
    for i in range(0, 9):
        if(arr[row][i]==num):
            return True
    return False

def used_col(arr, col, num):
    for j in range(0, 9):
        if(arr[j][col]==num):
            return True
    return False

def used_box(arr, row, col, num):
    for i in range(0,3):
        for j in range(0, 3):
            if(arr[i+row][j+col]==num):
                return True
    return False        

def check_valid(arr, row, col, num):
    if(used_row(arr, row, num)==True):
        return False
    if(used_col(arr, col, num)==True):
        return False
    if(used_box(arr, row-row%3, col-col%3, num)==True):
        return False
    return True
        
def solve(arr):
    l=[0, 0];
    if(find_empty(arr, l)==False):
        return True
    row=l[0]
    col=l[1]
    
    for num in range(1, 10):
        if(check_valid(arr, row, col, num)==True):
            arr[row][col]=num
            
            if(solve(arr)==True):
                return True
            arr[row][col]=0
    return False

#puzzle=[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          #[5, 2, 0, 0, 0, 0, 0, 0, 0],
          #[0, 8, 7, 0, 0, 0, 0, 3, 1],
          #[0, 0, 3, 0, 1, 0, 0, 8, 0],
          #[9, 0, 0, 8, 6, 3, 0, 0, 5],
          #[0, 5, 0, 0, 9, 0, 6, 0, 0],
          #[1, 3, 0, 0, 0, 0, 2, 5, 0],
          #[0, 0, 0, 0, 0, 0, 0, 7, 4],
          #[0, 0, 5, 2, 0, 6, 3, 0, 0]]
#if(solve(puzzle)==True):
    #print_puzzle(puzzle)
#else:
    #print("Invalid Puzzle")