class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Questions:
            1. is lower bound - min of piles --> 11
                is higher bound - sum of piles --> sum(piles) ????
        '''
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            mid = (low + high) //2
            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)
            if hours > h:
                low = mid + 1
            else:
                ans = min(ans, mid)
                high = mid -1
        return ans