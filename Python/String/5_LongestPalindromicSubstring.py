# https://leetcode.com/problems/longest-palindromic-substring/discuss/151144/Bottom-up-DP-Logical-Thinking

class Solution:

# solution 1 - Brute Force
    # def longestPalindrome(self, s: str) -> str:
    #     if len(s) <= 0:
    #         return ""
    #     ans = ""
    #     for i in range(len(s)):
    #         for j in range(i, len(s)+1):
    #             subStr = s[i:j+1]
    #             reverse = subStr[::-1]
    #             if subStr == reverse and len(subStr) > len(ans):
    #                 ans = subStr
    #     return ans
    
# solution 2 - expanding
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start:end + 1]

    def expandAroundCenter(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j - i - 1

# solution 3 - dp
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