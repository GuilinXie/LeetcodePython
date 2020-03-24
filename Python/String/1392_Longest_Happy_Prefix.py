# Solution 1 - cheating solution, O(n^2), superisely AC
class Solution:
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 0:
            return ""
        ans = 0
        for i in range(0, n):
            if s[0:i] == s[n-i:]:
                ans = i
        return s[:ans]

# Solution 2 - Use KMP's getNext idea
class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        ret = [-1] * (N + 1)
        j = -1
        for i in range(0, N):
            while j >= 0 and s[i] != s[j]:
                j = ret[j]
            j += 1
            ret[i + 1] = j
        end = ret[-1]
        return s[0:end]