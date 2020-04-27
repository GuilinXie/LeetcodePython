class Solution:
    def findDiagonalOrder(self, matrix):

        diags = collections.defaultdict(list)

        ans = []
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                diags[r + c].append(val)
        for k, v in diags.items():
            if k % 2 == 0:
                ans.extend(v[::-1])
            else:
                ans.extend(v)
        return ans