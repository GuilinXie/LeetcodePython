"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
#Solution 1: O(n), O(1)
# reference: https://zhuanlan.zhihu.com/p/38888164
class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        # copy every node, link them to a linked list
        curr = head
        while curr:
            node = Node(curr.val, None, None)
            node.next = curr.next
            curr.next = node
            curr = curr.next.next
        # copy the random pointer
        curr = head
        while curr:
            node = curr.next
            if curr.random is None:
                node.random = curr.random
            else:
                node.random = curr.random.next
            curr = curr.next.next
        # split the copy link
        curr = head
        newHead = head.next
        while curr:
            node = curr.next
            curr.next = node.next
            if node.next is None:
                node.next = None
            else:
                node.next = node.next.next
            curr = curr.next
        return newHead

#Solution 2: O(n), O(n)
# class Solution:
#     def copyRandomList(self, head):
#         dic = dict()
#         m = n = head
#         while m:
#             dic[m] = Node(m.val, None, None)
#             m = m.next
#         while n:
#             dic[n].next = dic.get(n.next)
#             dic[n].random = dic.get(n.random)
#             n = n.next
#         return dic.get(head)