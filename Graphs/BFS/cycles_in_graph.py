from collections import deque
from typing import List

class Pair:
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child


class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, v: int, adj: List[List[int]]) -> bool:
        visited = [False] * v
        p = Pair(-1, 0)
        for i in range(v):
            result = self.bfs(adj, visited, i)
            if (result): return 1
        return 0

    def bfs(self, adj, visited, start):
        q = deque()
        q.append(Pair(-1, start))

        while (q):
            top = q.popleft()
            parent = top.parent
            child = top.child
            if (not visited[child]):
                visited[child] = True
                for nbr in adj[child]:
                    if (visited[nbr] and nbr != parent):
                        return True
                    elif (not visited[nbr]):
                        q.append(Pair(child, nbr))
        return False