# Time: beat 50%, O(n * 2^n ), for each element, you have 2 choice for picking or not picking, and slicing takes O(n)
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
