# 2nd version - AC
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return
        R, C = len(matrix), len(matrix[0])
        ans = [[0] * C for _ in range(R)]
        
        initial = [(i, j, 0) for i in range(R) for j in range(C) if matrix[i][j] == 0]
        dq = collections.deque(initial)
        seen = set((i, j) for i, j, dist in initial)
        
        while dq:
            i, j, dist = dq.popleft()
            ans[i][j] = dist
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for new_i, new_j in neighbors:
                if 0 <= new_i < R and 0 <= new_j < C and (new_i, new_j) not in seen:
                    dq.append((new_i, new_j, dist + 1))
                    seen.add((new_i, new_j))
        return ans


# original
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
