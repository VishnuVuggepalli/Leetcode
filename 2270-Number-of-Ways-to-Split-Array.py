class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = 0
        valid_splits = 0
        Sum = sum(nums)

        for i in range(0,N-1):
            prefix += nums[i]
            if prefix >= Sum - prefix:
                valid_splits += 1

        return valid_splits