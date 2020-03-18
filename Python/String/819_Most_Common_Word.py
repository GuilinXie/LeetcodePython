class Solution:
    # Method 1: Counter, then most_common()[0][0]
    # It will sort and then get the max, a little bit overkill here
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = paragraph.lower()
        newData = list(filter(lambda x:len(x)>0, re.split(" |!|\?|\'|,|;|\.", para)))
        newDataFilter = []
        for data in newData:
            if data not in banned:
                newDataFilter.append(data)
        res = collections.Counter(newDataFilter).most_common()[0][0]
        return res

    # Method 2: Optimization
    # 1. Change all other punctuations to " ", then use split() to separate
    # 2. After Counter, iterate to get the max, avoiding sorting
    def mostCommonWord(self, paragraph: str, banned: List[str]):
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(word for word in paragraph.lower().split())
        print(count)
        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]
        return ans
