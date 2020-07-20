class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        high = len(height) - 1
        low = 0
        while low != high:
            if height[low] < height[high]:
                area = height[low] * (high - low)
                low += 1
            else:
                area = height[high] * (high - low)
                high -= 1
            maxArea = max(area, maxArea)
        return maxArea