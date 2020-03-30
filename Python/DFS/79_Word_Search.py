# 2nd version, O(N * 4^L), where N = m * n of the grid, 4^L where L is the length of the word.
class Solution:
    # Method: dfs + backtracd, can fail for adding visit set, so just change grid directly
    # For backtracking, do not check nei before going into dfs
    # evey nei going into the dfs, then check the borders at the begining of the dfs
    def exist(self, grid: List[List[str]], word: str) -> bool:
        m = len(grid)
        n = len(grid[0])
        if m <= 0 or n <= 0:
            return False
        for i in range(m):
            for j in range(n):
                if grid[i][j] != word[0]:
                    continue
                res = self.search(grid, i, j, word)
                if res:
                    return res
        return False

    def search(self, grid, i, j, s):
        if not s:
            return True

        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == s[0]:
            tmp = grid[i][j]
            grid[i][j] = "#"
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for new_i, new_j in neighbors:
                r = self.search(grid, new_i, new_j, s[1:])
                if r:
                    return True
            grid[i][j] = tmp
        return False


# original - actually, do not need to add cache to pass, just change gird directly for backtrack, can save time
# Time complexity O(N * 4^L), where N = m * n of the grid, 4^L where L is the length of the word.
class Solution:
    # Method: DFS + cache, can fail for time complexity if no cache
    def exist(self, grid: List[List[str]], word: str) -> bool:
        m = len(grid)
        n = len(grid[0])
        if m <= 0 or n <= 0:
            return False
        cache = set()
        for i in range(m):
            for j in range(n):
                visited = set()
                res = self.search(grid, i, j, word, visited, cache)
                if res:
                    return res
                key = str(i) + "_" + str(j) + "_" + word
                cache.add(key)
        return False

    def search(self, grid, i, j, s, visited, cache):
        if not s:
            return True
        key = str(i) + "_" + str(j) + "_" + s
        if key in cache:
            return False
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in visited:
            visited.add((i, j))
            if grid[i][j] == s[0]:
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for new_i, new_j in neighbors:
                    r = self.search(grid, new_i, new_j, s[1:], visited, cache)
                    if r:
                        return True
                # It is not right to add cache.add(key) here, because backtrack from point A may use the different routes as from point B
            visited.remove((i, j))
        return False
