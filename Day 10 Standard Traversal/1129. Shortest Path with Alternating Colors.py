class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for start, to in redEdges:
            graph[start].append((to, 1))
        for start, to in blueEdges:
            graph[start].append((to, -1))
        
        q = collections.deque([(0, 1), (0, -1)])
        res = [-1] * n
        res[0] = 0
        visited_edge = set()
        steps = 0
        while q:
            steps += 1
            size = len(q)
            for _ in range(size):
                node, color = q.popleft()
                for next_node, next_color in graph[node]:
                    if next_color == -color:
                        if res[next_node] == -1:
                            res[next_node] = steps
                        if (next_node, next_color) not in visited_edge:
                            visited_edge.add((next_node, next_color))
                            q.append((next_node, next_color))
        return res