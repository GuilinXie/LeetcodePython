class Solution:
    # solution 1, O(n), beat 50%
    def canJump(self, A):
        furthest = 0
        for i in range(0, len(A)):
            if furthest < i:
                return False
            furthest = max(furthest, i + A[i])
        return True

    # solution 2, TLE, only passed 73/75
    def canJump(self, nums: List[int]) -> bool:
        cache = dict()
        return self.dfs(nums, cache)

    def dfs(self, nums, cache):
        if len(nums) <= 1:
            return True
        key = len(nums)
        if key in cache:
            return cache[key]
        steps = nums[0]
        for i in range(1, steps + 1):
            res = self.dfs(nums[i:], cache)
            if res:
                cache[key] = True
                return True
        cache[key] = False
        return False

