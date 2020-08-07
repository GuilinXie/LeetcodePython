class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        n = len(A)
        for i in range(n):
            while A[i] > 0 and A[i] <= n and A[A[i] - 1] != A[i]:
                # use the following to swap is not correct, as A[i] changes during the processing
                # A[i], A[A[i] - 1] = A[A[i] - 1], A[i]
                index = A[i] - 1
                temp = A[index]
                A[index] = A[i]
                A[i] = temp
                
        for i in range(n):
            if A[i] != i + 1:
                return i + 1
        return n + 1
