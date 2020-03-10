# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.post = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.post = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.tail.prev
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.post
        p.post = n
        n.prev = p

    def _add(self, node):
        p = self.head.post
        self.head.post = node
        node.prev = self.head
        node.post = p
        p.prev = node