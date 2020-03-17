class Solution(object):

    def __init__(self):
        self.cache = set()

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if len(s) <= 0:
            return True
        if s in self.cache:
            return False
        wordDict = set(wordDict)
        for i in range(0, len(s) + 1):
            if s[:i] in wordDict:
                res = self.wordBreak(s[i:], wordDict)
                if res:
                    return True
        self.cache.add(s)
        return False