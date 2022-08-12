class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if (i==0 or j==0 or i==m-1 or j==n-1) and grid[i][j]==1:
                    self.dfs(grid,i,j,m,n,0)
					
        out = [] 
        
        for i in range(m):      
            for j in range(n):              
                if grid[i][j]==1:                  
                    count = self.dfs(grid,i,j,m,n,0)
                    out.append(count)
					
        if out:    
            return sum(out)
			
        return 0
                    
    def dfs(self,grid,i,j,m,n,count):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j]!=1:
            return count
        
        grid[i][j]=2
		
        count+=1
		
        count = self.dfs(grid,i+1,j,m,n,count)
        count = self.dfs(grid,i,j+1,m,n,count)
        count = self.dfs(grid,i-1,j,m,n,count)
        count = self.dfs(grid,i,j-1,m,n,count)
		
        return count