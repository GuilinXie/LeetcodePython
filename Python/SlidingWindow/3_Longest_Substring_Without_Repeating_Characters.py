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
    
    # Method 1 - for record
class Solution: 
    def lengthOfLongestSubstring(self, s):
        ans = 0
        i= 0
        seen = set()
        for j, c in enumerate(s):
                   
            while c in seen:         # first step, check starting pos, and to see if need to move forward
                seen.remove(s[i])
                i += 1
                
            ans = max(ans, j - i + 1)  # second step, update ans
            seen.add(c)       
        return ans
    

    # Method 2 - Use Hashtable to further optimize time complexity
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 0 :
            return 0
        
        seen = {}
        ans = 0
        start = -1
        for i , c in enumerate(s):
            if c in seen and seen[c] > start:
                start = seen[c]
            else:
                ans = max(ans, i - start)
            seen[c] = i         
        return ans
