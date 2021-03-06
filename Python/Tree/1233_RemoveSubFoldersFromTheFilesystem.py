import collections


class Solution(object):
    def removeSubfolders(self, A):
        Trie = lambda: collections.defaultdict(Trie)

        END = 1
        trie = Trie()

        rows = []
        for i, row in enumerate(A):
            row = row.split('/')
            row.pop(0)
            rows.append((row, i))
        rows.sort(key=lambda r: len(r[0]))

        ans = []
        for row, i in rows:
            cur = trie
            for x in row:
                cur = cur[x]
                if END in cur:
                    break
            else:
                cur[END] = 1
                ans.append(A[i])
        return ans

# class Solution:
#     def removeSubfolders(self, folder):
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

if __name__ == "__main__":
    s = Solution()
    res = s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])
    print (res)