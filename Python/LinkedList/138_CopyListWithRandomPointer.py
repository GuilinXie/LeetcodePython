# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

# # Method 1 - Hashmap, dict, space complexity o(n)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        m, n = head, head
        dic = dict()
        # dic[None] = None
        while m:
            dic[m] = Node(m.val)
            m = m.next
        while n:
            new_node = dic[n]
            # if n.next == None or n.random == None
            # dic.get(None) return return None
            # or we can use init dic[None] = None to solve this
            new_node.next = dic.get(n.next)
            new_node.random = dic.get(n.random)
            # new_node.next = dic[n.next]
            # new_node.random = dic[n.random]
            n = n.next
       # return dic[head]
        return dic.get(head)
        

# Method 2 - Copy directly
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
            if node.next:
                node.next = node.next.next
            curr = curr.next
        return newHead
