class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_inc, max_dec = 1,1
        inc,dec = 1,1
        for i in range(1, len(nums)):
            if nums[i-1]< nums[i]:
                inc += 1
                dec = 1
            elif nums[i-1] > nums[i]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            max_inc = max(max_inc, inc)
            max_dec = max(max_dec, dec)
        return max(max_inc, max_dec)