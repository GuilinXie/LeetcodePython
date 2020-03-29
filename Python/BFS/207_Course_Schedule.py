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


# Method 2 - BFS - AC - beat 70%- topological sort
class Solution:
    def canFinish(self, n, edges):
        if len(edges) <= 0:
            return True
        
        graph = {}
        indegree = {}
        for i in range(n):
            graph[i] = []
            indegree[i] = 0
        for child, parent in edges:
            graph[parent].append(child)
            indegree[child] += 1
        
        # put all courses without pres in the queue first
        initial = [v for v in indegree if indegree[v] == 0]
        total = len(initial)
        dq = collections.deque(initial)
        seen = set(initial)
        
        while dq:
            node = dq.popleft()
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0 and child not in seen:
                    dq.append(child)
                    total += 1
                    # after visiting the child, then add it to seen
                    seen.add(child)
        if total == n:
            return True
        return False
