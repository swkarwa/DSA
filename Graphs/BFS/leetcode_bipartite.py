from collections import deque
from typing import List
from collections import deque


class Pair:

    def __init__(self, node, level):
        self.node = node
        self.level = level


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False] * len(graph)
        color = [-1] * len(graph)
        for i in range(len(visited)):
            if (not visited[i]):
                if not self.check_bipartite(graph, i, visited, color):
                    return False
        return True

    def check_bipartite(self, graph, src, visited, color):

        q = deque()
        q.append(src)
        color[src] = 0
        while (q):

            node = q.popleft()

            if (visited[node]):
                continue
            visited[node] = True

            for nbr in graph[node]:

                if (color[nbr] == -1):
                    color[nbr] = 1 - color[node]
                    q.append(nbr)

                elif (color[nbr] == color[node]):
                    return False

        return True


Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]])
