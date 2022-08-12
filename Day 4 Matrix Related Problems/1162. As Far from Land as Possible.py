class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = collections.deque()
        d = 0
        
        if sum([sum(row) for row in grid]) == 0 or sum([sum(row) for row in grid]) == n*n:
            return -1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j, d))
                    
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y, d = q.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
                    grid[nx][ny] = 1
                    q.append((nx, ny, d+1))
    
        return d