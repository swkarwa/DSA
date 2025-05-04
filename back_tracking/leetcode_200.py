from back_tracking.leetcode_733_flood_fill import image
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_islands(r, c):
            if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0'):
                return

            grid[r][c] = '0'
            get_islands(r, c + 1)  # east
            get_islands(r + 1, c)  # south
            get_islands(r, c - 1)  # west
            get_islands(r - 1, c)  # north

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                if (grid[r][c] == '1'):
                    count += 1
                    get_islands(r, c)
        return count

grid = [["1"],["1"]]
count = Solution().numIslands(grid)
print(count)