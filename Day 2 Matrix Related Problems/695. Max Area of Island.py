class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def dfs(i,j,s):
            if i<0 or j<0 or i==len(grid) or j==len(grid[0]) or visited[i][j]==1 or grid[i][j]==0:
                return 0
            visited[i][j]=1
            return(1+dfs(i,j+1,s)+dfs(i,j-1,s)+dfs(i+1,j,s)+dfs(i-1,j,s))
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]==0 and grid[i][j]==1:
                    ans=max(dfs(i,j,0),ans)
        return ans