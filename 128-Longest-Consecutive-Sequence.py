class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        val_count_map = {}
        max_val = 0
        for num in nums:
            low = val_count_map.get(num-1,0)
            high = val_count_map.get(num+1,0)
            val = low+ high +1
            val_count_map[num - low] = val
            val_count_map[num + high] = val
            max_val = max(val, max_val)
        return max_val