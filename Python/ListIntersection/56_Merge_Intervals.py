# Solution 1 - beat 70%
class Solution:
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        intervals.sort()
        ans = [intervals[0]]
        for cur in intervals[1:]:
            if cur[0] <= ans[-1][1]:
                ans[-1][1] = max(cur[1], ans[-1][1])
            else:
                ans.append(cur)
        return ans


# Solution 2
class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        res = []
        res.append(intervals[0])
        i = 0
        for j in range(1, len(intervals)):
            post = intervals[j]
            pre = res[i]
            ## Method1: delete one, add one
            # if pre[1] >= post[0]:
            #     start = pre[0]
            #     end = max(pre[1], post[1])
            #     res.remove(res[i])
            #     res.append([start, end])

            ## Method 2: update the last digit of res, direcly, optimization
            if pre[1] >= post[0]:
                res[-1][-1] = max(pre[1], post[1])
            else:
                res.append(post)
                i += 1
        #        intervals[0] = [0,0]
        return res
