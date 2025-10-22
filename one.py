N = 4
board = [-1] * N

def is_safe(row, col):
    for r in range(row): 
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False 
    return True  

def solve(row=0):
    if row == N:
        for r in range(N):
            print(" ".join("Q" if board[r] == c else "*" for c in range(N)))
        print()
        return True  

    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
            board[row] = -1
    return False

solve()
