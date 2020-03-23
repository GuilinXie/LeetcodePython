class Solution:
    # Method 1 - Ok solution for record, but iterate too many times
    def closestDivisors(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dist = sys.maxsize
        cand1 = self.findMinDist(n + 1, dist)
        cand2 = self.findMinDist(n + 2, dist)
        if abs(cand1[0] - cand1[1]) < abs(cand2[0] - cand2[1]):
            return cand1
        else:
            return cand2

    def findMinDist(self, n, dist):
        end = int(math.sqrt(n) + 1)
        for i in range(1, end):
            if n % i == 0:
                d1 = i
                d2 = int(n / i)
                if abs(d1 - d2) < dist:
                    ans = [d1, d2]
        return ans

    # Method 2 - iterate from end sqrt(n) + 1, the first pair met must be the closest
    def closestDivisors(self, n):
        """
        :type num: int
        :rtype: List[int]
        """
        end = int(sqrt(n) + 1)
        for i in range(end, 0, -1):
            if (n + 1) % i == 0:
                return [i, int((n + 1) / i)]
            if (n + 2) % i == 0:
                return [i, int((n + 2) / i)]
        return []