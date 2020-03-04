class Solution:
    # method 1 - use min-heap
    def findKthLargest(self, A: List[int], k: int) -> int:
        if len(A) < k:
            return
        h = [n for n in A[0:k]]
        heapq.heapify(h)
        for i in range(k, len(A)):
            if A[i] > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, A[i])
        return h[0]

    

    # method 2- slower than the above one
    # use quick-sort partition
    def findKthLargest(self, A, k):
        if A:
            pos = self.partition(A, 0, len(A) - 1)
            if k > pos + 1:
                return self.findKthLargest(A[pos + 1:], k - pos - 1)
            elif k < pos + 1:
                return self.findKthLargest(A[:pos], k)
            else:
                return A[pos]

    def partition(self, A, l, r):
        pivot = A[r]
        i = l - 1
        for j in range(l, r):
            # if A[j] <= A[r], then it's kth smallest
            # the following is kth largest
            if A[j] > A[r]:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1
