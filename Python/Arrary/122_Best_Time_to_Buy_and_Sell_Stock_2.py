class Solution:

    # Method 1: similar to stock 1, keep min_price
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 0:
            return 0

        min_price = sys.maxsize
        res = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                res += prices[i] - min_price
                min_price = prices[i]
        return res

    # Method 2 - more straightforward, sum up directly
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 0:
            return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res   