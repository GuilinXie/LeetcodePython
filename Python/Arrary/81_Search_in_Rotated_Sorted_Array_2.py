class Solution:
    def search(self, A: List[int], target: int) -> bool:
        #   def search(self, A: List[int], target: int) -> int:
        lo, hi = 0, len(A) - 1
        if len(A) <= 0:
            return False
        while lo <= hi:
            mid = (lo + hi) // 2
            if A[mid] == target:
                return True

            # duplicate
            if A[lo] == A[mid] and A[hi] == A[mid]:
                lo += 1
                hi -= 1

            elif A[lo] <= A[mid]:
                if A[lo] <= target and target < A[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if A[mid] < target and target <= A[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False
