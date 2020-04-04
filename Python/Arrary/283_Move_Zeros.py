class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]
        """
        L = len(nums)
        if L <= 0:
            return
        i = 0
        for j in range(0, L):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1