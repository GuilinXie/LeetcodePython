class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 0:
            return 0

        n = len(A)
        ans = 1
        anchor = 0

        for i in range(1, n):
            c = self.cmp(A[i - 1], A[i])
            if c == 0:
                anchor = i
            elif i == n - 1 or c * self.cmp(A[i], A[i + 1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans

    def cmp(self, a, b):
        return (a > b) - (a < b)