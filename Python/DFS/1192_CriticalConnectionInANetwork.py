from collections import defaultdict

from collections import defaultdict


class Solution(object):
    def criticalConnections(self, n, connections):
        """
        type n: int
        type connections: List[List[int]]
        """
        # build undirected graph
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        dfn = [None for _ in range(n)]
        low = [None for _ in range(n)]

        res = []
        self.cur = 0

        def dfs(node, parent):
            if dfn[node] is None:
                dfn[node] = self.cur
                low[node] = self.cur
                self.cur += 1
                for n in graph[node]:
                    if dfn[n] is None:
                        dfs(n, node)
                l = min([low[i] for i in graph[node] \
                         if i != parent] + [low[node]])
                low[node] = l

        dfs(0, None)
        for v in connections:
            if low[v[0]] > dfn[v[1]] or low[v[1]] > dfn[v[0]]:
                res.append(v)
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])
    print (res)