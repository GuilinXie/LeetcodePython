# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return res

    def dfs(self, node):
        if node == None:
            return 0

        left_res = 0
        right_res = 0
        if node.left:
            left_res = self.dfs(node.left)
        if node.right:
            right_res = self.dfs(node.right)
        res = max(left_res, right_res)

        return res + 1