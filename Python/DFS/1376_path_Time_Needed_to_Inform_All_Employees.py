class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        if len(manager) <= 0 or len(informTime) <= 0:
            return
        graph = dict()
        for i in range(-1, n):
            graph[i] = []
        for i in range(0, len(manager)):
            graph[manager[i]].append(i)
        path = []
        res = self.dfs(graph, informTime, headID, path)
        for node in path:
            print( node )
            print(" ")
        return res, path

    # Tree with weights
    def dfs(self, graph, informTime, node, path):
        if graph[node] == []:
            path.append(node)
            return 0
        res = -1
        node_list = []
        for child in graph[node]:
            tmp_list = []
            tmp_res = self.dfs(graph, informTime, child, tmp_list)
            if tmp_res > res:
                res = tmp_res
                node_list = tmp_list
        path.append(node)
      #  path += [n for n in node_list]
        path += node_list
        return res + informTime[node]


if __name__ == "__main__":
    s = Solution()
    n = 8
    headID = 0
    manager = [-1,5,0,6,7,0,0,0]
    informTime = [89,0,0,0,0,523,241,519]
    res, path = s.numOfMinutes(n,headID,manager,informTime)
    print(path)