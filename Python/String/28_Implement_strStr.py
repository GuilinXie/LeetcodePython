# Solution 1 - Naive Search, worst case - O((m - n+ 1) * m)
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == "" and needle == "":
            return 0
        if needle == "":
            return 0
        m, n = len(haystack), len(needle)
        for i in range(0, m - n + 1):
            j = 0
            while j < n:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == n:
                return i
        return -1

# Method 2 - KMP, it is tricky to understand the getNext functions
# Time complextity O(m + n)
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        i, j = 0, 0
        m, n = len(haystack), len(needle)
        nextIndex = self.getNext(needle)
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = nextIndex[j]
        if j == n:
            return i - j
        else:
            return -1

    def getNext(self, p):
        n = len(p)
        nextIndex = [0] * n
        nextIndex[0] = -1
        i, j = 0, -1
        while i < n - 1:
            if j == -1 or p[i] == p[j]:
                i += 1
                j += 1
                nextIndex[i] = j
            else:
                j = nextIndex[j]
        print(nextIndex)
        return nextIndex