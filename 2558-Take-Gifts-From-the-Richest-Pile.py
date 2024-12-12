import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            heapq.heappush(gifts,-math.floor(math.sqrt(-heapq.heappop(gifts))))
        return -sum(gifts)