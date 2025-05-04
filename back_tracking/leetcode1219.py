from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold = 0  # Initialize to 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):  # Iterate over columns
                if grid[r][c] > 0:  # Start from cells with gold
                    gold = self.get_gold_from_position(grid, r, c)
                    max_gold = max(max_gold, gold)

        return max_gold

    def get_gold_from_position(self, grid, r, c):
        # Check for out of bounds or if the cell has no gold
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
            return 0

        current_gold = grid[r][c]  # Store the current cell's gold
        grid[r][c] = 0  # Mark the cell as visited by setting it to 0

        # Explore all four directions
        gold = current_gold + (
                self.get_gold_from_position(grid, r + 1, c) +
                self.get_gold_from_position(grid, r - 1, c) +
                self.get_gold_from_position(grid, r, c - 1) +
                self.get_gold_from_position(grid, r, c + 1)
        )

        grid[r][c] = current_gold  # Restore the original value

        return gold


# Example usage
solution = Solution()
grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
print(solution.getMaximumGold(grid))  # Should output 24
