# Solution 1 - beat 85%
# bit manipulation
class Solution:
    def subsetsWithDup(self, nums):
        res = []
        maxEnd = 1 << len(nums)
        nums.sort()
        for i in range(maxEnd):
            tmp = []
            dup = False
            for j in range(len(nums)):
                if i & (1 << j):
                    # If previous value in the array is same as this
                    # AND previous value is not part of this set then it is a dup
                    if j != 0 and nums[j] == nums[j-1] and (i & 1 << (j-1)) == 0:
                        dup = True
                        break
                    else:
                        tmp.append(nums[j])
            if not dup:
                res.append(tmp)
        return res
    
# Solution 2 - beat 80%
# DFS
class Solution:    
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        nums.sort()
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, tmp, res):
        res.append(tmp)
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], tmp + [nums[i]], res)
