
# For record- at this time, I do not know str.isalnum() function.
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not ('a' <= s[i] <= 'z' or '0' <= s[i] <= '9'):
                i += 1
            while i < j and not ('a' <= s[j] <= 'z' or '0' <= s[j] <= '9'):
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

# Using str.isalnum()
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

