# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# Method 1 - I first use this one, but need head.next = None to avoid cycle
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head.next
        while cur:
            n = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = n
        head.next = None
        return dummy.next

# Method 2 - remain pre, cur, n, totally 3 pointers
# pre = cur,  not pre = cur.next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        pre = None
        cur = head
        while cur:
            n = cur.next
            cur.next = pre
            pre = cur
            cur = n
        return pre