class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Q = deque()
        M, N = len(grid), len(grid[0])
        if M == 0:
            return -1
        fresh = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    Q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        rotten = 0
        while Q and fresh > 0:
            rotten += 1
            for _ in range(len(Q)):
                rottenx, rotteny = Q.popleft()
                
                for dirc in directions:
                    newx = rottenx + dirc[0]
                    newy = rotteny + dirc[1]

                    if newx < 0 or newy < 0 or newx >= M or newy >= N or grid[newx][newy] == 2 or grid[newx][newy] == 0:
                        continue
                    
                    Q.append([newx, newy])
                    grid[newx][newy] = 2
                    fresh -= 1
        return rotten if fresh == 0 else -1