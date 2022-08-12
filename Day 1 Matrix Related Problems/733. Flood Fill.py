class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        c=image[sr][sc]
        visited=[[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        def dfs(i,j):
            if i==len(image) or j==len(image[0]) or i<0 or j<0 or visited[i][j]!=0 or image[i][j]!=c:
                return
            visited[i][j]=1
            image[i][j]=color
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)
        dfs(sr,sc)
        return image