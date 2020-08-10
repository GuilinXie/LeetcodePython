# beat 70%, time complexity: O(n * m * log(m)), m = max(len(word))
class Solution:
    def groupAnagrams(self, strs):
        dic = dict()
        for s in strs:
            key = tuple(sorted(s))
            if key not in dic:
                dic[key] = []
            dic[key].append(s)
        return dic.values()
