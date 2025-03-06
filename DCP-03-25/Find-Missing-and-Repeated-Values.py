class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # 1,3,2,2 - find missing value, find the duplicate
        R = C = len(grid[0])
        visited = set()
        removed = set(i for i in range(1, (R * R)+1))
        res = [0,0]

        for i in range(R):
            for j in range(C):
                if grid[i][j] in visited:
                    res[0] = grid[i][j]
                    continue
                if grid[i][j] not in visited:
                    visited.add(grid[i][j])
                if grid[i][j] in removed:
                    removed.remove(grid[i][j])
        res[1] = removed.pop()
        return res
                
