class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]

        for start,end in intervals[1:]:
            if start > res[-1][1]:
                res.append([start,end])
            else:
                res[-1][1] = max(res[-1][1], end)
        return res
        # cur_min , cur_max = intervals[0][0], intervals[0][1]
        # res = []
        # for start,end in intervals[1:]:
        #     if cur_max < start:
        #         res.append([cur_min, cur_max])
        #         cur_min , cur_max = start, end
        #     else:
        #         cur_min = min (start, cur_min)
        #         cur_max = max (end, cur_max)
        
        # res.append([cur_min, cur_max])
        # return res
