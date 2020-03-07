class Solution:
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
        if m == 0:
            index = int(n / 2)
            return B[index] if n%2 == 1 else 0.5*(B[index]+B[index - 1])

        half_len = int((m + n + 1) / 2)

        # Check by traversing A from 0 to m
        i = 0
        while i <= m:
            j = half_len - i
            if i == 0 and B[j - 1] <= A[i]:
                if j == n:
                    min_right = A[i]
                else:
                    min_right = min(A[i], B[j])
                max_left = B[j - 1]
                break
            elif i == m and A[i - 1] <= B[j]:
                min_right = B[j]
                if j == 0:
                    max_left = A[i - 1]
                else:
                    max_left = max(A[i - 1], B[j - 1])
                break
            elif B[j - 1] <= A[i] and A[i - 1] <= B[j]:
                min_right = min(A[i], B[j])
                max_left = max(A[i - 1], B[j - 1])
                break
            i += 1
        if (m + n) % 2 == 1:
            return max_left
        else:
            return 0.5 * (max_left + min_right)