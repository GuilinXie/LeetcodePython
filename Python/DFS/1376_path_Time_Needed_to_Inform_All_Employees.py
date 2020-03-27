class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        if len(manager) <= 0:
            return 0
        if len(manager) != len(informTime):
            return -1
        graph = dict()
        for i in range(-1, n):
            graph[i] = []
        for i, m in enumerate(manager):
            graph[m].append(i)

        ans, path = self.dfs(graph, informTime, headID)
        print(path)
        return ans

    # dfs idea, iterate all neighbors, find the maxPath & maxCand, then add cur to the final result
    def dfs(self, graph, informTime, cur):

        maxCand = 0
        maxPath = []

        for nei in graph[cur]:
            cand, candpath = self.dfs(graph, informTime, nei)
            if cand >= maxCand:
                maxPath = candpath
                maxCand = cand

        maxPath.insert(0,cur)
        ans = informTime[cur]+maxCand

        return ans, maxPath


if __name__ == "__main__":
    s = Solution()
    n = 8
    headID = 0
    manager = [-1,5,0,6,7,0,0,0]
    informTime = [89,0,0,0,0,523,241,519]
    res, path = s.numOfMinutes(n,headID,manager,informTime)
    print(path)
