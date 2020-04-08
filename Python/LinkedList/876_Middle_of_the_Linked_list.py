# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Method 1 - O(N) - slow & fast points
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        # if head.next == None:
        #     return head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow


# Method 2 - O(N + 0.5N)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next

        mid = cnt // 2 + 1
        cur = head
        while mid > 0:
            mid -= 1
            if mid > 0:
                cur = cur.next
        return cur