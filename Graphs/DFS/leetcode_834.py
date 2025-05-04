from typing import List


class Solution:

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # prepare graph
        graph = [[] for _ in range(n)]
        visited = [False] * n
        for edge in edges:
            src, dest = edge
            graph[src].append(dest)
            graph[dest].append(src)

        self.result = [0] * n  # stores result
        self.children = [0] * n  # stores number of child nodes for each node
        self.count = 1

        self.result[0] = self.dfs_base(graph, 0, -1, 0)
        print(self.children)

    def dfs_base(self, graph, parent, prev_node, distance):
        total_count = 1
        sum = distance
        for child in graph[parent]:
            if child == prev_node:
                continue
            total_count += 1
            sum += self.dfs_base(graph, child, parent, distance + 1)
        self.children[parent] = total_count
        return sum


n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]

Solution().sumOfDistancesInTree(n , edges)

