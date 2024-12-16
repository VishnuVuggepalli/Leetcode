class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_count= {}
        calc_sum =0
        # def calc_pairs(val):
        #     if val == 0:
        #         return 0
        #     return val + calc_pairs(val-1)
        for width, height in rectangles:
            ratio = width/height
            if ratio in ratio_count:
                ratio_count[ratio] += 1
                calc_sum += ratio_count[ratio]
            else:
                ratio_count[ratio] = 0

        return calc_sum
