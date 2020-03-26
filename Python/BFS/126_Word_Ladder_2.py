class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

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
        q = collections.deque([(beginWord, 1, [beginWord])])
        seen = set()
        ans = []
        shortest = sys.maxsize

        while q:
            word, step, tmp = q.popleft()
            seen.add(word)
            if word == endWord and step <= shortest:
                ans.append(tmp)
                shortest = step
                continue  # delete the continue if only need one path
            ## If only need to return 1 shortest path,
            ## then
            ## 1. add this break
            ## 2. delete the step variable
            ## 3. delete the shortest variable
            #        break
            for i in range(0, len(word)):
                key = word[0:i] + "_" + word[i + 1:]
                neighbors = d.get(key)
                for nei in neighbors:
                    if nei not in seen:
                        q.append((nei, step + 1, tmp + [nei]))
        return ans