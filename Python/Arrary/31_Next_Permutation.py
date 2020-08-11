# 1. Find the largest index k such that nums[k] < nums[k + 1]. If no such index , just reverse
# 2. Find the largest index l > k such that nums[k] < nums[l]
# 3. Swap nums[k] and nums[l]
# 4. Reverse the sub-array nums[k + 1:]
    
# how to understand it:
# step-1: easy, find the first digit that can be swapped to make permutation bigger
# step-2: easy, find the digit bigger but closest to nums[k]
# step-3: swap(nums[k], nums[l])
# step-4: sort the subarray nums[k+1:end], why we can just reverse instead of sort?
# because we know nums[k+1:end] must be non-increasing, reason:
# 1. at step 1, we know nums[k+1:end] is non-decreasing
# 2. before swap in step 3, we know nums[l-1] >= nums[l] > nums[k] >= nums[l+1]
# 3. so after swap, we still have nums[l-1] > nums[k] >= nums[l+1], so we can reverse it

# beat 68%, time complexity O(N)
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
         
        L = len(nums)
        i, j = L - 1, L - 1
        
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        
        k = i - 1
        
        while nums[j] <= nums[k]:
            j -= 1
        
        nums[k], nums[j] = nums[j], nums[k]       
        low, high = k + 1, L - 1
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1     
