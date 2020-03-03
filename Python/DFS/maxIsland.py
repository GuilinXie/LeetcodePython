"""
Amazon Phone Interview
2020.03.02

o x x o x
x o o o x
x x x x x
x o o x x

o-> Island
x-> water

connected: vertically, horizontally, diagonally

eg: return 5

"""

def getMaxIsland(A):
    if len(A) <= 0 or len(A[0]) <= 0:
        return 0
    r, c = len(A), len(A[0])
    visited = set()
    res = 0
    for i in range(r):
        for j in range(c):
            if (i, j) not in visited:
                tmp_res = dfs(A, i, j, visited)
                if tmp_res > res:
                    res = tmp_res
    return res

def dfs(A, i, j, visited):
    if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or ((i, j) in visited) or A[i][j] != "o":
        return 0
    visited.add((i, j))
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1),\
                 (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1),\
                 (i + 1, j + 1)]
    # need to use size to store the sum of all neighbors
    # not return 1 + dfs(A, new_i, new_j, visited) directly
    size = 1
    for new_i, new_j in neighbors:
        size += dfs(A, new_i, new_j, visited)
    return size

if __name__ == "__main__":
    A = [["o", "x", "x","o", "x"],
        ["x", "o", "o","o", "x"],
        ["x", "x", "x","x", "x"],
        ["x", "o", "o","x", "x"]]
    r = getMaxIsland(A)
    print(r)
