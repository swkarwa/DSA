from functools import reduce
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # prepare graph here
        graph = [[] for _ in range(n)]

        for edge in edges:
            if (edge):
                s, d = edge
                graph[s].append(d)
                graph[d].append(s)
        print("graph", graph)
        visited = [False] * n
        count = 0
        for i in range(len(graph)):
            if (not visited[i]):
                component = []
                self.dfs(graph, i, visited, component)
                total_vertices_in_component = len(component)
                total_edges = reduce(lambda acc, vertex: acc + len(graph[vertex]), component, 0)
                if(total_edges == total_vertices_in_component * (total_vertices_in_component-1)):
                    count+=1
        print(count)
        return count

    def dfs(self, graph, src, visited, current):

        visited[src] = True
        current.append(src)
        for nbr in graph[src]:
            if (not visited[nbr]):
                visited[nbr] = True
                self.dfs(graph, nbr, visited, current)


Solution().countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]])
