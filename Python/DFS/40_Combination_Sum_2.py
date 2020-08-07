# Time: beat 50%
# Space: beat 35%
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        self.dfs(candidates, [], target, res)
        return res
    
    def dfs(self, cands, path, target, res):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in range(len(cands)):
            if i != 0 and cands[i] == cands[i-1]:
                continue
            self.dfs(cands[i+1:], path + [cands[i]], target - cands[i], res)
