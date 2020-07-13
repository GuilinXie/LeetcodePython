class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[len(nums) - 1]
        for i in range(0, len(nums) - 1):
            start = i + 1
            end = len(nums) - 1

            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s > target:
                    end -= 1
                    while end >= start and nums[end] == nums[end + 1]:
                        end -= 1
                else:
                    start += 1
                    while start <= end and nums[start] == nums[start - 1]:
                        start += 1

                if abs(s - target) < abs(closestSum - target):
                    closestSum = s
        return closestSum
