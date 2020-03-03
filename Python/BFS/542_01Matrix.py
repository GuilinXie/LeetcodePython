import collections

class Solution:
    def updateMatrix(self, A):
        if len(A) <= 0 or len(A[0]) <= 0:
            return
        m, n = len(A), len(A[0])

        q = collections.deque([((r, c), 0)
                               for r in range(m)
                               for c in range(n)
                              if A[r][c] == 0])
        seen = {x for x, _ in q}
        result = [[0] * n for _ in range(m)]
        while q:
            (r, c), depth = q.popleft()
            result[r][c] = depth
            neighbor = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for nei in neighbor:
                if nei not in seen and 0 <= nei[0] < m and 0 <= nei[1] < n:
                        seen.add(nei)
                        q.append((nei, depth + 1))
        return result

if __name__ == "__main__":
    s = Solution()
    res = s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
    print (res)
