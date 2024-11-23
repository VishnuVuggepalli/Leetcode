class Solution:         
    def sortArray(self, nums: List[int]) -> List[int]:
        def mainSort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2

            left = nums[:mid]
            right = nums[mid:]

            sortedLeft = mainSort(left)
            sortedRight = mainSort(right)

            return merge(sortedLeft, sortedRight)

        def merge(left,right):
            i = j = 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            res.extend(left[i:])
            res.extend(right[j:])

            return res

        return mainSort(nums)