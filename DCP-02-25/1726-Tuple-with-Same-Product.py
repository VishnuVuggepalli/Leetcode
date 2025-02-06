class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_count = {}
        tuples = 0
        N = len(nums)
        for i in range(N-1):
            for j in range(i+1,N):
                cur_prod = nums[i] * nums[j]
                if cur_prod in prod_count:
                    tuples += 8 * prod_count[cur_prod]
                    prod_count[cur_prod] += 1
                else:
                    prod_count[cur_prod] = 1
          
        return tuples