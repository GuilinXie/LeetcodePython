class Solution:
    def findOrder(self, n, edges):
        if n <= 0:
            return []

        graph = dict()
        in_degree = dict()
        for i in range(n):
            graph[i] = []
            in_degree[i] = 0
        # If there is no prerequisite requirements, then return initial graph directly
        if len(edges) <= 0:
            return graph

        for u, v in edges:
            graph[v].append(u)
            in_degree[u] += 1
        q = collections.deque([u for u in in_degree if in_degree[u] == 0])

        res = []
        while q:
            node = q.popleft()
            res.append(node)
            neighbors = graph[node]
            for nei in neighbors:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return res if len(res) == n else []


