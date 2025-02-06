class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_count = {}
        max_set = set()
        N = len(nums)
        for i in range(N-1):
            for j in range(i+1,N):
                cur_prod = nums[i] * nums[j]
                if cur_prod not in prod_count:
                    prod_count[cur_prod] = 0
                prod_count[cur_prod] += 1
                if prod_count[cur_prod] > 1:
                    max_set.add(cur_prod)
        #         print(nums[i], nums[j])
        # print(prod_count)
        tuples = 0
        for i in max_set:
            tuples += (((prod_count[i] * (prod_count[i] -1)) // 2) * 8)
        

        return tuples