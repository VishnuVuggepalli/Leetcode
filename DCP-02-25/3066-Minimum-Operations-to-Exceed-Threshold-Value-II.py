class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        while len(nums) >= 2:
            small1 = heapq.heappop(nums)
            small2 = heapq.heappop(nums)
            if small1 >= k and small2 >= k:
                return count
            heapq.heappush(nums, (min(small1, small2) * 2) + max(small1, small2))
            count += 1
        return count