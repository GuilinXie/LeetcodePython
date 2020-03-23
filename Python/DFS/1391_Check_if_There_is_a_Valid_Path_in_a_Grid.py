
# BFS
class Solution(object):
    def hasValidPath(self, A):
        R, C = len(A), len(A[0])

        NORTH = [-1, 0]
        SOUTH = [1, 0]
        WEST = [0, -1]
        EAST = [0, 1]
        neighbors = {
            1: [WEST, EAST],
            2: [NORTH, SOUTH],
            3: [WEST, SOUTH],
            4: [SOUTH, EAST],
            5: [WEST, NORTH],
            6: [NORTH, EAST]
        }

        queue = [(0, 0)]
        while queue:
            r, c = queue.pop()
            if r== R - 1 and c == C - 1:
                return True
            d = A[r][c]
            A[r][c] = -1
            for dr, dc in neighbors[d]:
                new_r = r + dr
                new_c = c + dc
                if not (0 <= new_r < R and 0 <= new_c < C):
                    continue
                if A[new_r][new_c] == -1:  # already visited
                    continue
                if [-dr, -dc] not in neighbors[A[new_r][new_c]]:  # required direction not exist
                    continue
                queue.append((new_r, new_c))
        return False


# DFS
class Solution(object):

    def __init__(self):
        self.NORTH = [-1, 0]
        self.SOUTH = [1, 0]
        self.WEST = [0, -1]
        self.EAST = [0, 1]
        self.neighbors = {
            1: [self.WEST, self.EAST],
            2: [self.NORTH, self.SOUTH],
            3: [self.WEST, self.SOUTH],
            4: [self.SOUTH, self.EAST],
            5: [self.WEST, self.NORTH],
            6: [self.NORTH, self.EAST]
        }

    def hasValidPath(self, A):
        if len(A) <= 0 or len(A[0]) <= 0:
            return False
        return self.dfs(A, 0, 0)

    def dfs(self, A, i, j):
        R, C = len(A), len(A[0])
        if i == R - 1 and j == C - 1:
            return True

        d = A[i][j]
        A[i][j] = -1
        for dr, dc in self.neighbors[d]:
            new_i = i + dr
            new_j = j + dc
            if not (0 <= new_i < R and 0 <= new_j < C):
                continue
            if A[new_i][new_j] == -1:
                continue
            if [-dr, -dc] not in self.neighbors[A[new_i][new_j]]:  # extra condition in this problem
                continue
            if self.dfs(A, new_i, new_j):
                return True
        return False


# Method 3 - Original AC code in weekly contest 181
class Solution:
    def __init__(self):
        self.dic = {
            1: ['', 'left', 'right'],
            2: ['', 'up', 'down'],
            3: ['', 'left', 'down'],
            4: ['', 'right', 'down'],
            5: ['', 'left', 'up'],
            6: ['', 'right', 'up']
        }

    def hasValidPath(self, grid):
        """
        type grid: List[List[int]]
        rtype: bool
        """
        # if len(grid) <= 0 or len(gird[0]) <= 0:
        #     return False
        return self.checkValidPath(grid, 0, 0, '') or self.checkValidPath(grid, 0, 0, '')

    def checkValidPath(self, grid, i, j, direction):
        row, col = len(grid), len(grid[0])

        if 0 <= i < row and 0 <= j < col and 0 < int(grid[i][j]) < 7 and (direction in self.dic[int(grid[i][j])]):
            if i == row - 1 and j == col - 1:
                return True
            record = grid[i][j]
            grid[i][j] = "-1"
            #     l_nei, r_nei, u_nei, d_nei = (i, j-1), (i, j+1), (i-1, j), (i, j+1)
            checkleft, checkright, checkup, checkdown = False, False, False, False
            if record == 1:
                checkleft = self.checkValidPath(grid, i, j - 1, 'right')
                checkright = self.checkValidPath(grid, i, j + 1, 'left')
            elif record == 2:
                checkup = self.checkValidPath(grid, i - 1, j, 'down')
                checkdown = self.checkValidPath(grid, i + 1, j, 'up')
            elif record == 3:
                checkup = self.checkValidPath(grid, i, j - 1, 'right')
                checkdown = self.checkValidPath(grid, i + 1, j, 'up')
            elif record == 4:
                checkup = self.checkValidPath(grid, i, j + 1, 'left')
                checkdown = self.checkValidPath(grid, i + 1, j, 'up')
            elif record == 5:
                checkup = self.checkValidPath(grid, i - 1, j, 'down')
                checkdown = self.checkValidPath(grid, i, j - 1, 'right')
            elif record == 6:
                checkup = self.checkValidPath(grid, i - 1, j, 'down')
                checkdown = self.checkValidPath(grid, i, j + 1, 'left')
            if checkleft or checkright or checkup or checkdown:
                return True
        #           grid[i][j] = record
        return False

if __name__ == "__main__":
   # A = [[4,3,1], [6,5,1], [1,1,1]]
    A = [[2,4,3],[6,5,2]]
    s = Solution()
    res = s.hasValidPath(A)
    print(res)