class Solution:
    def maxAreaOfIsland(self, A):
        if len(A) <= 0 or len(A[0]) <= 0:
            return 0
        r, c = len(A), len(A[0])
        res = 0
        for i in range(r):
            for j in range(c):
                if A[i][j] == 1:
                    tmp_res = self.dfs(A, i, j)
                    if tmp_res > res:
                        res = tmp_res
        return res

    def dfs(self, A, i, j):
        if 0 <= i < len(A) and 0 <= j < len(A[0]) and A[i][j] == 1:
            A[i][j] = 0
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            size = 1
            for new_i, new_j in neighbors:
                size += self.dfs(A, new_i, new_j)
            return size
        return 0