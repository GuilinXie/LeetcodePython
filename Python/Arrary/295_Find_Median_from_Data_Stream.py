class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []
        self.l_len = 0
        self.r_len = 0

    def addNum(self, num: int) -> None:
        ''' left heap will be equal or 1 longer than right heap
            left heap -> max heap, need to store -val
            right heap -> min heap, default heapq
        '''
        if self.l_len == self.r_len:
            if self.left == []:
                 heapq.heappush(self.left, -num)
            else:
                min_right = self.right[0]
                if num > min_right:
                    val = heapq.heappop(self.right)
                    heapq.heappush(self.right, num)
                    heapq.heappush(self.left, -val)
                else:
                    heapq.heappush(self.left, -num)
            self.l_len += 1
        elif self.l_len > self.r_len:
            max_left = -self.left[0]
            if num >= max_left:
                heapq.heappush(self.right, num)
            else:
                val = -heapq.heappop(self.left)
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, val)
            self.r_len += 1

    def findMedian(self) -> float:
        if self.l_len > self.r_len:
            return -self.left[0]
        else:
            return 0.5 * (-self.left[0] + self.right[0])