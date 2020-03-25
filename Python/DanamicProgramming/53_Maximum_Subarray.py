class Solution:
    # Method 1 - bf - TLE
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
        s = 0
        n = len(nums)
        res = -sys.maxsize
        for i in range(0, n):
            cand = 0
            for j in range(i, n):
                cand += nums[j]
                res = max(res, cand)
        return res

    # Method 2 - dp - store the max sum ending with i
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1, n):
            dp[i] = nums[i] if dp[i - 1] < 0 else nums[i] + dp[i - 1]
            ans = max(ans, dp[i])
        return ans