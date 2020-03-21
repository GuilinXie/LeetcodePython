# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        if root == None:
            return
        res = []
        self.dfs(root, s, res, [])
        return res

    def dfs(self, root, s, res, tmp):
        if root == None:
            return
        if root.left == None and root.right == None and s == root.val:
            tmp += [root.val]
            res.append(tmp)
            tmp = []
        if root.left:
            self.dfs(root.left, s - root.val, res, tmp + [root.val])
        if root.right:
            self.dfs(root.right, s - root.val, res, tmp + [root.val])