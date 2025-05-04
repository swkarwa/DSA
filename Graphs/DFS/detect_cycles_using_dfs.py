from typing import List


class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, v: int, adj: List[List[int]]) -> bool:
        visited = [False] * v
        # Code here
        for i in range(v):
            result = self.dfs(adj, visited, i, -1)
            if (result):
                return 1
        return 0

    def dfs(self, graph, visited, src, parent):
        visited[src] = True
        for nbr in graph[src]:
            if (not visited[nbr]):
                if self.dfs(graph, visited, nbr, src):
                    return True
            elif (nbr != parent):
                return True
        return False


result = Solution().isCycle(4, [[1, 2], [2, 3],[] ,[]])
print(result)
