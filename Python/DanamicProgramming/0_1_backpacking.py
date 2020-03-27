
# Method 1 - Recursize
# i - the ith item operation, can add or not add
# j - leftover backpack space is j

def bagProblem(values, weights, i, j):
    maxValue = 0
    if i == -1:
        return 0
    # if there is enough leftover space j in backpack for item i
    if j >= weight[i]:
        value1 = bagProblem(values, weights, i - 1, j - weights[i]) + values[i]
        value2 = bagProblem(values, weights, i - 1, j)
        maxValue = max(value1, value2)
    return maxValue


# Method 2 - Recursive + cache
# cache can be used for stroing local variables
def bagProblem(values, weights, i, j, cache):
    maxValue = 0
    if i == -1:
        return 0
    if cache[i][j] > 0:
        return cache[i][j]

    if j >= weights[i]:
        value1 = bagProblem(i - 1, j - weights[i]) + values[i]
        value2 = bagProblem(i - 1, j)
        maxValue = max(value1, value2)
    cache[i][j] = maxValue
    return maxValue


