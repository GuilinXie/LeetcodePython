class Solution:
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        if len(sticks) <= 1:
            return 0
        hp = sticks
        heapq.heapify(hp)
        cost = 0
        while len(hp) != 1:
            minVal = heapq.heappop(hp)
            minVal2 = heapq.heappop(hp)
            cost += minVal + minVal2
            newVal = minVal + minVal2
            heapq.heappush(hp, newVal)
        return cost