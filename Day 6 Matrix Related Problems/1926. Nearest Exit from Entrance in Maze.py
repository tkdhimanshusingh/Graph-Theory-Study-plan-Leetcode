class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = entrance
        rows, cols = len(maze), len(maze[0])
        q = deque()
        q.append((m, n, 0))
        visited = {}
        visited[(m, n)] = 1
        while q:
            x, y, s = q.popleft()
            if (x in (0, rows - 1) or y in (0, cols - 1)) and maze[x][y] == '.' and (x != m or y != n):
                return s
            for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                u, v = x + i, y + j
                if 0 <= u <= rows - 1 and 0 <= v <= cols - 1 and maze[u][v] == '.' and visited.get((u, v), 0) == 0:
                    q.append((u, v, s + 1))
                    visited[(u, v)] = 1
        return -1