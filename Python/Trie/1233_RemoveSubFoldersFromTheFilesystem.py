import collections

# Solution 1 - Trie
class Solution(object):
    def removeSubfolders(self, A):
        # Trie = lambda: collections.defaultdict(Trie)
        # trie = Trie()

        END = "#"
        trie = dict()
        rows = []
        for i, row in enumerate(A):
            row = row.split('/')
            row.pop(0)
            rows.append((row, i))
        rows.sort(key=lambda r: len(r[0]))

        ans = []

        for row, i in rows:
            flag = True
            cur = trie
            for x in row:
                if x not in cur:
                    cur[x] = dict()
                cur = cur[x]
                if END in cur:
                    flag = False   # it has the prefix
                    break
            if flag:
                cur[END] = "#"
                ans.append(A[i])
        return ans

# Solution 2: no Trie
# class Solution:
#     def removeSubfolders(self, folder: List[str]) -> List[str]:
#         folder.sort(key = lambda x: len(x))
#         d = set()
#         ans = list()
#         for f in folder:
#             path = f.split("/")
#             flag = True
#             for i in range(2, len(path)):
#                 cur = "/".join(path[:i])
#                 if cur in d:
#                     flag = False
#                     break
#             if flag:
#                 d.add(f)
#                 ans.append(f)
#         return ans

# Solution 3 - Standard buildTrie method

class Solution:
    
    def __init__(self):
        self.root = dict()
    
    def removeSubfolders(self, A: List[str]) -> List[str]:
        if len(A) <= 1:
            return A   
        rows = []
        for row in A:
            row = row.strip("/").split("/")
            rows.append(row)
        rows = sorted(rows, key=len)
        
        res = []
        self.buildTrie(rows, res)
        return ["/" + "/".join(row) for row in res]
    
    def buildTrie(self, folders, res):        
     
        for folder in folders:
            p = self.root
            for c in folder:
                if "#" in p:
                    break
                if c not in p:
                    p[c] = dict()         
                p = p[c]
            if "#" not in p: 
                p["#"] = "#"
                res.append(folder)
            

if __name__ == "__main__":
    s = Solution()
    res = s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])
    print (res)
