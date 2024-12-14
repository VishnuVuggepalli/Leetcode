class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        left , right = 0 , len(nums)-1
        for num in range(len(nums)-1,-1,-1):
            if abs(nums[left]) < abs(nums[right]):
                res[num] = nums[right] * nums[right]
                right -= 1
            else:
                res[num] = nums[left] * nums[left]
                left += 1
        return res