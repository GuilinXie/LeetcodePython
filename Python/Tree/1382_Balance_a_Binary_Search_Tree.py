class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arrBST = self.inorderTraversal(root)
        return self.sortedArrayToBalancedBST(arrBST)

    def inorderTraversal(self, root):
        res = []
        if root:
            tmp_left = self.inorderTraversal(root.left)
            res += tmp_left
            res.append(root.val)
            tmp_right = self.inorderTraversal(root.right)
            res += tmp_right
        return res

    def sortedArrayToBalancedBST(self, arr):
        if not arr:
            return None

        mid = int((len(arr)) / 2)

        val = arr[mid]
        root = TreeNode(val)

        root.left = self.sortedArrayToBalancedBST(arr[:mid])
        root.right = self.sortedArrayToBalancedBST(arr[mid + 1:])
        return root

    # Method 2 - inorderTraversal, with a res input
    def inorderTraversal(self, root, res):
        if root:
            self.inorderTraversal(root.left, res)
            res.append(root.val)
            self.inorderTraversal(root.right, res)
        return res