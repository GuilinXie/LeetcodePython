#dfs + cache, beat 27%
class Solution:
    def __init__(self):
        self.cache = dict()

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if not self.isSafe(r, c, N):
            return 0.0
        if K == 0:
            return 1

        key = (r, c, K)
        if key in self.cache:
            return self.cache[key]

        dirs = {(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)}
        prob = 0.0
        for dr, dc in dirs:
            prob += 0.125 * self.knightProbability(N, K - 1, r + dr, c + dc)

        self.cache[key] = prob

        return prob

    def isSafe(self, r, c, N):
        return r >= 0 and c >= 0 and r < N and c < N