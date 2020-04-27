class Solution(object):
    def findDiagonalOrder(self, A):
        diags = collections.defaultdict(list)
        ans = []
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                diags[r + c].append(val)

        for k, v in diags.items():
            ans.extend(v[::-1])
        return ans