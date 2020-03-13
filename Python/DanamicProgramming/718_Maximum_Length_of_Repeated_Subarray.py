class Solution:

    # Method 1: Recursive, but I did not find how to cache this
    # So time complexity is too high
    # def __init__(self):
    #     self.cache = dict()

    def findLength(self, A, B):
        return self.findLengthHelp(A, B, 0)

    def findLengthHelp(self, A, B, res):
        #         key = str(len(A)) + "_" + str(len(B))
        if len(A) <= 0 or len(B) <= 0:
            #             self.cache[key] = res
            return res

        #         # if key in self.cache:
        #         #     return self.cache[key]
        if A[-1] == B[-1]:
            res = self.findLengthHelp(A[:-1], B[:-1], res + 1)
        res = max(res, self.findLengthHelp(A[:-1], B, 0), self.findLengthHelp(A, B[:-1], 0))
        #         self.cache[key] = res
        return res

    # Method 2 - dp, it need to find the max in dp for substring
    # but for subsequence, the dp can accumulate, so return dp[m][n]
    def findLength(self, A, B):
        if len(A) <= 0 or len(B) <= 0:
            return 0
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j])
        return res