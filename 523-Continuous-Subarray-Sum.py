class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_div_map = {0:-1}
        prefix =0
        for num in range(len(nums)):
            prefix += nums[num]
            temp_div = prefix % k
            if temp_div in prefix_div_map:
                if num - prefix_div_map[temp_div] >1 :
                    return True
            else:
                prefix_div_map[temp_div] = num

        return False
        