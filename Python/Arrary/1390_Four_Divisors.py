import math


class Solution:
    def sumFourDivisors(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        ans = 0
        for num in nums:
            cand = self.checkSum(num)
            ans += cand
        return ans

    def checkSum(self, n):
        s = 1 + n
        cnt = 2
        end = int(math.sqrt(n) + 1)
        for i in range(2, end):
            if n % i == 0:
                if i * i < n:  # avoid cases like 4, with divisors 1,2,4, where 2 * 2 = 4
                    s += i
                    s += int(n / i)
                    cnt += 2
                if i * i == n:
                    cnt += 1  # If it is cases like 4
                if cnt > 4:
                    return 0
        if cnt == 4:
            return s
        return 0