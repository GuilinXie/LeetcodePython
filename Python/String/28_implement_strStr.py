class Solution:
    # Solution 1 - beat 70%
    def strStr(self, haystack, needle):
        return haystack.find(needle)
    
    # Solution 2 - beat 40%
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        for i in range(0, len(haystack) + 1):
            for j in range(0, len(needle) + 1):
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if haystack[i+j] != needle[j]:
                    break
        return -1
