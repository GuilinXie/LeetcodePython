# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1 - Using DFS - preOrder to serialize and deserialize
# But the problem is that it returns tuple for the serialize function, should return str
class Codec:
    def serialize(self, root):
        if not root:
            return 'x'
        return root.val, self.serialize(root.left), self.serialize(root.right)

    def deserialize(self, data):
        if data[0] == 'x':
            return None
        node = TreeNode(data[0])
        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])
        return node


# Method 1 - Update, change serialize return to str
class Codec:
    def serialize(self, root):
        if not root:
            return 'x'
        mid = str(root.val)
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return mid + " " + left + " " + right

    def deserialize(self, data):
        if len(data) <= 0:
            return None
        data = data.split()
        root = deserializeDfs(data)  # pass data as list address to the dfs, then data.pop() will always keep the change
        return root

    def deserializeDfs(data):
        if data[0] == "x":
            data.pop(0)
            return None
        root = TreeNode(data[0])
        data.pop(0)
        root.left = deserializeDfs(data)
        root.right = deserializeDfs(data)
        return root


# Method 2 - Using BFS - level order to serialize and deserialize
from collections import deque
class Codec:

    def serialize(self, root):
        string = ""
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if not cur:
                string += ",None"
                continue
            else:
                string += "," + str(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
        return string

    def deserialize(self, data):
        data = deque(data.split(","))
        _, val = data.popleft(), data.popleft()
        root = None if val == "None" else TreeNode(int(val))
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if cur:
                a, b = data.popleft(), data.popleft()
                cur.left = TreeNode(int(a)) if a != "None" else None
                cur.right = TreeNode(int(b)) if b != "None" else None
                queue.append(cur.left)
                queue.append(cur.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))