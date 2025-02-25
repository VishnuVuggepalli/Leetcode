class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        # that guy's solution did not pass and no recursion as a topic , 
        # the answer might not be the one which he coded 

        l, r = 0, len(nums)-1

        while l < r:
            mid = l + (r-l) //2
            if nums[mid + 1] > nums[mid]:
                l = mid + 1
            else:
                r = mid
        return l