class Solution:
    def twoSumLessThanK(self, A, K):
        A.sort()
        if len(A) <= 1:
            return -1
        i = 0
        j = len(A) - 1
        res = -1
        while i < j:
            s = A[i] + A[j]
            if s < K:
                if res < s:
                    res = s
                i += 1
            else:
                j -= 1
        return res