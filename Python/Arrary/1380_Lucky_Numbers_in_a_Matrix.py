class Solution:
    def luckyNumbers (self, grid: List[List[int]]) -> List[int]:
        if len(grid) <= 0 or len(grid[0]) <= 0:
            return
        dic = dict()
        for i, x in enumerate(grid):
            key = i
            value = (i, x.index(min(x)), min(x))
            dic[key] = value
        res = set()
        for key, value in dic.items():
            i_max = value[2]
            j = value[1]
            column_j = [row[j] for row in grid]
            j_max = max(column_j)
            if j_max == i_max:
                res.add(j_max)
        return res