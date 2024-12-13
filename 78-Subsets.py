class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(level, subset):
            if level == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[level])
            backtrack(level+1,subset)

            subset.pop()
            backtrack(level+1, subset)
        backtrack(0,[])

        return res