# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Method 1: O(n^2), as we need to find the left_max and right_min for each node
    #     def isValidBST(self, root: TreeNode) -> bool:
    #         if root == None:
    #             return True

    #         left_max = -sys.maxsize
    #         right_min = sys.maxsize

    #         left = root.left
    #         if left:
    #             while left.right != None:
    #                 left = left.right
    #             left_max = left.val

    #         right = root.right
    #         if right:
    #             while right.left != None:
    #                 right = right.left
    #             right_min = right.val

    #         if root.val <= left_max or root.val >= right_min:
    #             return False

    #         return self.isValidBST(root.left) and self.isValidBST(root.right)

    # Method 2: O(n), as we traverse each node once
    def isValidBST(self, root: TreeNode) -> bool:
        lower = -sys.maxsize
        upper = sys.maxsize
        return self.check(root, lower, upper)

    def check(self, node, lower, upper):
        if node == None:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        left = self.check(node.left, lower, val)
        right = self.check(node.right, val, upper)
        return left and right