# Recursive - Beat 71%
# Beat 71%
class Solution:
    def fourSum(self, nums, target):
        results = []
        nums.sort()
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, res, results):
        if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
            return
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(res + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(nums) - N + 1):
                if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                    self.findNsum(nums[i + 1:], target - nums[i], N - 1, res + [nums[i]], results)

# Iterative based on threeSum - Beat 37%
class Solution:
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            tar = target - num
            threeRes = self.threeSum(nums[i + 1:], tar)
            if threeRes:
                for cand in threeRes:
                    res.append([num] + cand)
        return res

    def threeSum(self, nums, target):
        res = []
        #    nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            tar = target - num
            twoRes = self.find(nums, i + 1, len(nums) - 1, tar)
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