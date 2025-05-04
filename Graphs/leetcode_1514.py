import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:

        """
            prepare graph
        """
        graph = [[] for _ in range(n)]
        for i, (s, d) in enumerate(edges):
            graph[s].append((d, succProb[i]))
            graph[d].append((s, succProb[i]))

        heap = [(-1, start_node)]
        heapq.heapify(heap)

        probablity = [0] * n
        probablity[start_node] = 1

        while heap:

            current_probab, current_node = heapq.heappop(heap)
            current_probab = -current_probab

            if current_node == end_node:
                return current_probab

            for nbr, edge_probab in graph[current_node]:
                new_probab = current_probab * edge_probab
                if new_probab > probablity[nbr]:
                    probablity[nbr] = new_probab
                    heapq.heappush(heap, (-new_probab, nbr))

        return 0 if probablity[end_node] == 0 else probablity[end_node]


n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

Solution().maxProbability(n  , edges , succProb , start , end)