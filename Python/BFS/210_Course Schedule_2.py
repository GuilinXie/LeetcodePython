class Solution:
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 0:
            return []
        # construct graph
        graph = {i:[] for i in range(n)}
        indegree = {i:0 for i in range(n)}
            
        for child, parent in edges:
            graph[parent].append(child)
            indegree[child] += 1
            
        ans = [v for v in indegree if indegree[v] == 0]
        dq = collections.deque(ans)
        
        if len(edges) <= 0:
            return ans
        
        while dq:
            node = dq.popleft()
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    dq.append(child)
                    ans.append(child)
        if len(ans) == n:
            return ans
        else:
            return []
