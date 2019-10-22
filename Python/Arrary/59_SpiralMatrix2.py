class Solution:
    def generateMatrix(self, n):
        if n <= 0:
            return
        rowBegin = 0
        rowEnd = n - 1
        colBegin = 0
        colEnd = n - 1
        matrix = [[0] * n for _ in range(n)]
        num = 1
        while rowBegin <= rowEnd and colBegin <= colEnd:
            for j in range(colBegin, colEnd + 1):
                matrix[rowBegin][j] = num
                num += 1
            rowBegin += 1
            for j in range(rowBegin, rowEnd + 1):
                matrix[j][colEnd] = num
                num += 1
            colEnd -= 1
            for j in range(colEnd, colBegin - 1, -1):
                if rowBegin <= rowEnd:  # with this condition, it works even if it is a m*n matrix
                    matrix[rowEnd][j] = num
                    num += 1
            rowEnd -= 1
            for j in range(rowEnd, rowBegin - 1, -1):
                if colBegin < colEnd:
                    matrix[j][colBegin] = num
                    num += 1
            colBegin += 1
        return matrix

if __name__ == "__main__":
    s = Solution()
    res = s.generateMatrix(3,4)
    print (res)