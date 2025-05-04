from typing import List
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)

        # Create a mapping for rows and columns to index stones
        row_map = {}
        col_map = {}

        for i, (x, y) in enumerate(stones):
            if x not in row_map:
                row_map[x] = i
            else:
                uf.union(i, row_map[x])  # Union the current stone with the first stone in this row

            if y not in col_map:
                col_map[y] = i
            else:
                uf.union(i, col_map[y])  # Union the current stone with the first stone in this column

        # Count unique roots (connected components)
        root_set = set(uf.find(i) for i in range(n))
        return n - len(root_set)  # Total stones - number of unique roots


# Example usage
solution = Solution()
stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
print(solution.removeStones(stones))  # Output: 5