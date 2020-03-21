class Solution:
    def dailyTemperatures(self, T):
        '''
        :type T: List[int]
        :rtype: List[int]
        '''
        if len(T) <= 0:
            return
        n = len(T)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and T[i] > stack[-1][0]:
                t, index = stack.pop()
                ans[index] = i - index
            stack.append((T[i], i))
        return ans