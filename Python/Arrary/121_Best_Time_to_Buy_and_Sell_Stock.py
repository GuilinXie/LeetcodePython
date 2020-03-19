class Solution:

    # Method 1 : BF, O(n*2), O(1)
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 0:
            return 0
        res = 0
        for i in range(0, len(prices)):
            max_right = max(prices[i:])
            profit = max_right - prices[i]
            if profit > res:
                res = profit
        return res

    # Method 2: dp, similar to trapping rain water right side, O(n), O(n)
    def maxProfit(self, prices):
        if len(prices) <= 0:
            return 0
        n = len(prices)
        max_right = [0] * n
        max_right[n - 1] = prices[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], prices[i])

        res = 0
        for i in range(0, len(prices)):
            profit = max_right[i] - prices[i]
            if profit > res:
                res = profit
        return res

    # Method 3: best one, O(n), O(1)
    def maxProfit(self, prices):
        if len(prices) <= 0:
            return 0
        min_price = sys.maxsize
        max_profit = 0
        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit