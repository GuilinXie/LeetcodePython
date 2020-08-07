# beat 50%
# time complexity: O(m+n), top1 vote solution in Discussion: https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        pos = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                
                s = mul + pos[p2]
                
                pos[p1] += s // 10
                pos[p2] = s % 10
            
        ans = ''.join([str(i) for i in pos])
        if ans.lstrip("0") != "":
            ans = ans.lstrip("0")
        else:
            ans = "0"
        return ans
