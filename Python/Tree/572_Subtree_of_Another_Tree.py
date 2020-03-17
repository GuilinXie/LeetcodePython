class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None and t == None:
            return True
        if s == None:
            return False
        if t == None:
            return True
        if self.isSametree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSametree(self, s, t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        if s.val != t.val:
            return False
        else:
            return self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)