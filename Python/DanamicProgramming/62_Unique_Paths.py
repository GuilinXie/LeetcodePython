# # Solution 1 - beat 85%
# # Math
from math import factorial as f
class Solution:
    # calculate the num of combination
    def nCr(self, n, r):
        return f(n) // f(r) // f(n-r)
    
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1
        return self.nCr(m + n - 2, m - 1)

# TLE
class Solution:       
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
    

# dp
# beat 95%
class Solution:
    def uniquePaths(self, m, n):
        dp = [[1] * n for _ in range(m)]
        
        for col in range(1, m):
            for row in range(1, n):
                dp[col][row] = dp[col-1][row] + dp[col][row-1]
        return dp[m-1][n-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
