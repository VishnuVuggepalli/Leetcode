class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit= 0
        for price in range(1,len(prices)):
            if prices[price-1] < prices[price]: 
                profit += prices[price]- prices[price -1]
        return profit