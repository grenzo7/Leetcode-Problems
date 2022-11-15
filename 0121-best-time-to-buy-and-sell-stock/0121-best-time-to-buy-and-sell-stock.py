class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0
        max_profit = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                sell += 1
            elif prices[sell] <= prices[buy]:
                buy = sell
                sell += 1
            max_profit = max(max_profit,profit)
        return max_profit