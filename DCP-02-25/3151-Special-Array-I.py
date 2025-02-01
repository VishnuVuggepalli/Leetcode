class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 1:
            return True
        for i in range(1, N):
            if (nums[i-1] & 1) == (nums[i] & 1):
                return False
        return True