
# Method 1 - Traverse tree to get two lists, then find the intersection where they split.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # get two paths in list with node p and q
        p_path = self.getPath(root, p, [])
        q_path = self.getPath(root, q, [])

        # find intersection where two list split
        m, n = len(p_path), len(q_path)
        end = min(m, n)
        if end <= 0:
            return
        for i in range(end):
            if p_path[i] != q_path[i]:
                return p_path[i - 1]
        return p_path[end - 1]

    def getPath(self, root, node, tmp):
        if root == None:
            return
        if root == node:
            tmp = tmp + [root]
            return tmp
        tmp = tmp + [root]
        left = self.getPath(root.left, node, tmp)
        right = self.getPath(root.right, node, tmp)
        if left:
            return left
        if right:
            return right


# Method 2 - check where p, q locate in the tree
# It has three relative position, left + mid + right

class Solution:
    ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        global ans
        if root == None:
            return
        self.checkCount(root, p, q)
        return ans

    def checkCount(self, root, p, q):
        global ans
        if root == None:
            return False
        mid = 0
        if root == p or root == q:
            mid = 1
        left = 1 if self.checkCount(root.left, p, q) else 0
        right = 1 if self.checkCount(root.right, p, q) else 0
        total = mid + left + right
        if total >= 2:
            ans = root
        return True if total > 0 else False