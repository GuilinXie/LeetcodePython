# https://leetcode.com/problems/longest-palindromic-substring/discuss/151144/Bottom-up-DP-Logical-Thinking

class Solution:
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        start = 0
        longest = 1
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s) - 1, -1, -1):
            for dist in range(1, len(s)-i):
                j = i + dist
                if dist == 1 and s[i] == s[j]:
                    dp[i][j] = True
                if dist > 1 and s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                if dp[i][j] and j-i+1 > longest:
                    start = i
                    longest = j - i + 1
        return s[start:start+longest]