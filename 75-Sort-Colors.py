class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        count = [0]*3

        for num in nums:
            count[num] += 1
        
        val = 0
        for idx in range(len(nums)):
            while count[val] == 0:
                val += 1 
            nums[idx] = val
            count[val] -= 1