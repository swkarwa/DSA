"""
    BFS : Breath first search alogrithm
    question : https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

"""
from typing import List
from collections import deque

class Solution:

    # Function to return a list containing the DFS traversal of the graph.

    def bfs(self, graph):
        vertices = len(graph)
        visited = [False]*vertices

        queue = deque()
        result = []
        queue.append(0)
        visited[0] = True

        while queue :
            node = queue.popleft()
            result.append(node)

            for nbr in graph[node]:
                if not visited[nbr]:
                    visited[nbr] = True
                    queue.appened(nbr)

        return result

graph = [[2, 3, 1], [0], [0, 4], [0], [2]]
s = Solution()
result = s.bfs(graph)
print(result)
