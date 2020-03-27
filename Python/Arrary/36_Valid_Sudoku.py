class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9 or len(board[0]) != 9:
            return False
        for i in range(0, 9):
            for j in range(0, 9):
                res = self.checkCell(board, i, j)
                if res == False:
                    return False
        return True

    def checkCell(self, board, r, c):

        n = board[r][c]
        # check column
        for i in range(0, 9):
            if i != r and board[i][c].isdigit() and board[i][c] == n:
                return False
        # check row
        for j in range(0, 9):
            if j != c and board[r][j].isdigit() and board[r][j] == n:
                return False
        # check block
        starti = int(r / 3)
        startj = int(c / 3)
        for i in range(starti * 3, starti * 3 + 3):
            for j in range(startj * 3, startj * 3 + 3):
                if i != r and j != c and board[i][j].isdigit() and board[i][j] == n:
                    return False
        return True