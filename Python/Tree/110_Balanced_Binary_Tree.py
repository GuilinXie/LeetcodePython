# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) <= 1:
            return self.isBalanced(root.left) \
                   and self.isBalanced(root.right)
        return False

    def height(self, root):
        if root == None:
            return 0
        left = 1 + self.height(root.left)
        right = 1 + self.height(root.right)
        if left > right:
            return left
        else:
            return right