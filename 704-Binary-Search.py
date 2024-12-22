class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low , high = 0 , len(nums)

        while low < high:
            mid = (low + high) //2

            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid
        if low > 0 and nums[low-1] == target:
            return low -1
        else:
            return -1
        #     if target < nums[mid]:
        #         high = mid-1
        #     elif target > nums[mid]:
        #         low = mid+1
        #     else:
        #         return mid
        # return -1