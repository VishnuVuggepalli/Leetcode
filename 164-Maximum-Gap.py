class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_diff = 0
        heapq.heapify(nums)

        while len(nums) > 1:
            cur = heapq.heappop(nums)
            max_diff = max(max_diff, nums[0] - cur)
        return max_diff