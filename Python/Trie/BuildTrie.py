
import collections
from typing import Dict, Any

'''
reference: https://zhuanlan.zhihu.com/p/47220472
'''

class Solution():

    def __init__(self):
        self.trie = dict()

    def buildTrie(self, words):

        # trie = {}
        # Trie = lambda: collections.defaultdict(Trie)
        # trie = Trie()

        for word in words:
            # 请把这个t理解为指针，这个指针除了用来移动外，也用来建立新的字典。
            # please think this t as a pointer, t is used for moving and building the dict
            t = self.trie
            for c in word:
                if c not in t:
                    t[c] = dict()
                t = t[c]
            t["#"] = "#"
        return self.trie

    def search(self, word):
        t = self.trie
        for c in word:
            # 如果我们在本层发现了这个字母，那么，我们进入下一层
            # if find c in this level, then move t to the next level
            if c in t:
                # 关键点依然是把t理解成指针
                # understand t as a pointer is important
                t = t[c]
            else:
                return False
        # 当所有字母都检查完毕的时候，我们需要确定，这个被查询的序列到底是不是一个完整的单词
        # after checking all the characters, then check if this is a real word with "#" ending mark
        if "#" in t:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    res = s.buildTrie(['cat','category','tree','trace','top'])
    # print (res)
    # print (s.search("category"))
    # print (s.search("cata"))
    # print (s.search("tree"))