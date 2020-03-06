def numIslands(grid):
    if len(grid) <= 0 or len(grid[0]) <= 0:
        return 0
    r, c = len(grid), len(grid[0])
    visited = set()
    res = 0
    for i in range(r):
        for j in range(c):
            if (i, j) not in visited and grid[i][j] == "1":
                res += 1
                dfs(grid, i, j, visited)
    return res


def dfs(A, i, j, visited):
    if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) \
            or (i, j) in visited or A[i][j] == "0":
        return
    visited.add((i, j))
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for new_i, new_j in neighbors:
        dfs(A, new_i, new_j, visited)
        
# if A is too large, and we do not want to keep a visited set, and we can change A
# then we can change A[i][j] = "#", after visiting (i, j)
