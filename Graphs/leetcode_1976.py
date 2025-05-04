import heapq
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        # Prepare graph as adjacency list
        graph = [[] for _ in range(n)]
        for src, dest, wt in roads:
            graph[src].append((dest, wt))
            graph[dest].append((src, wt))

        # Dijkstra’s with path counting
        min_heap = [(0, 0)]  # (distance, node)
        dist = [float('inf')] * n
        dist[0] = 0
        path_count = [0] * n
        path_count[0] = 1

        while min_heap:
            distance, node = heapq.heappop(min_heap)

            # If a shorter path to the destination is already found, skip
            if distance > dist[node]:
                continue

            # Explore neighbors
            for neighbor, weight in graph[node]:
                new_distance = distance + weight

                # Found a shorter path to neighbor
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    path_count[neighbor] = path_count[node]
                    heapq.heappush(min_heap, (new_distance, neighbor))

                # Found another shortest path to neighbor
                elif new_distance == dist[neighbor]:
                    path_count[neighbor] = (path_count[neighbor] + path_count[node]) % MOD

        return path_count[n - 1]  # Total paths to reach node n-1
n = 7
edges = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
s = Solution().countPaths( n , edges)