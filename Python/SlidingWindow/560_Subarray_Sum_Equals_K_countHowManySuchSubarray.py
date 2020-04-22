class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) <= 0:
            return

        dic = {0: 1}
        s = 0
        ans = 0
        for n in nums:
            s += n
            if s - k in dic:
                ans += dic[s - k]
            if s not in dic:
                dic[s] = 0
            dic[s] += 1
        return ans