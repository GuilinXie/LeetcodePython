# Method 1: AC
class Solution:
    def maxScore(self, P, k):
        su, mx, L = 0, 0, len(P)
        for i in range(k):
            su += P[i]
        mx = max(mx, su)
        for i in range(0, k):
            su -= P[k - i - 1]
            su += P[L - i - 1]
            mx = max(mx, su)
        return mx


# Method 2 - TLE 16/40
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        if len(cardPoints) <= 1 or len(cardPoints) < k:
            return
        cache = {}
        return self.getMaxScore(cardPoints, k, 0, len(cardPoints) - 1, cache)

    def getMaxScore(self, cardPoints, k, i, j, cache):
        if k == 0 or i > j:
            return 0
        if i <= j:
            left = self.getMaxScore(cardPoints, k - 1, i + 1, j, cache) + cardPoints[i]
            right = self.getMaxScore(cardPoints, k - 1, i, j - 1, cache) + cardPoints[j]
            ans = left if left > right else right
            cache[(i, j, k)] = ans
            return ans