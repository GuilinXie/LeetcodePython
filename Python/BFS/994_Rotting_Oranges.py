# 2nd version - AC - beat 90%
class Solution:
    def orangesRotting(self, A):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(A) <= 0 or len(A[0]) <= 0:
            return 0
        R, C = len(A), len(A[0])
        
        initial = [(i, j, 0) for i in range(R) for j in range(C) if A[i][j] == 2]
        dq = collections.deque(initial)
        ans = 0
        while dq:
            i, j, time = dq.popleft()
            ans = time
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for new_i, new_j in neighbors:
                if 0 <= new_i < R and 0 <= new_j < C and A[new_i][new_j] == 1:
                    dq.append((new_i, new_j, time + 1))
                    A[new_i][new_j] = 2
                    
        for i in range(R):
            for j in range(C):
                if A[i][j] == 1:
                    return -1
        return ans



# original
class Solution:
    def orangesRotting(self, A):
        if len(A) <= 0 or len(A[0]) <= 0:
            return -1
        m, n = len(A), len(A[0])
        fresh_cnt = 0
        deque = collections.deque()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    fresh_cnt += 1
                if A[i][j] == 2:
                    deque.append(((i, j), 0))
        res = 0

        # remember to check this before while loop
        if fresh_cnt == 0:
            return 0

        while deque:
            level_num = len(deque)
            for l in range(level_num):
                (i, j), d = deque.popleft()
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for new_i, new_j in neighbors:
                    if 0 <= new_i < len(A) and 0 <= new_j < len(A[0]) \
                            and A[new_i][new_j] == 1:
                        A[new_i][new_j] = 2
                        fresh_cnt -= 1
                        deque.append(((new_i, new_j), d + 1))
            res += 1
        return res - 1 if fresh_cnt == 0 else -1
