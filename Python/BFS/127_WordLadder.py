from collections import deque


# Solution 1: Optimize the neighbor words

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    key = word[:i] + "_" + word[i + 1:]
                    if key not in d:
                        d[key] = []
                    d[key].append(word)
            return d

        wordList.append(beginWord)
        d = construct_dict(set(wordList))
        # def neighbor(key):
        #     if key in d:
        #         return d[key]
        #     return []
        q = collections.deque([(beginWord, 1)])
        seen = set()
        while q:
            (word, steps) = q.popleft()
            if word not in seen:
                seen.add(word)
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    key = word[:i] + "_" + word[i + 1:]
                    neigh = d.get(key, [])
                    for nei in neigh:
                        if nei not in seen:
                            q.append((nei, steps + 1))
        return 0

# Solution 2: high time compexity - have not optimized the neighbor word
# from collections import deque

# class Solution(object):                
#     def ladderLength(self, beginWord, endWord, wordList):
#         if len(beginWord) <= 0 or len(endWord) <= 0 or len(wordList) <= 0:
#             return 0
#         wordList = set(wordList)
#         if endWord not in wordList:
#             return 0
#         seen = {beginWord}
#         q = collections.deque([(beginWord, 1)])
#         def neighbor(word):
#             for i in range(len(word)):
#                 for x in range(0, 26):
#                     w = list(word)
#                     c = chr(ord('a') + x)
#                     if w[i] != c:
#                         w[i] = c
#                         w = "".join(w)
#                         if w in wordList:
#                             yield w
#         while q:
#             (word, depth) = q.popleft()
#             if word == endWord:
#                 return depth
#             for nei in neighbor(word):
#                 if nei not in seen:
#                     seen.add(nei)
#                     q.append((nei, depth + 1))
#         return 0

# #     def ladderLength(self, beginWord, endWord, wordList):
# #         if len(beginWord) <= 0 or len(endWord) <= 0 or len(wordList) <= 0:
# #             return 0
# #         wordList = set(wordList)
# #         seen = {beginWord}
# #         q = collections.deque([beginWord])

# #         def neighbor(word):
# #             for i in range(len(word)):
# #                 for x in range(0, 26):
# #                     w = list(word)
# #                     c = chr(ord('a') + x)
# #                     if w[i] != c:
# #                         w[i] = c
# #                         w = "".join(w)
# #                         if w in wordList:
# #                             yield w

# #         ans = 0
# #         while q:
# #             levelnum = len(q)
# #             ans += 1
# #             for i in range(0, levelnum):
# #                 w = q.popleft()
# #                 if w == endWord:
# #                     return ans
# #                 for nei in neighbor(w):
# #                     if nei not in seen:
# #                         seen.add(nei)
# #                         q.append(nei)
# #         return 0
