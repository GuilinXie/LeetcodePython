class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if board == None or len(board) != 9 or len(board[0]) != 9:
            return
        self.solve(board)

    def solve(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    for k in "123456789":
                        check = self.isValid(board, i, j, k)
                        if check:
                            board[i][j] = k
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    def isValid(self, board, r, c, k):
        for i in range(0, 9):
            # check column
            if board[r][i] != "." and board[r][i] == k:
                return False
            # check row
            if board[i][c] != "." and board[i][c] == k:
                return False

        # check block
        starti = int(r / 3)
        startj = int(c / 3)
        for i in range(starti * 3, starti * 3 + 3):
            for j in range(startj * 3, startj * 3 + 3):
                if board[i][j] != "." and board[i][j] == k:
                    return False
        return True