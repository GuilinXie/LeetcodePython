class Solution:
    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, [], target, res)
        return res

    def dfs(self, cands, path, target, res):

        if target == 0:
            res.append(path)
            return
        elif target < 0:  # backtracking
            return

        for i in range(len(cands)):
            # cands[i:], use it instead of cands, to avoid dupicate results
            self.dfs(cands[i:], path + [cands[i]], target - cands[i], res)