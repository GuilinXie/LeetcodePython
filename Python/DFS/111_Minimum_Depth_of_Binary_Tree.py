# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        # to make sure the end node is leaf, one of the child node is null
        if root.left == None:
            return 1 + self.minDepth(root.right)
        if root.right == None:
            return 1 + self.minDepth(root.left)
        
        # both left and right child node are not null
        left = 1 + self.minDepth(root.left)
        right = 1 + self.minDepth(root.right)
        return min(left, right)
