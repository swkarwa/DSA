from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        max_row = max(row[0] for row in stones)
        max_col = max(row[1] for row in stones)

        grid = [["." for col in range(max_col + 1)] for row in range(max_row + 1)]
        visited = [[False for col in range(max_col + 1)] for row in range(max_row + 1)]

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if [r, c] in stones:
                    grid[r][c] = "S"

        stones_to_remove = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):

                if (grid[r][c] == "S"):
                    visited[r][c] = True
                    if self.can_remove(grid, visited, r, c):
                        stones_to_remove += 1
        return stones_to_remove

    def can_remove(self, grid, visited, r, c):

        if_stone_in_row, if_stone_in_col = False, False

        # check in row
        for row in range(len(grid)):
            if grid[row][c] == "S" and not visited[row][c]:
                if_stone_in_row = True
                break

        # check in row
        for col in range(len(grid[r])):
            if grid[r][col] == "S" and not visited[r][col]:
                if_stone_in_col = True
                break

        return if_stone_in_row or if_stone_in_col
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
ans = Solution().removeStones(stones)
print(ans)