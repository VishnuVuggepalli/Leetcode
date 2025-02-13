class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        nums = sorted(set(nums))
        max_diff =0
        for i in range(1, len(nums)):
            max_diff = max(nums[i] - nums[i-1], max_diff)
        return max_diff
        # max_diff = 0
        # heapq.heapify(nums)

        # while len(nums) > 1:
        #     cur = heapq.heappop(nums)
        #     max_diff = max(max_diff, nums[0] - cur)
        # return max_diff