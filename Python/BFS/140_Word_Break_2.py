# DFS - AC with cache, TLE without cache, slower than BFS, but easy to explain and understand
class Solution:
     def wordBreak(self, s, wordDict):
        cache = dict()
        return self.dfs(s, wordDict, cache)
        
     def dfs(self, s, wordDict, cache):
        
        if s in cache:
            return cache[s]
        
        res = []
        
        if not s:
            res.append("")
            return res
        
        for end in range(1, len(s) + 1):
            if s[0:end] in wordDict:
                tmp = self.dfs(s[end:], wordDict, cache)
                for word in tmp:
                    space = "" if word == "" else " "
                    res.append(s[0:end] + space + word)
                    
        cache[s] = res
        return res



# BFS
class Solution:
     def wordBreak(self, s, wordDict):
            q = collections.deque()
            visited = [0] * (len(s) + 1)
            q.append((0,[]))
            res = []
            tmp_res = ""
            while q:
                start = q.popleft()
                if visited[start] == 0:
                    for end in range(start + 1, len(s) + 1):
                        if s[start:end] in wordDict:
                            q.append(end)
                            tmp_res += " " + s[start:end]
                            if end == len(s):
                                res.append(tmp_res)
                                tmp_res = ""
                    visited[start] = 1
            return res
