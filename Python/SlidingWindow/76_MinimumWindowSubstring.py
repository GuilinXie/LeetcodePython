import collections
class Solution:
    def minWindow(self, s, t):
        need = collections.Counter(t)            #hash table to store char frequency
        missing = len(t)                         #total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):          #index j from 1
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:                     #match all chars
                while i < j and need[s[i]] < 0:  #remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                if end == 0 or j-i < end-start:  #update window
                    start, end = i, j

                need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
                missing += 1                     #we missed this first char, so add missing by 1
                i += 1                           #update i to start+1 for next window
        return s[start:end]

# Method 2 - for record, different boundry conditions, enumerate(s), j from 0 not from 1, so end = j + 1 
import collections
class Solution:
    def minWindow(self, s, t):
        need = collections.Counter(t)            #hash table to store char frequency
        missing = len(t)                         #total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s):    
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:                     #match all chars
                while i < j and need[s[i]] < 0:  #remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                if end == 0 or j-i+1 < end-start:  #update window
                    start, end = i, j + 1

                need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
                missing += 1                     #we missed this first char, so add missing by 1
                i += 1                           #update i to start+1 for next window
        return s[start:end]   
    
if __name__ == "__main__":
    s = Solution()
    res = s.minWindow("ABECBA", "ABC")
    print (res)
