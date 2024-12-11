class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prefix_prod = 1
        left = 0
        count = 0
        for num in range(len(nums)):
            prefix_prod *= nums[num]
            while prefix_prod >= k:
                prefix_prod = prefix_prod/nums[left] 
                left += 1
            count += num - left +1
        return count
