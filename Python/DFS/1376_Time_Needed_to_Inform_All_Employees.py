class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        if len(manager) <= 0 or len(informTime) <= 0:
            return
        graph = dict()
        for i in range(-1, n):
            graph[i] = []
        for i in range(0, len(manager)):
            graph[manager[i]].append(i)
        res = self.dfs(graph, informTime, headID)
        return res

    # Tree with weights
    def dfs(self, graph, informTime, node):
        if graph[node] == []:
            return 0
        res = 0
        for child in graph[node]:
            tmp_res = self.dfs(graph, informTime, child)
            if tmp_res > res:
                res = tmp_res
        return res + informTime[node]