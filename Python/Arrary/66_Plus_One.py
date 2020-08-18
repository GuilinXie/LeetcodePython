# beat 80%
# add one. There could be no explicit carry.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        L = len(digits)
        
        for i in range(L-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            
        newDigits = [0] * (L + 1)
        newDigits[0] = 1
        return newDigits
