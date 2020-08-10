# beat 10%, further optimization - only keep the (row, col) number to record
# time complexity: O(N!), there is N possibilities to put the first queen, N * (N - 1) to put the second queen, and so on...
# space complexity: O(N) to keep an information about diagonals and rows

class Solution:
    def solveNQueens(self, n):
        res = []
        board = [["."] * n for _ in range(n)]
        self.solver(board, res, 0)
        return res
    
    def solver(self, board, res, row):
        L = len(board)
        if row == L:
            res.append(["".join(r) for r in board])
            return
        for col in range(L):
            if self.isValid(board, row, col):
                board[row][col] = "Q"
                self.solver(board, res, row + 1)
                board[row][col] = "."
   
    
    def isValid(self, board, row, col):
        L = len(board)
        # if row < 0 or row >= L or col < 0 or col >= L:
        #     return False
        for i in range(L):
            if board[i][col] == "Q":
                return False
            if board[row][i] == "Q":
                return False
        for i in range(L):
            for j in range(L):
                if i + j == row + col or i - j == row - col:
                    if board[i][j] == "Q":
                        return False
        return True
