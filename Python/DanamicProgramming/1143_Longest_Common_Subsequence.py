class Solution:
    # Method 1 - Recursive and Cache
    # key = "text1" + "_" + "text2", if using key like this, then too much memory
    # key = str(len(text1)) + "_" + str(len(text2)), this works
    def __init__(self):
        self.cache = dict()

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        key = str(len(text1)) + "_" + str(len(text2))
        if text1 == "" or text2 == "":
            self.cache[key] = 0
            return 0
        if key in self.cache:
            return self.cache[key]
        if text1[-1] == text2[-1]:
            res = 1 + self.longestCommonSubsequence(text1[:-1], text2[:-1])
            self.cache[key] = res
            return res
        else:
            res = max(self.longestCommonSubsequence(text1, text2[:-1]),
                      self.longestCommonSubsequence(text1[:-1], text2))
            self.cache[key] = res
            return res

    # Method 2 - DP
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) <= 0 or len(text2) <= 0:
            return 0
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]