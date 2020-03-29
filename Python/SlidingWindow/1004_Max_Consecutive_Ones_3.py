class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        zeros = 0
        ans = 0
        for right in range(len(A)):
            if A[right] == 0:
                zeros += 1
            if zeros > K:
                while left < len(A) and A[left] != 0:
                    left += 1
                left += 1
                zeros -= 1
            ans = max(ans, right - left + 1)
        return ans