from collections import deque
class Solution:
    def bfs(self, v, adj):
        visited = [False] * v
        q = deque()
        q.append(0)
        result = []
        while (q):
            top = q.popleft()
            result.append(top)
            if (visited[top]):
                continue
            visited[top] = True
            for nbr in adj[top]:
                if (not visited[nbr]):
                    q.append(nbr)
        print(result)


v = 10
edges = [[0, 1],
         [0, 2],
         [0, 4],
         [0, 8],
         [1, 5],
         [1, 6],
         [1, 9],
         [2, 4],
         [3, 7],
         [3, 8],
         [5, 8],
         [6, 7],
         [6, 9]]
Solution().bfs(v, edges)
