from typing import List
import heapq


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        if (len(edges) == 0):
            return [-1]

        # prepare graph
        graph = [[] for _ in range(n + 1)]
        for edge in edges:
            src, dest, weight = edge
            graph[src].append([dest, weight])
            graph[dest].append([src, weight])

        # initialize dijkstra's variables
        distance = [float('inf')] * (n + 1)
        distance[1] = 0  # start distance is always 0
        parent = [-1] * (n + 1)  # store parent reference , to track path later

        # insert src node in heap with 0 distance
        heap = [(0, 1)]
        path = []

        while (heap):

            current_dist, current_node = heapq.heappop(heap)

            if (current_dist > distance[current_node]):
                continue

            for neighbor in graph[current_node]:
                nbr_node, nbr_distance = neighbor
                new_distance = current_dist + nbr_distance

                if (new_distance < distance[nbr_node]):
                    distance[nbr_node] = new_distance
                    parent[nbr_node] = current_node  # store path here
                    heapq.heappush(heap, (new_distance, nbr_node))

        if (distance[n] == float('inf')):
            return [-1]

        # find path
        current = n
        while (current != -1):
            path.insert(0, current)
            current = parent[current]
        return [distance[n]] + path


edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
result = Solution().shortestPath(5, 6, edges)
print(result)
