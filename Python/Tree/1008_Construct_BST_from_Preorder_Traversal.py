# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) <= 0:
            return
        root = self.buildBFS(preorder)
        return root

    def buildBFS(self, nums):
        if len(nums) <= 0:
            return None
        rootVal = nums[0]
        root = TreeNode(rootVal)
        rootLeft = [n for n in nums if n < rootVal]
        rootRight = [n for n in nums if n > rootVal]
        root.left = self.buildBFS(rootLeft)
        root.right = self.buildBFS(rootRight)
        return root