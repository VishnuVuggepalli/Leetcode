class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # kadane's - local max and global max 
        local_max = 0
        res = 0
        local_min = 0

        for i in nums:
            local_max = max(local_max + i, 0)
            local_min = min(local_min + i, 0)

            res = max(res, local_max, -local_min)
        
        return res