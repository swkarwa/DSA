# variation of Dijkstra's
import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for col in range(cols)] for row in range(rows)]

        heap = [(grid[0][0], 0, 0)]  # height , row , col
        heapq.heapify(heap)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        while heap:

            h, r, c = heapq.heappop(heap)
            ans = max(ans, h)  # calculate ans here

            visited[r][c] = True  # mark current cell as visited

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return ans

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and not visited[nr][nc]):
                    visited[nr][nc] = True
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))

        return ans
