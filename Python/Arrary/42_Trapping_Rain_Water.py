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
    # Time Complexity O(n)-beat 44%, Space Complexity O(n)-beat 50%
    # Can be further optimized, using less space, by computing leftMax on the fly.
    class Solution:
    def trap(self, height):
        if len(height) <= 0:
            return 0
        L = len(height)
        leftMax, rightMax = [0] * L, [0] * L
        
        leftMax[0] = height[0]
        rightMax[L - 1] = height[L - 1]

        for i in range(1, L):
            leftMax[i] = max(leftMax[i-1], height[i])
        for i in range(L - 2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        ans = 0
        for i, hei in enumerate(height):
            minH = min(leftMax[i], rightMax[i])
            ans += minH - height[i]

        return ans

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
