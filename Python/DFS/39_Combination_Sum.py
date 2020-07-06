# Time: O(l^k)
# Where l is the length of the array, k is the length of the longest possible combination (namely target / minInArray).
# i.e. If the min value in array is 1, and target is 9, the longest length of possible combination is 9 (9/1)

# Space: Space: O(k)
# For storing the path, which could be k long at most.

# beat 40%
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
