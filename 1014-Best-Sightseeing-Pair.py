class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap =[]
        heapq.heapify(min_heap)
        for x,y in points:
            sqrt_val = (x ** 2) + (y ** 2)
            heapq.heappush(min_heap,(sqrt_val, [x,y]))
        res =[]
        for i in range(k):
            x,y = heapq.heappop(min_heap)
            res.append(y)
        return res