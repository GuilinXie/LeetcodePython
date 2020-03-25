# Method 1 - time complexity O(4^n), too much time, for M * N = 5 * 7
# It takes a few seconds to get the result.
# It gets all path from 4 directions, overkill
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        if len(A) <= 0 or len(A[0]) <= 0:
            return
        res = []
        self.dfs(A, 0, 0, res, [])
        ans = max([min(p) for p in res])
        return ans

    def dfs(self, A, i, j, res, tmp):
        R, C = len(A), len(A[0])
        if i == R - 1 and j == C - 1:
            tmp.append(A[i][j])
            res.append(tmp)
            return
        if 0 <= i < R and 0 <= j < C and A[i][j] != "#":
            record = A[i][j]
            A[i][j] = "#"
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for new_i, new_j in neighbors:
                self.dfs(A, new_i, new_j, res, tmp + [record])
            A[i][j] = record

# Method 2 - Optimized Solution - O(N * logN), where  N = m * n is the size of the matrix
class Solution:
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        R, C = len(A), len(A[0])
        if R <= 0 or C <= 0:
            return 0
        hq = [(-A[0][0], 0, 0)]
        seen = [[0] * C for _ in range(R)]
        while hq:
            cost, i, j = heapq.heappop(hq)
            if i == R - 1 and j == C - 1:
                return -cost
            # seen.add((i, j))  # Got TLE
            # seen[i][j] = 1
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for ni, nj in neighbors:
                # if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in seen:
                # seen.add((ni, nj))
                if 0 <= ni < R and 0 <= nj < C and seen[ni][nj] == 0:
                    seen[ni][nj] = 1     # If the neighbor has already been visited, then put it into seen can save time for priority queue
                    heapq.heappush(hq, (max(cost, -A[ni][nj]), ni, nj))

if __name__ == "__main__":
    s = Solution()
    A =[[1,0,1,1,1,0,0],[0,1,1,1,1,1,0],[1,0,1,1,1,1,0],[1,1,1,0,1,1,0],[1,0,1,1,0,1,0]]
#    A =[[1,0,1,1,1,0],[0,1,1,1,1,1],[1,0,1,1,1,1],[1,1,1,0,1,1],[1,0,1,1,0,1]]
    res = s.maximumMinimumPath(A)
    print(res)