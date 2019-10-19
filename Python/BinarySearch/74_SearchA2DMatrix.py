class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            rowRight = matrix[i][col - 1]
            if rowRight == target:
                return True
            elif rowRight < target:
                continue
            else:
                rowLeft = matrix[i][0]
                if rowLeft == target:
                    return True
                elif rowLeft > target:
                    return False
                else:
                    return self.binarySearch(matrix[i], target)

    def binarySearch(self, nums, target):
        if len(nums) <= 0:
            return False
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False