# Solution 1 - beat 99%
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        
        a, b = a.zfill(n), b.zfill(n)
        
        ans = ""
        carry = 0
        for i in range(n - 1, -1, -1):
            int_a = int(a[i])
            int_b = int(b[i])
            s = int_a + int_b + carry
            digit = s % 2
            carry = s // 2
            ans = str(digit) + ans
        if carry:
            ans = "1" + ans
        return ans
            
# Solution 2 - bit manipulation
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y          # SUM result without carry
            carry = (x & y) << 1    # remaining carry result
            x, y = answer, carry
        return bin(x)[2:]
