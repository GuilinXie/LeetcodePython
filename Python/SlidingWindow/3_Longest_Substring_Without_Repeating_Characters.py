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
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """        
        start = -1
        ans = 0
        seen = dict()
        for i, c in enumerate(s):
            if c in seen and seen[c] > start:
                start = seen[c]
            ans = max(ans, i - start)
            seen[c] = i
        return ans
