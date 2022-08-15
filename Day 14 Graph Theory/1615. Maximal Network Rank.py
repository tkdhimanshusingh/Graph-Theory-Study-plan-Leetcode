class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        count = [0] * n
        connected = [[False]*n for _ in range(n)]
        
        for i,j in roads:
            count[i] += 1
            count[j] += 1
            connected[i][j] = True
            connected[j][i] = True
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res,count[i] + count[j] -  (1 if connected[i][j] else 0))

        return res