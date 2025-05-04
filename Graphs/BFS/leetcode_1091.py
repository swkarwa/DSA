from collections import deque
from typing import List

class Pair:
    def __init__(self, r, c, level):
        self.r = r
        self.c = c
        self.level = level


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        q.append(Pair(0, 0, 1))
        min_distance = float('inf')
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        while (q):
            top = q.popleft()
            r = top.r
            c = top.c
            level = top.level
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == 1):
                    continue
                if (nr == len(grid) - 1 and nc == len(grid[0]) - 1):
                    min_distance = min(min_distance, level)
                q.append(Pair(nr, nc, level + 1))
                grid[nr][nc] = 1

        return min_distance+1

result = Solution().shortestPathBinaryMatrix([[0,1],[1,0]])
print(result)