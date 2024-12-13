class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index, res):
            if index == len(nums):
                return res
            
            include_number = backtrack(index + 1, res ^ nums[index])
            exclude_number = backtrack(index + 1, res)
            return include_number + exclude_number        
        return backtrack(0, 0)