class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return 0
        TRANS = {0: -1, 1: 1}
        dic = {0: -1}
        curSum = 0
        ans = 0
        for i, num in enumerate(nums):
            num = TRANS[num]
            curSum += num
            if curSum in dic:
                j = dic[curSum]
                ans = max(ans, i - j)
            else:
                dic[curSum] = i
        return ans