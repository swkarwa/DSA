from collections import deque

from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if (grid[0][0] == 1 or grid[-1][-1] == 1):
            return -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        q = deque()
        q.append((0, 0, 1))
        while (q):
            r, c, level = q.popleft()
            if (r == len(grid) - 1 and c == len(grid[0]) - 1):
                return level
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == 1):
                    continue
                if (grid[nr][nc] == 0):
                    q.append((nr, nc, level + 1))
        return -1
grid = [[0,1],[1,0]]
ans = Solution().shortestPathBinaryMatrix(grid)
print(ans)

