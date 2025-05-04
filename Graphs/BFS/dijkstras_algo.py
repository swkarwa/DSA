import heapq
from typing import List


class Solution:
    def dijkstra(self, V: int, adj: List[List[List[int]]], S: int) -> List[int]:
        # Distance array to store the shortest distance from S to all nodes
        dist = [float('inf')] * V
        dist[S] = 0  # The distance to the source is 0

        # Min-heap to keep track of (distance, node)
        heap = [(0, S)]  # Start with the source node at distance 0

        while heap:
            current_dist, node = heapq.heappop(heap)

            # If the current distance is greater than the stored distance, skip this node
            if current_dist > dist[node]:
                continue

            # Traverse all neighbors of the current node
            for neighbor in adj[node]:
                nbr_node, weight = neighbor

                # Calculate the distance to the neighbor
                new_dist = current_dist + weight

                # If a shorter distance is found, update it
                if new_dist < dist[nbr_node]:
                    dist[nbr_node] = new_dist
                    heapq.heappush(heap, (new_dist, nbr_node))

        return dist  # Returns the shortest distance from S to all nodes

V = 3
graph = [[[1,1] , [2,6]] , [[2,3],[0,1]] , [[1,3],[0,6]]]
result = Solution().dijkstra(V , graph , 2)
print(result)
