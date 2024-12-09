class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''Classic Case of prefix sum 0 if you do not know prefix sum use cases it is hard to solve '''
        prefix_sum = 0
        count =0
        prefix_count_map = {0:1}

        for num in nums:
            prefix_sum += num

            if prefix_sum -k in prefix_count_map:
                count += prefix_count_map[ prefix_sum -k ]
            if prefix_sum in prefix_count_map:
                prefix_count_map[prefix_sum] += 1
            else:
                prefix_count_map[prefix_sum] = 1
        return count