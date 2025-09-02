def solve_n_queens(n):
    board = [["."]*n for _ in range(n)]
    res = []

    def is_safe(r,c):
        for i in range(r):
            if board[i][c]=="Q": return False
            if c-(r-i)>=0 and board[i][c-(r-i)]=="Q": return False
            if c+(r-i)<n and board[i][c+(r-i)]=="Q": return False
        return True

    def backtrack(r):
        if r==n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if is_safe(r,c):
                board[r][c]="Q"
                backtrack(r+1)
                board[r][c]="."

    backtrack(0)
    return res

n = int(input("Enter N for N-Queens: "))
solutions = solve_n_queens(n)
print(f"Number of solutions: {len(solutions)}")
for sol in solutions:
    for row in sol:
        print(row)
    print()

# Complexity:
# Time: O(N!)
# Space: O(N^2)
