from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = [[False for col in row] for row in grid]
        q = deque()
        for r in range(len(grid)):
            got_component = False
            for c in range(len(grid)):
                if (grid[r][c] == 1):
                    got_component = True
                    self.dfs(grid, r, c, visited, q)
                    break
            if(got_component):
                break
        level = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while (q):

            size = len(q)
            while (size > 0):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or visited[nr][nc]):
                        continue
                    if (not visited[nr][nc] and grid[nr][nc] == 1):
                        return level
                    visited[nr][nc] = True
                    q.append((nr, nc))
                size -= 1
            level += 1
        return -1

    def dfs(self, grid, r, c, visited, q):
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or visited[r][c] or grid[r][c] == 0):
            return

        visited[r][c] = True
        q.append((r, c))
        self.dfs(grid, r + 1, c, visited, q)
        self.dfs(grid, r - 1, c, visited, q)
        self.dfs(grid, r, c + 1, visited, q)
        self.dfs(grid, r, c - 1, visited, q)


ans = Solution().shortestBridge([[0, 1], [1, 0]])
print(ans)
