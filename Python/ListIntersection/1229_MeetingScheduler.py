# SOLUTION 1: Two Pointers, Average Time Complexity O(n)
class Solution:

    def minAvailableDuration(self, slots1, slots2, duration):
        i, j = 0, 0
        n1 = len(slots1)
        n2 = len(slots2)
        # res = []
        slots1.sort()
        slots2.sort()
        while i < n1 and j < n2:
            maxStart = max(slots1[i][0], slots2[j][0])
            minEnd = min(slots1[i][1], slots2[j][1])
            if minEnd - maxStart >= duration:
                return [maxStart, maxStart + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []

    # SOLUTION 2: sort - Time Complexity nlog(n)
    # def minAvailableDuration(self, slots1, slots2, duration):
    #     if len(slots1) <= 0 or len(slots2) <= 0:
    #         return []
    #     OPEN = 1
    #     CLOSE = 0
    #     events = []
    #     for a, b in slots1:
    #         events.append((a, OPEN))
    #         events.append((b, CLOSE))
    #     for a, b in slots2:
    #         events.append((a, OPEN))
    #         events.append((b, CLOSE))
    #     events.sort()
    #     active = 0
    #     prev = events[0][0]
    #     for x, cmd in events:
    #         if active == 2 and x - prev >= duration:
    #             return [prev, prev + duration]
    #         if cmd == OPEN:
    #             active += 1
    #         else:
    #             active -= 1
    #         prev = x
    #     return []