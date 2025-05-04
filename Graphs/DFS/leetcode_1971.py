from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = [[] for _ in range(n)]
        for edge in edges:
            s, d = edge
            graph[s].append([s, d])
            graph[d].append([d, s])

        for g in graph:
            print(g)
        return True

s = Solution()
s.validPath(3, [[0,1],[1,2],[2,0]] , 0 , 2)