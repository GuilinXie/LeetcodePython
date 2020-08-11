class Solution:
    # Solution 1.0:
    # BFS - more neat code, beat 88%
    def jump(self, nums: List[int]) -> int:
        L, start, end, step = len(nums), 0, 0, 0
        while end < L - 1:
            step += 1
            maxend = end
            for i in range(start, maxend + 1):
                if i + nums[i] >= L - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step

class Solution:
    # solution 1 - bfs - beat 13%
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        furthest = 0
        curMax = 0
        level = 0
        i = 0
        while i <= curMax:
            while i <= curMax:
                furthest = max(furthest, i + nums[i])
                if furthest >= len(nums) - 1:
                    return level + 1
                i += 1
            level += 1
            curMax = furthest

    # solution 2 - passed 90/92, memory limit exceeded, too many cache
    def jump(self, nums):
        cache = dict()
        return self.dfs(nums, cache)

    def dfs(self, nums, cache):
        if len(nums) <= 1:
            return 0
        key = len(nums)
        if key in cache:
            return cache[key]
        # print(nums)
        steps = nums[0]
        res = sys.maxsize
        for i in range(1, steps + 1):
            cand = self.dfs(nums[i:], cache) + 1
            res = min(res, cand)
        cache[key] = res
        return res
