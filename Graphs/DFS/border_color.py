from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        original_color = grid[row][col]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        border = set()

        def dfs(r, c):
            grid[r][c] = -original_color  # Mark as visited with a temporary color
            is_border = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == -original_color:
                        continue  # Already visited
                    elif grid[nr][nc] == original_color:
                        dfs(nr, nc)  # Continue DFS for the same color
                    elif (grid[nr][nc] != original_color):
                        is_border = True  # Found a different color, mark as border
                else:
                    is_border = True  # Out of bounds, also a border

            if is_border:
                border.add((r, c))
            grid[r][c] = original_color

        dfs(row, col)
        for r, c in border:
            grid[r][c] = color
        return grid


grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

result = Solution().colorBorder(grid, 0, 0, 3)
for r in result:
    print(r)
