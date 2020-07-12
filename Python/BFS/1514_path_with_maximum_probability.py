# BFS, weighted graph, search for maxPath
class Solution:
    def maxProbability(self, n: int, edges, succProb, start, end):

        graph = collections.defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        # this works as seen, and also keeps the previous maxProbs
        distance = [0.0] * n
        distance[start] = 1.0

        heap = []
        heapq.heappush(heap, (-1.0, start))

        while heap:
            p, node = heapq.heappop(heap)
            p = -p

            if node == end:
                return p

            for v, w in graph[node]:
                if distance[v] < p * w:
                    distance[v] = p * w
                    heapq.heappush(heap, (-p * w, v))

        return 0