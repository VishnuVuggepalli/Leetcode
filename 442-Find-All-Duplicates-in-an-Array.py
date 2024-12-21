class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set()
        count_map ={}
        for i in nums:
            if i not in count_map:
                count_map[i] = 1
            else:
                res.add(i)
        return list(res)