# Method 1 - dfs with cache to optimize time complexity
class Solution:
    def canFinish(self, n, edges):
        if len(edges) <= 0 or len(edges[0]) <= 0:
            return True
        # construct graph
        graph = {i: [] for i in range(n)}
        for child, parent in edges:
            graph[parent].append(child)
            
        cache = set()
        for node in graph.keys():
            if node in cache:
                continue
            seen = set()
            res = self.dfs(graph, node, seen, cache)
            if not res:
                return False
            cache.add(node)
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


# Method 2 - BFS - AC - beat 70%- topological sort
# Method 2 - BFS - topological sort
class Solution:
    def canFinish(self, n, edges):
        if len(edges) <= 0:
            return True
        
        # graph = {}
        # indegree = {}
        # for i in range(n):
        #     graph[i] = []
        #     indegree[i] = 0

        # construct graph
        graph = {i: [] for i in range(n)}
        indegree = {i: 0 for i in range(n)}
        
        for child, parent in edges:
            graph[parent].append(child)
            indegree[child] += 1
        
        # put all courses without pres in the queue first
        initial = [v for v in indegree if indegree[v] == 0]
        total = len(initial)
        dq = collections.deque(initial)
        
        while dq:
            node = dq.popleft()
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    dq.append(child)
                    total += 1
        if total == n:
            return True
        return False
