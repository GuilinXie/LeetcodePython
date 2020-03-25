class Solution:
    # Method 1 - BF - TLE
    def subarraySum(self, nums, k):
        """
        type nums: List[int]
        type k: int
        rtype: int
        """
        n = len(nums)
        if n <= 0:
            return 0
        ans = 0
        for i in range(n):
            cand = 0
            for j in range(i, n):
                cand += nums[j]
                if cand == k:
                    ans += 1
        return ans

    # Method 2 - Optimized using dict to cache all the sum of subarray
    def subarraySum(self, nums, target):
        n = len(nums)
        if n <= 0:
            return 0
        cache = {0: 1}
        s = 0
        cnt = 0
        for i in range(n):
            s += nums[i]
            if s - target in cache:
                cnt += cache[s - target]
            # else:
            #     cache[s - k] = 0
            if s not in cache:
                cache[s] = 0
            cache[s] += 1
        return cnt