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
    
    # Method 2 - AC - same idea as previous, maybe code can be more clear
    # check conditions before going into dfs
    
    class Solution:
    def maxAreaOfIsland(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if len(A) <= 0 or len(A[0]) <= 0:
            return 0
        R, C = len(A), len(A[0])
        ans = 0
        for i in range(0, R):
            for j in range(0, C):
                if A[i][j] == 1:
                    cand = self.dfs(A, i, j)
                    ans = max(ans, cand)
        return ans
    
    def dfs(self, A, i, j):
        ans = 1
        A[i][j] = "#"
        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        R, C = len(A), len(A[0])
        for new_i, new_j in neighbors:
            if 0 <= new_i < R and 0 <= new_j < C and A[new_i][new_j] == 1:
                ans += self.dfs(A, new_i, new_j)
        return ans
