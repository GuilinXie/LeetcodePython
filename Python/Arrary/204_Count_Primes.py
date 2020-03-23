import math


class Solution:

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        # do not need to reset isPrime[0] = False or isPrime[1] = False
        # because we can skip these 2 cases in range(2, n)
        isPrime = [True] * n

        end = int(math.sqrt(n)) + 1
        for i in range(2, end):
            if isPrime[i] == False:
                continue
            for j in range(i * i, n, i):
                isPrime[j] = False

        ans = 0
        for i in range(2, n):
            if isPrime[i]:
                ans += 1
        return ans
