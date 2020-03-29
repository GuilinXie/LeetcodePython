# 2nd version - update seen for every neighbor before appending to queue, can be faster
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList.append(beginWord)
        
        def buildDict(wordSet):
            wordDict = {}
            for word in wordSet:
                for i in range(0, len(word)):
                    key = word[:i] + "_" + word[i+1:]
                    if key not in wordDict:
                        wordDict[key] = []
                    wordDict[key].append(word)
            return wordDict
        
        wordDict = buildDict(wordList)
        
        dq = collections.deque([(beginWord, 1)])
        seen = set([beginWord])
        while dq:
            word, dist = dq.popleft()
           # not fast if update seen here
           # seen.add(word)
            if word == endWord:
                return dist
            for i in range(0, len(word)):
                key = word[:i] +  "_" + word[i+1:]
                if key not in wordDict:
                    continue
                else:
                    for nei in wordDict[key]:
                        if nei not in seen:
                            dq.append((nei, dist + 1))
                            # update seen here for every neighbor, can be faster
                            seen.add(nei)
        return 0
       

# original
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        def construct_dict(word_list):
            d = dict()
            for word in word_list:
                for i in range(0, len(word)):
                    key = word[0:i] + "_" + word[i + 1:]
                    if key not in d:
                        d[key] = []
                    d[key].append(word)
            return d

        wordList.append(beginWord)
        d = construct_dict(wordList)
        q = collections.deque([(beginWord, 1)])
        seen = set()

        while q:
            word, step = q.popleft()
            seen.add(word)
            if word == endWord:
                return step
            for i in range(0, len(word)):
                key = word[0:i] + "_" + word[i + 1:]
                neighbors = d.get(key)
                for nei in neighbors:
                    if nei not in seen:
                        q.append((nei, step + 1))
        return 0
