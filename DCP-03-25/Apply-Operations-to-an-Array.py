class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i] != 0:
                res.append(nums[i])
        
        if nums[len(nums)-1]!= 0:
            res.append(nums[len(nums)-1])
        
        for i in range(len(res), len(nums)):
            res.append(0)
        
        return res

        