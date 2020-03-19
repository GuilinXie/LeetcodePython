class TrieNode():
    def __init__(self):
        self.children = dict()
        self.data = None
        self.isEnd = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def buildTrie(self, words):
        for word in words:
            p = self.root
            for c in word:
                if c not in p.children:
                    p.children[c] = TrieNode()
                p = p.children[c]
            p.isEnd = True
            p.data = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        if m <= 0 or n <= 0:
            return []

        self.buildTrie(words)

        res = set()
        for i in range(m):
            for j in range(n):
                p = self.root
                self.dfs(board, i, j, p, res)
        #          res.append(word)
        return res

    def dfs(self, board, i, j, p, res):
        if p:
            if p.isEnd == True:
                res.add(p.data)
            # It is not right to return here, because there are other words
            m, n = len(board), len(board[0])
            if 0 <= i < m and 0 <= j < n and board[i][j] in p.children:
                c = board[i][j]
                record = board[i][j]
                board[i][j] = "*"
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for new_i, new_j in neighbors:
                    self.dfs(board, new_i, new_j, p.children[c], res)
                board[i][j] = record
        return 