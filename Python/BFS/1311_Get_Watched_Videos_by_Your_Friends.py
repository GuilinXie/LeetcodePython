# 2nd version - beat 80%
# more readability
from collections import Counter
class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, idx, level):
        if (len(watchedVideos) <= 0 or len(friends) <= 0 or idx < 0 or level < 0):
            return
        graph = {}
        for i in range(0, len(friends)):
            graph[i] = friends[i]
            
        dq = collections.deque([(idx, 0)])
        seen = set([idx])
        cand = []
        while dq:
            cur, dist = dq.popleft()
            if dist == level:

                cand.append(cur)
            neighbors = graph[cur]
            for nei in neighbors:
                if nei not in seen:
                    seen.add(nei)
                    dq.append((nei, dist + 1))
          
        watchedTotal = []
        for f in cand:
            watchedTotal += watchedVideos[f]
            
        count = Counter(watchedTotal)
        sortCount = sorted(count.items(), key=lambda item:(item[1],item[0]))
        ans = [k for k, v in sortCount]
        return ans

# original
# do not need level_num, instead using deque && popleft() to control the order
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
