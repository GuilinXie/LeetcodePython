import collections

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

if __name__ == "__main__":
    s = Solution()
    res = s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])
    print (res)