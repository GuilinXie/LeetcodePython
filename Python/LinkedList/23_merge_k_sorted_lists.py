# Solution 1 - heapq as PriorityQueue - beat 40%
# Use cnt & ignoreValue, because heapq breaks as ListNode doesnot have __lt__ comparison function
class Solution:
    def mergeKLists(self, lists):
        h = cur = ListNode(0)
        pq = []
        cnt = 0
        for l in lists:
            if l:
                cnt += 1
                heapq.heappush(pq, (l.val, cnt, l))
        while pq:
            val, ignoreValue, node = heapq.heappop(pq)
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                cnt += 1
                heapq.heappush(pq, (node.val, cnt, node))
        return h.next


# solution 2 - divide and conquer - recursive - beat 20%
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        list1 = self.mergeKLists(lists[0:mid])
        list2 = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(list1, list2)

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