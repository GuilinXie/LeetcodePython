# Rotate 90 degrees (clockwise)
# if it is 90 degrees (anti-clockwise), need to consider i1 + j2 = i2 + j1 to change(probably)
# beat 90%
class Solution:
    def rotate(self, matrix):
        matrix.reverse()
        # list(map(list, list(zip(*matrix))))  # not in-place, zip(*A) could get from columns
        for i in range(0, len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
