# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # solution 1 - recursive - beat 98%
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        h = ListNode(0)
        cur = h
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # Solution 2 - iterative - beat 20%
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        h = ListNode(0)
        cur = h

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2
        return h.next
