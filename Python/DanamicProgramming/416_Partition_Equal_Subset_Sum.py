# Recursive + Cache, TLE, pass 53/105
# Add sum(nums) % 2 precheck, AC with 5%
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) <= 0:
            return False

        if sum(nums) % 2 != 0:
            return False

        capacity = sum(nums) // 2

        L = len(nums) - 1
        cache = dict()
        return self.bagProblem(nums, L, capacity, cache)

    def bagProblem(self, weights, i, j, cache):
        key = str(i) + "_" + str(j)
        if i == -1:
            cache[key] = False
            return False
        if j == 0:
            cache[key] = True
            return True
        if key in cache:
            return cache[key]

        if j >= weights[i]:
            res1 = self.bagProblem(weights, i - 1, j - weights[i], cache)
            res2 = self.bagProblem(weights, i - 1, j, cache)
            if res1 or res2:
                cache[key] = True
                return True
        cache[key] = False
        return False


# dp solution: AC beat 29.38%
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) <= 0:
            return False

        s = sum(nums)

        if s % 2 != 0:
            return False

        capacity = s // 2

        return self.bagProblem(nums, capacity)

    def bagProblem(self, weights, capacity):
        R = len(weights) + 1
        C = capacity + 1

        dp = [[False] * C for _ in range(R)]

        for i in range(0, R):
            dp[i][0] = True

        for i in range(1, R):
            for w in range(1, C):
                if w >= weights[i - 1]:
                    dp[i][w] = dp[i - 1][w] or dp[i - 1][w - weights[i - 1]]
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[R - 1][C - 1]












