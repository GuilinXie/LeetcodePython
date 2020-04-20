# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1 - beat 75%, easier to find out with a helper buildBST function
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) <= 0:
            return None
        root = self.buildBST(nums, 0, len(nums) - 1)
        return root
    
    def buildBST(self, nums, low, high):
        if low > high:
            return None
        mid = (low + high + 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums, low, mid - 1)
        root.right = self.buildBST(nums, mid + 1, high)
        return root
    
    
# Solution 2 - hard to find out later
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) <= 0:
            return None
        mid = int(len(nums) / 2)
        val = nums[mid]
        root = TreeNode(val)
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
