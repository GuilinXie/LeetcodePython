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