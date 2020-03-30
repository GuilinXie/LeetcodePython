# 2nd version - AC - beat 30%
# hot using positive number, and order two items accordingly
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0 

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self._addRecord(sentence, times[i])
            
    def _addRecord(self, sentence, hot):
        p = self.root
        for c in sentence:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isEnd = True
        p.rank += hot
        p.data = sentence
    
    def _search(self, keyword):
        p = self.root
        for c in keyword:
            if c not in p.children:
                return []
            p = p.children[c]
        return self._dfs(p)
    
    def _dfs(self, root):
        res = []
        if root:
            if root.isEnd:
                res.append((root.rank, root.data))
            for child in root.children:
                res.extend(self._dfs(root.children[child]))   
        return res
                
    
    def input(self, c: str) -> List[str]:
        res = []
        if c != "#":
            self.keyword += c
            res = self._search(self.keyword)
        else:
            self._addRecord(self.keyword, 1)
            self.keyword = ""
        res = sorted(res, key=lambda item:(-item[0], item[1]))
        return [item[1] for item in res[:3]]


# original - hot using negative number
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self._addRecord(sentence, times[i])

    def _addRecord(self, sentence, hot):
        p = self.root
        for c in sentence:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isEnd = True
        p.rank -= hot
        p.data = sentence

    def _search(self, keyword):
        p = self.root
        for c in keyword:
            if c not in p.children:
                return []
            p = p.children[c]
        return self._dfs(p)

    def _dfs(self, root):
        res = []
        if root:
            if root.isEnd:
                res.append((root.rank, root.data))
            for child in root.children:
                res.extend(self._dfs(root.children[child]))
        return res

    def input(self, c: str) -> List[str]:
        res = []
        if c != "#":
            self.keyword += c
            res = self._search(self.keyword)
        else:
            self._addRecord(self.keyword, 1)
            self.keyword = ""
        return [item[1] for item in sorted(res)[:3]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
