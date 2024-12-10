class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        prefix_sum =0
        for num in range(len(nums)):
            if nums_sum - prefix_sum - nums[num] == prefix_sum:
                return num
            prefix_sum += nums[num]
        return -1