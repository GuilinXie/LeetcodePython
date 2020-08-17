# Solution 1 - beat 80%
# bit manipulation
class Solution:
    def subsets(self, nums):
        res = []
        maxEnd = 1 << len(nums)
        for i in range(maxEnd):
            tmp = []
            for j in range(len(nums)):
                if i & (1 << j):
                    tmp.append(nums[j])
            res.append(tmp)
        return res
        
# Solution 2 - beat 70%
# DFS
class Solution:
    def subsets(self, nums):
        if not nums:
            return []
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, tmp, res):
        # no need for deep copy like: res.append([t for t in tmp]), as dfs has a new address of tmp
        res.append(tmp)  
        for i in range(len(nums)):
            self.dfs(nums[i+1:], tmp + [nums[i]], res)
