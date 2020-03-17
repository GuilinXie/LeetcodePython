class Solution(object):
    def maxPerformance(self, N, S, E, K):  # n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        people = list(zip(E, S))
        people.sort(reverse=True)
        pq = []  # heap, or use heap as priority queue
        pqsum = 0
        res = 0
        for e, s in people:
            pqsum += s
            heapq.heappush(pq, s)
            if len(pq) > K:
                pqsum -= heapq.heappop(pq)
            cand = pqsum * e
            if cand > res:
                res = cand
        return res % MOD
