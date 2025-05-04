from collections import deque
from typing import List
class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, graph: List[List[int]]) -> bool:
        # code here
        in_degree = [0] * V
        q = deque()
        for v in range(V):
            for node in graph[v]:
                in_degree[node] += 1

        for node, degree in enumerate(in_degree):
            if (degree == 0):
                q.append(node)
        count = 0
        while (q):
            top = q.popleft()
            for nbr in graph[top]:
                in_degree[nbr] -= 1
                if (in_degree[nbr] == 0):
                    q.append(nbr)
                    count += 1
        if (count == V):
            return True
        return False

graph = [[1],[2],[3],[3]]
result = Solution().isCyclic(6 , graph)
print(result)