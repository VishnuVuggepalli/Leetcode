import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = {}
        pq =[]
        for val in range(len(nums)):
            counted[nums[val]] = 1+ counted.get(nums[val],0)
        for key, val in counted.items():
            heapq.heappush(pq,(-val,key))
        res= []
        for count in range(k):
            res.append(heapq.heappop(pq)[1])
        return res
