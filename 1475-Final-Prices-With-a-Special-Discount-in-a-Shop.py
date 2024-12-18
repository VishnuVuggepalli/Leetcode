class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        '''
        1. for each i - check for the very next , first min number , and subreact and store 
        if no min found - continue
        '''

        ans = prices[:]

        mono_stack= []

        for i, price in enumerate(prices):
            while mono_stack and prices[mono_stack[-1]] >= price:
                ans[mono_stack.pop()] -= price
            mono_stack.append(i)
        return ans



        # for i in range(len(prices) -1):
        #     j = i +1
        #     for j in range(i+1,len(prices)):
        #         if prices[j] <= prices[i]:
        #             prices[i] -= prices[j]
        #             break
        # return prices
                

        # i = 0
        # j = i + 1
        # while i < len(prices)-1 and j < len(prices):
        #     if prices[j] <= prices[i]:
        #         prices[i] -= prices[j]
        #         i += 1
        #         j = i
        #     j += 1
        # return prices