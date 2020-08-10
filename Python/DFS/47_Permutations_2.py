# beat 90%
# Time Complexity < O(n^2 * n!), from CCI-P52
class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, tmp, res):
        if not nums:
            res.append(tmp)
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], tmp + [nums[i]], res)
