from typing import List


class Solution:
    def __init__(self):
        self.components = dict()

    def find(self, x, parent):
        if (parent[x] == x):
            return x
        parent[x] = self.find(parent[x], parent)
        return parent[x]

    def union(self, x, y, parent, rank):

        root_x = self.find(x, parent)
        root_y = self.find(y, parent)

        if (root_x != root_y):

            if (rank[root_x] > rank[root_y]):
                parent[root_y] = root_x

            elif (rank[root_y] > rank[root_x]):
                parent[root_x] = root_y

            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        parent = [node for node in range(n)]
        rank = [0] * n

        for edge in edges:
            x = edge[0]
            y = edge[1]
            root_x = self.find(x, parent)
            root_y = self.find(y, parent)
            if (root_x != root_y):
                self.union(x, y, parent, rank)

        for par in parent:
            self.components[par] = self.components.get(par, 0) + 1
        print(self.components)
        return 0


n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Solution().countPairs(n, edges)
