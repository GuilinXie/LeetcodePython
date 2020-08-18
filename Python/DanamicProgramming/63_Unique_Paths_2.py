# Solution 1 - dp- Space O(M*N) - beat 90%
# refer: https://leetcode.com/problems/unique-paths-ii/discuss/146073/Python-DP-beat-100-python-submissions
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [[0] * c for _ in range(r)]
        dp[0][0] = 1 if grid[0][0] == 0 else 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i - 1 >= 0:
                        dp[i][j] += dp[i-1][j]
                    if j - 1 >= 0:
                        dp[i][j] += dp[i][j-1]
        return dp[-1][-1]

# Solution 2 - dp - Space O(N) - beat 80%
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        c = len(grid[0])
        dp = [0] * c
        
        dp[0] = 1
        
        for row in grid:
            for j in range(c):
                if row[j] == 1:
                    # if grid[0][0] == 1, then this step will set dp[0] = 0 back from the initial dp[0] = 1
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
                    
        return dp[c-1]
