class Solution:
    def bfs(self, i, j, grid):
        R = len(grid)
        C = len(grid[0])
        directions = [-1,0,1,0,-1]
        q = [(i,j)]
        fish = grid[i][j]
        grid[i][j] =0
        while q:
            x,y = q.pop()
            for dir in range(4):
                nx = x + directions[dir]
                ny = y + directions[dir +1]

                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] > 0:
                    q.append((nx,ny))
                    fish += grid[nx][ny]
                    grid[nx][ny] = 0
        return fish


    def findMaxFish(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        maxFish = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] > 0:
                    maxFish = max(maxFish, self.bfs(i,j,grid))
        
        return maxFish