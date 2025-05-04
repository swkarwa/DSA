"""
    Question : https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
    Detect cycle in a undirected graph using BFS and DFS
"""
from typing import List
from collections import deque


class Solution:

    def detectCycle(self, V: int, edges: List[int]) -> bool:
        graph = [[] for _ in range()]
        visited = [False] * V;
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        for i in range(V):
            if not visited[i]:
                if self.dfs(graph, visited, i, -1):
                    return True
        return False

    def dfs(self, graph, visited, current, parent) -> bool:
        """ DFS approach """
        visited[current] = True
        for child in graph[current]:
            if not visited[child]:
                if self.dfs(graph, visited, child, current):
                    return True
            elif child != parent:
                return True
        return False

    def bfs(self, graph, visited, current, parent) -> bool:
        """ BFS approach """
        q = deque()
        q.append((current, parent))
        visited[current] = True
        while q:
            current, parent = q.popleft()
            for child in graph[current]:
                if not visited[child]:
                    visited[child] = True
                    q.append((child, current))
                elif child != parent:
                    return True
        return False


V = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
s = Solution()
result = s.detectCycle()
s.detectCycle()
