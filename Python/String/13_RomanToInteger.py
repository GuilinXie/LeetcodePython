class Solution:
    def romanToInt(self, s):
        if len(s) <= 0:
            return 0
        ans = 0
        if "IV" in s:
            ans -= 2
        if "IX" in s:
            ans -= 2
        if "XL" in s:
            ans -= 20
        if "XC" in s:
            ans -= 20
        if "CD" in s:
            ans -= 200
        if "CM" in s:
            ans -= 200
        for i in range(len(s)):
            if s[i] == "M":
                ans += 1000
            elif s[i] == "D":
                ans += 500
            elif s[i] == "C":
                ans += 100
            elif s[i] == "L":
                ans += 50
            elif s[i] == "X":
                ans += 10
            elif s[i] == "V":
                ans += 5
            elif s[i] == "I":
                ans += 1
        return ans