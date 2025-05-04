from typing import List


class Solution:
    def dfs(self, graph, node, count, visited):
        visited[node] = True
        for nbr in graph[node]:
            if (not visited[nbr]):
                count = 1 + self.dfs(graph, nbr, count, visited)
        return count

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        graph = [[] for node in range(n)]

        for edge in edges:
            src, dest = edge
            graph[src].append(dest)
            graph[dest].append(src)

        comp_counts = []
        for node in range(n):
            if (not visited[node]):
                count = self.dfs(graph, node, 0, visited)
                comp_counts.append(count)

        print(comp_counts)
        return 0


n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Solution().countPairs(n, edges)
