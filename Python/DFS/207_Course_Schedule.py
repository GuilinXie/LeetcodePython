# Method 1 - dfs with cache to optimize time complexity
class Solution:
    def canFinish(self, n, edges):
        if len(edges) <= 0 or len(edges[0]) <= 0:
            return True
        graph = dict()
        for i in range(n):
            graph[i] = []
        for item in edges:
            graph[item[1]].append(item[0])
        cache = set()
        for parent in graph.keys():
            if parent in cache:
                continue
            seen = set()
            res = self.dfs(graph, parent, seen, cache)
            if not res:
                return False
            cache.add(parent)
        return True

    def dfs(self, graph, node, seen, cache):
        if node in seen:
            return False
        if node in cache:
            return True
        seen.add(node)
        for child in graph[node]:
            res = self.dfs(graph, child, seen, cache)
            if not res:
                return False
        seen.remove(node)
        cache.add(node)
        return True


# Method 2 - BFS - topological sort
class Solution:
    def canFinish(self, n, edges):
        # construct graph
        graph = {i: set() for i in range(n)}
        in_degrees = {i: 0 for i in range(n)}

        for edge in edges:
            graph[edge[1]].add(edge[0])
            in_degrees[edge[0]] += 1

        # init var
        q = collections.deque()
        visited = set()

        # find nodes whose in degree == 0
        for index, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(index)

        # loop all nodes whose in degree == 0
        while q:
            index = q.popleft()
            visited.add(index)
            for g in graph[index]:
                in_degrees[g] -= 1
                if in_degrees[g] == 0:
                    q.append(g)
        return len(visited) == n