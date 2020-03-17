class Solution:
    # Method 1 - Brute Force Time complexity O(n^2), Space Complexity O(1)
    def trap(self, height: List[int]) -> int:

        length = len(height)
        if length <= 0:
            return 0

        res = 0
        for i in range(length):
            left_max = max(height[0:i + 1])
            right_max = max(height[i:])
            high = min(left_max, right_max)
            res += high - height[i]

        return res

    # Method 2 - Dynamic Programming, store left_max[i] and right_max[i]
    # Time Complexity O(n), Space Complexity O(n)
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length <= 0:
            return 0
        left_max = [0] * length
        right_max = [0] * length
        left_max[0] = height[0]
        end = length - 1
        right_max[end] = height[end]

        for i in range(1, length):
            left_max[i] = max(left_max[i - 1], height[i])

        for i in range(length - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        res = 0
        for i in range(1, length - 1):
            # res += max(0, min(left_max[i], right_max[i]) - height[i])
            min_max = min(left_max[i], right_max[i])
            hei = height[i]
            tmp_res = min_max - hei
            res += tmp_res
        return res

    # Method 3 - Stack, O(N), O(N)
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length <= 0:
            return 0
        stack = []
        res = 0
        for i in range(0, length):
            #            print(stack)
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                res += distance * bounded_height
            stack.append(i)
        return res