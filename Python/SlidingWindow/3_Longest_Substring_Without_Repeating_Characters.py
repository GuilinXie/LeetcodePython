class Solution:

    # Method 1 - Traditional Sliding Window
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        res = 0
        i = j = 0
        while j < n:
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                res = max(res, j - i)
            else:
                seen.remove(s[i])
                i += 1
        return res

    # Method 2 - Use Hashtable to further optimize time complexity
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        dic = dict()
        i = -1
        for j in range(0, n):
            if s[j] in dic:
                i = max(i, dic[s[j]])
            res = max(res, j - i)
            dic[s[j]] = j
        return res

    # Method 2
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     res = 0
    #     start = 0
    #     dic = dict()
    #     for i in range(0, len(s)):
    #         if s[i] in dic and start <= dic[s[i]]:
    #             start = dic[s[i]] + 1
    #         else:
    #             res = max(res, i - start + 1)
    #         dic[s[i]] = i
    #     return res