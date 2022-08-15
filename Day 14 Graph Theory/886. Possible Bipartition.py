class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
            dis_graph = defaultdict(set)
            colors = [-1 for i in range(n+1)]

            for a, b in dislikes:
                dis_graph[a].add(b)
                dis_graph[b].add(a)

            visited = set()

            for i in range(1, n+1):
                queue = deque([(i, 1)])

                while queue:
                    curr_node, curr_color = queue.popleft()

                    if colors[curr_node] == -1:
                        colors[curr_node] = curr_color

                    visited.add(curr_node)

                    for nei in dis_graph[curr_node]:
                        if colors[nei] == -1:
                            queue.append((nei, 1 - curr_color))
                        else:
                            if colors[curr_node] == colors[nei]:
                                return False

            return True