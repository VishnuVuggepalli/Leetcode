class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low < high:
            mid = low + (high-low) // 2
            if nums[mid] == nums[mid-1]:
                if mid % 2:
                    low =mid +1
                else:
                    high = mid - 2
            elif nums[mid] == nums[mid+1]:
                if mid % 2:
                    high = mid - 1
                else:
                    low = mid + 2
            else:
                return nums[mid]
        return nums[low]
