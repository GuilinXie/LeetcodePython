class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rowCnt = [0] * n
        self.colCnt = [0] * n
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        if player == 1:
            self.rowCnt[row] += 1
            self.colCnt[col] += 1
            if row == col:
                self.diag1 += 1
            if row + col == self.n - 1:
                self.diag2 += 1
        if player == 2:
            self.rowCnt[row] -= 1
            self.colCnt[col] -= 1
            if row == col:
                self.diag1 -= 1
            if row + col == self.n - 1:
                self.diag2 -= 1

        if abs(self.rowCnt[row]) == self.n or abs(self.colCnt[col]) == self.n or \
                abs(self.diag1) == self.n or abs(self.diag2) == self.n:
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)