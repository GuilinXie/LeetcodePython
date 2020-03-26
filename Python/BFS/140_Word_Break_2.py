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