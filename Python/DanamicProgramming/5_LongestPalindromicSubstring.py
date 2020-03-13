# https://leetcode.com/problems/longest-palindromic-substring/discuss/151144/Bottom-up-DP-Logical-Thinking

class Solution:
    # def longestPalindrome(self, s):
    #     if len(s) <= 1:
    #         return s
    #     start = 0
    #     longest = 1
    #     dp = [[False] * len(s) for _ in range(len(s))]
    #     for i in range(len(s)):
    #         dp[i][i] = True
    #     for i in range(len(s) - 1, -1, -1):
    #         for dist in range(1, len(s)-i):
    #             j = i + dist
    #             if dist == 1 and s[i] == s[j]:
    #                 dp[i][j] = True
    #             if dist > 1 and s[i] == s[j] and dp[i+1][j-1]:
    #                 dp[i][j] = True
    #             if dp[i][j] and j-i+1 > longest:
    #                 start = i
    #                 longest = j - i + 1
    #     return s[start:start+longest]
    def __init__(self):
        self.dp = None

    def findLongestCommon(self, s1, s2):
        if len(s1) <= 0 or len(s2) <= 0:
            return
        m = len(s1)
        n = len(s2)
        self.dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    self.dp[i][j] = 1 + self.dp[i - 1][j - 1]
                else:
                    self.dp[i][j] = 0
        print(self.dp)
if __name__ == "__main__":
    s = Solution()
    s.findLongestCommon("babad", "dabab")
    print(s.dp)
