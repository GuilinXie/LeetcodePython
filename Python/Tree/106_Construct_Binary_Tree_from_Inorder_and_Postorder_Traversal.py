# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        m, n = len(inorder), len(postorder)
        if m <= 0 or n <= 0:
            return None

        root_val = postorder[-1]
        mid = inorder.index(root_val)

        root = ListNode(root_val)

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:n - 1])
        return root
