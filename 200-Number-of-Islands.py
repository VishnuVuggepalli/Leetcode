class Solution:
    def dfs(self,row:int, col:int, grid:List[List[str]], ROW_SIZE:int, COL_SIZE: int):
        if row < 0 or row >= ROW_SIZE or col >= COL_SIZE or col < 0 or grid[row][col] != '1':
            return
        grid[row][col] = '2' 
        self.dfs(row+1, col, grid, ROW_SIZE, COL_SIZE)
        self.dfs(row-1, col, grid, ROW_SIZE, COL_SIZE)
        self.dfs(row, col+1, grid, ROW_SIZE, COL_SIZE)
        self.dfs(row, col-1, grid, ROW_SIZE, COL_SIZE)
        return
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW_SIZE = len(grid)
        COL_SIZE = len(grid[0])
        islands = 0
        for row in range(ROW_SIZE):
            for col in range(COL_SIZE):
                if grid[row][col] == '1':
                    self.dfs(row, col, grid, ROW_SIZE, COL_SIZE)
                    islands += 1
        return islands 