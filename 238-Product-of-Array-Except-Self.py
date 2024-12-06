class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for l in range(1, len(nums)):
            ans[l] = ans[l-1] * nums [l-1]
        temp = nums[-1]
        for r in range(len(nums) -2, -1, -1):
            ans[r] *= temp
            temp *= nums[r]
        return ans