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
            ch = s[j]
            if ch in dic and dic[ch] > i:
                i = dic[ch]
            if j - i > res:
                res = j - i
            dic[ch] = j
        return res

# Method 2 - more optimization implementation for methoed 2, using enumerate
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """        
        start = -1
        dic = dict()
        ans = 0
        for i, c in enumerate(s):
            if c in dic and dic[c] > start:
                start = dic[c]          
            if i - start > ans:  
                ans = i - start                 
            dic[c] = i
        return ans
