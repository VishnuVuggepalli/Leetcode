class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # check out of bounds 
        N = len(grid)

        def out_of_bounds(r, c):
            return (r<0 or c<0 or r ==N or c == N)

        def dfs(r,c,label):
            if (out_of_bounds(r,c) or grid[r][c] != 1):
                return 0
            grid[r][c] = label
            size = 1
            neigh = [[r,c-1],[r+1,c],[r-1,c],[r,c+1]]
            for nr,nc in neigh:
                size += dfs(nr,nc, label)
            return size

        def connect(r,c):
            visit = set()
            res = 1
            neigh = [[r,c-1],[r+1,c],[r-1,c],[r,c+1]]
            for nr, nc in neigh:
                if not out_of_bounds(nr,nc) and grid[nr][nc] not in visit:
                    res += cur_area[grid[nr][nc]]
                    visit.add(grid[nr][nc])
            return res


        # preprocess per each area
        label = 2
        cur_area = defaultdict(int)
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    cur_area[label] = dfs(r,c,label)
                    label += 1
        
        # step 2 : take water and connect disjoint labels
        res = 0 if not cur_area else max(cur_area.values())
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    res = max(res, connect(r,c))
        return res

