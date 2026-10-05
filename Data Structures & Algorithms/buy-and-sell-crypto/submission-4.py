class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0
        while sell < len(prices):
            net = prices[sell] - prices[buy]

            if prices[buy] > prices[sell]:
                buy = sell

            if net > profit:
                profit = net

            sell += 1

        return profit

        