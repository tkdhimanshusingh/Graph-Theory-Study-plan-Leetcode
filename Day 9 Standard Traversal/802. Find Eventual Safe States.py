class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out_degree = collections.defaultdict(int)
        in_nodes = collections.defaultdict(list) 
        queue = []
        ret = []
        for i in range(n):
            out_degree[i] = len(graph[i])
            if out_degree[i]==0:
                queue.append(i)
            for j in graph[i]:
                in_nodes[j].append(i)  
        while queue:
            term_node = queue.pop(0)
            ret.append(term_node)
            for in_node in in_nodes[term_node]:
                out_degree[in_node] -= 1
                if out_degree[in_node]==0:
                    queue.append(in_node)
        return sorted(ret)