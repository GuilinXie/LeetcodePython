import collections

class Solution:
    def balancedString(self, s):
        count = collections.Counter(s)
        res = len(s)
        n = len(s)
        i = 0
        for j, char in enumerate(s):
            count[char] -= 1
            while i < n and all(n / 4 >= count[c] for c in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.balancedString("WWEQERQWQWWRWWERQWEQ")
    print (res)