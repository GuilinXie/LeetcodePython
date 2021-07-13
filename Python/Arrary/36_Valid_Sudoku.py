# Check row / column/ sub_board separately
# Time complexity O (m * n)
# Space complexity O(max(m, n)), where m = 9, n = 9
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9 or len(board[0]) != 9:
            return False
        
        for i in range(9):
            if not check_row(board, i):
                return False
            
        for j in range(9):
            if not check_column(board, j):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check_sub_board(board, i, j):
                    return False
        return True

def check_row(board, i):
    seen = set()
    for j in range(9):
        if board[i][j] != ".":
            if board[i][j] in seen:
                return False
            else:
                seen.add(board[i][j])
    return True

def check_column(board, j):
    seen = set()
    for i in range(9):
        if board[i][j] != ".":
            if board[i][j] in seen:
                return False
            else:
                seen.add(board[i][j])
    return True

def check_sub_board(board, i, j):
    seen = set()
    for new_i in range(i, i + 3):
        for new_j in range(j, j + 3):
            if board[new_i][new_j] != ".":
                if board[new_i][new_j] in seen:
                    return False
                else:
                    seen.add(board[new_i][new_j])
    return True
        


# Solution 1: record digit = board[r][c], then change it to a special character to avoid too many checks in self.isValid()
# beat 82%
class Solution:
    def isValidSudoku(self, board):
        if len(board) != 9 or len(board[0]) != 9:
            return False
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    digit = board[r][c]
                    board[r][c] = "#"
                    if not self.isValid(board, r, c, digit):
                        return False
                    board[r][c] = digit
        return True
    
    def isValid(self, board, r, c, digit):
        # check row, column
        
        for i in range(9):
            if board[r][i] == digit:
                return False
            if board[i][c] == digit:
                return False
        
        # check block
        startRow = r // 3
        startCol = c // 3
        for i in range(startRow * 3, startRow * 3 + 3):    # do not forget the * 3
            for j in range(startCol * 3, startCol * 3 + 3):
                if board[i][j] == digit:
                    return False
        return True


# Solution 2: Would check if the current cell, too much check....
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
