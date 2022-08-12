class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if grid[i][j] == 1:
                return True
            
            if i<=0 or j<=0 or i>=len(grid)-1 or j>= len(grid[0])-1:
                return False
            
            grid[i][j] = 1
            
            t1 = dfs(grid,i+1,j)
            t2 = dfs(grid,i-1,j)
            t3 = dfs(grid,i,j+1)
            t4 = dfs(grid,i,j-1)
            
            return t1 and t2 and t3 and t4
        
        count = 0
        for i in range(1,len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 0 and dfs(grid,i,j):
                    count += 1
        return count