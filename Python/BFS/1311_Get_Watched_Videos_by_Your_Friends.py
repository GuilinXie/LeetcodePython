from collections import Counter
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        if (len(watchedVideos) <= 0 or len(friends) <= 0 or id < 0 or level < 0):
            return
        graph = {}
        for i in range(0, len(friends)):
            graph[i] = friends[i]
        q = [id]
        visited = [False] * len(friends)
        k = 0
        while k < level:
            levelnum = len(q)
            num = 0
            while num < levelnum:
                node = q.pop(0)
                num += 1
                visited[node] = True
                for nei in graph[node]:
                    if visited[nei] == False:
                        q.append(nei)
            k += 1
        watchedTotal = []
        for f in q:
            video = watchedVideos[f].copy()
            watchedTotal.extend(video)
        a = Counter(watchedTotal)
        b = sorted(a.items(),key=lambda item:(item[1],item[0]))
        res = []
        for k, v in b:
            res.append(k)
        return res