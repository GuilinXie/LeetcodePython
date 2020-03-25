# Method 1 - sort, O(N * logN)
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cnt = collections.Counter(words)
        sortCnt = sorted(cnt.items(), key=lambda item:(-item[1], item[0]))
        res = sortCnt[0:k]
        return [r[0] for r in res]

# Method 2 - optimized, using heap, count O(N), heap to get topK, O(N * logk)
# To be implement