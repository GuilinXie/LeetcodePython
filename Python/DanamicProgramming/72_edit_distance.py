class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        m, n = len(word1) + 1, len(word2) + 1
        dp = [[0] * n for _ in range(m)]
        for i in range(1, m):
            dp[i][0] = i
        for j in range(1, n):
            dp[0][j] = j
        for i in range(1, m):
            for j in range(1, n):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    replace = dp[i - 1][j - 1] + 1
                    delete = dp[i - 1][j] + 1
                    insert = dp[i][j - 1] + 1
                    dp[i][j] = min(replace, delete, insert)
        return dp[m-1][n-1]

'''
reference:
https://leetcode.com/problems/edit-distance/discuss/25846/C%2B%2B-O(n)-space-DP
'''