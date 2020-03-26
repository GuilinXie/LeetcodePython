class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = collections.Counter(tasks)

        hq = [-value for key, value in count.items()]
        heapq.heapify(hq)

        time = 0
        while hq:
            i = 0
            temp = []
            while i <= n:
                if hq:
                    top = heapq.heappop(hq)
                    # if top == -1, meaning it is the last one, no need to record
                    if top != -1:
                        temp.append(top + 1)
                time += 1
                if not hq and not temp:
                    break
                i += 1
            for t in temp:
                heapq.heappush(hq, t)
        return time