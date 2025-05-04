from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        total_empty_squares = 0
        start_row = start_col = -1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    total_empty_squares += 1
                elif grid[r][c] == 1:
                    total_empty_squares += 1
                    start_row, start_col = r, c

        return self.back_track(grid, start_row, start_col, total_empty_squares)

    def back_track(self, grid, r, c, total_empty_square):
        if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == -1):
            return 0

        if (grid[r][c] == 2):
            return 1 if total_empty_square == 0 else 0

        temp = grid[r][c]
        grid[r][c] = -1
        total_empty_square -= 1
        total_paths = (
                self.back_track(grid, r + 1, c, total_empty_square) +
                self.back_track(grid, r - 1, c, total_empty_square) +
                self.back_track(grid, r, c + 1, total_empty_square) +
                self.back_track(grid, r, c - 1, total_empty_square)
        )
        grid[r][c] = temp
        total_empty_square += 1
        return total_paths

grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
result = Solution().uniquePathsIII(grid)
print(result)
