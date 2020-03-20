# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Method 1 - Recursive dfs
    def hasPathSum(self, root: TreeNode, s: int) -> bool:
        if not root:
            return False
        if root.left == None and root.right == None and s == root.val:
            return True
        return self.hasPathSum(root.left, s - root.val) or \
               self.hasPathSum(root.right, s - root.val)

    # Method 2 - Iterative - dfs
    def hasPathSum(self, root, s):
        if not root:
            return False
        stack = [(root, s - root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                if val == 0:
                    return True
            if curr.right:
                stack.append((curr.right, val - curr.right.val))
            if curr.left:
                stack.append((curr.left, val - curr.left.val))
        return False

    # Method 3 - Iterative bfs
    def hasPathSum(self, root, s):
        if root == None:
            return False
        if root.left == None and root.right == None:
            if s == root.val:
                return True
        q = [(root, s)]
        while q:
            node, val = q.pop(0)
            if node.left == None and node.right == None:
                if val == node.val:
                    return True
            if node.left:
                q.append((node.left, val - node.val))
            if node.right:
                q.append((node.right, val - node.val))
        return False