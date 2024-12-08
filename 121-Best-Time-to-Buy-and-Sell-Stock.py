class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        low_buy = prices[0]
        for sell in range(len(prices)):
            low_buy = min(low_buy, prices[sell])
            profit = max(profit, prices[sell] - low_buy)
        return profit