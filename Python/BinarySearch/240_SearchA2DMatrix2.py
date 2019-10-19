class Solution:

    def searchMatrix(self, matrix, target):
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        i, j = 0, col - 1
        while i >= 0 and i < row and j >= 0 and j < col:
            curr = matrix[i][j]
            if curr == target:
                return True
            elif curr < target:
                i += 1
            else:
                j -= 1
        return False