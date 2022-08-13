class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        queue = collections.deque([])
        n = len(graph)
        seen = set()
        
        for node in range(n):
            visited_states = 1 << node
            queue.append((node,visited_states))
            seen.add((node,visited_states))
        
        step = 0
        complete_state = (1 << n) - 1
        print(complete_state)
        while queue:
            for _ in range(len(queue)):
                cur,seen_states = queue.popleft()
                if seen_states == complete_state:
                    return step
                
                for nxt in graph[cur]:
                    new_states = seen_states | (1 << nxt)
                    if (nxt,new_states) not in seen:
                        seen.add((nxt,new_states))
                        queue.append((nxt,new_states))
            step +=1