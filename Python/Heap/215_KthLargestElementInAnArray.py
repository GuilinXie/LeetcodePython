import heapq

class Solution:
    def findKthLargest(self, nums, k):
        if len(nums) <= 0:
            return
        h = [i for i in nums[0:k]]
        heapq.heapify(h)
        for i in range(k, len(nums)):
            if nums[i] > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, nums[i])
        return h[0]