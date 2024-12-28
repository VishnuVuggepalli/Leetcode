class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # sliding window , prefix_sum
        window_sum = [sum(nums[:k])]
        for i in range(k, len(nums)):
            window_sum.append(window_sum[-1] + nums[i] - nums[i-k])
        
        dp ={} # for memoization -- cache
        def get_max(i , count):
            if (i,count) in dp:
                return dp[(i,count)]
            if count ==3 or i > len(nums) -k :
                return 0
            include = window_sum[i] + get_max(i+k, count +1)
            not_include = get_max(i +1, count)

            dp[(i,count)] = max(include,not_include)
            return dp[(i,count)]
        
        def get_indices():
            i =0
            indices =[]

            while i <= len(nums) -k and len(indices) < 3:
                include = window_sum[i] + get_max(i +k, len(indices) +1)
                not_include = get_max(i +1, len(indices))

                if include >= not_include:
                    indices.append(i)
                    i+=k
                else:
                    i += 1

            return indices
        return get_indices()