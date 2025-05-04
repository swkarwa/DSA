"""
    DFS : depth first search alogrithm
    question : https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

"""
from typing import List


class Solution:

    # Function to return a list containing the DFS traversal of the graph.

    def dfs(self, graph):
        # code here

        visited = [False] * len(graph)
        return self.dfs_helper(graph, visited, 0, [])

    def dfs_helper(self, graph, visited, node, result):
        if visited[node]:
            return

        visited[node] = True
        result.append(node)
        for nbr in graph[node]:
            if not visited[nbr]:
                self.dfs_helper(graph, visited, nbr, result)
        return result


graph = [[2, 3, 1], [0], [0, 4], [0], [2]]
s = Solution()
result = s.dfs(graph)
print(result)
