# base on twoSUm - beat 27%
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -num
            twoRes = self.find(nums, i + 1, len(nums) - 1, target)
            if twoRes:
                for cand in twoRes:
                    res.append([num] + cand)
        return res

    def find(self, nums, low, high, target):
        res = []
        while low < high:
            s = nums[low] + nums[high]
            if s == target:
                res.append([nums[low], nums[high]])
                low += 1
                high -= 1
                while low <= high and low and nums[low] == nums[low - 1]:
                    low += 1
                while high >= low and nums[high] == nums[high + 1]:
                    high -= 1
            elif s < target:
                low += 1
            else:
                high -= 1
        return res
    
    # solution 2 - one function - beat 19%
    class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return
        nums.sort()
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        res = []
        target = 0
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s > target:
                    end -= 1
                    while end >= start and nums[end] == nums[end + 1]:
                        end -= 1
                elif s < target:
                    start += 1
                    while start <= end and nums[start] == nums[start - 1]:
                        start += 1
                else:
                    res.append([nums[i], nums[start], nums[end]]) 
                    end -= 1
                    start += 1
                    while start <= end and nums[start] == nums[start - 1]:
                        start += 1
                    while end >= start and nums[end] == nums[end + 1]:
                        end -= 1
        return res
   
# Solution 3 - Recursive, - see 4Sum, beat 80%
