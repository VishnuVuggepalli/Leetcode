class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        # +x,-x -x,+x
        max_points = 1
        for i,p1 in enumerate(points):
            line_map = defaultdict(int)
            x1,y1 = p1
            for j,p2 in enumerate(points[i+1:]):
                x2,y2 = p2
                if x1 - x2 == 0:
                    slope = inf
                else:
                    slope = (y1 -y2) / (x1 - x2)
                line_map[slope] += 1
                max_points = max(line_map[slope], max_points)
        return max_points+1