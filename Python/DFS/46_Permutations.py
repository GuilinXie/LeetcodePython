# Solution 1 -  dfs / backtracting - beat 48%
class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if nums == []:
            res.append(path)
        # dfs & backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


# Solution 2 - library - beat 90%
from itertools import permutations as P

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return P(nums)