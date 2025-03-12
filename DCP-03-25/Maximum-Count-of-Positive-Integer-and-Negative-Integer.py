class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        low ,high = 0, len(nums)-1
        while low <= high:
            mid = low + (high -low) // 2
            if nums[mid] < 0:
                low = mid + 1
            else:
                high = mid -1 
        neg = high
        # print(low,high)
        low, high = 0 , len(nums)-1
        while low <= high:
            mid = low + (high - low ) // 2
            if nums[mid] > 0:
                high = mid - 1
            else:
                low = mid + 1
        # print(low, high)
        pos = len(nums) - low
        
        return max(neg + 1, pos) 