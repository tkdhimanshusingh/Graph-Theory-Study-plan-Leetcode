class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[math.inf if mat[i][j] != 0 else 0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = min(dp[i][j], 1 + dp[i - 1][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j - 1])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j])
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j + 1])

        return dp