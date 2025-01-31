class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        N = len(nums)
        if N <2:
            return N
        while j < N :
            while j < N and nums[i] == nums[j]:
                j += 1
            if j < N:
                nums[i+1] = nums[j]
                i += 1
                j += 1
        
        return i+1