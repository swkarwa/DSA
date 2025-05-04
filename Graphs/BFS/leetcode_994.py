from collections import deque
from typing import List


class current_orange:

    def __init__(self, r, c, time):
        self.r = r
        self.c = c
        self.time = time


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        visited = [[0 for c in grid] for row in grid]

        q = deque()
        total_fresh_oranges = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] == 2):
                    orange = current_orange(r, c, 0)
                    q.append(orange)
                if (grid[r][c] == 1):
                    total_fresh_oranges += 1
                    visited[r][c] = 1

        max_time = self.bfs(grid, q, visited)
        current_rotted_oranges = sum(row.count(2) for row in visited)
        if (current_rotted_oranges == total_fresh_oranges):
            return max_time
        return -1

    def bfs(self, basket, q, visited):
        max_time = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while (q):
            top = q.popleft()
            neighbors = []
            for nr, nc in directions:
                r, c = top.r, top.c
                r += nr
                c += nc
                if (r >= 0 and c >= 0 and r <= len(basket) - 1 and c <= len(basket[0]) - 1 and visited[r][c] == 1):
                    neighbors.append((r, c))
                    visited[r][c] = 2

            for r, c in neighbors:
                current_time = top.time + 1
                co = current_orange(r, c, current_time)
                q.append(co)
            max_time = max(max_time, current_time)
        return max_time

basket = [[2,1,1],[0,1,1],[1,0,1]]
result = Solution().orangesRotting(basket)
print(result)