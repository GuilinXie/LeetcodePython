class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return
        rowBegin = 0
        colBegin = 0
        rowEnd = len(matrix) - 1
        colEnd = len(matrix[0]) - 1
        res = []
        while rowBegin <= rowEnd and colBegin <= colEnd:
            # traverse right
            for j in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][j])
            rowBegin += 1
            # traverse down
            for j in range(rowBegin, rowEnd + 1):
                res.append(matrix[j][colEnd])
            colEnd -= 1
            # traverse left
            if rowBegin <= rowEnd:
                for j in range(colEnd, colBegin - 1, -1):
                    res.append(matrix[rowEnd][j])
            rowEnd -= 1
            # traverse up
            if colBegin <= colEnd:
                for j in range(rowEnd, rowBegin - 1, -1):
                    res.append(matrix[j][colBegin])
            colBegin += 1
        return res