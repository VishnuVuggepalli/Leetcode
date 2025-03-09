class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        re_looped = colors[:k-1]
        rot_colors = colors + re_looped
        res = 0
        count = 2

        for i in range(1,len(rot_colors)-1):
            if rot_colors[i] == rot_colors[i-1] or rot_colors[i] == rot_colors[i+1]:
                count = 2
            else:
                count += 1
            if count >= k:
                res += 1

        return res