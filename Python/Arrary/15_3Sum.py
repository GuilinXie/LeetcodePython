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