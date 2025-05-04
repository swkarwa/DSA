from typing import List
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(r: int, c: int):
            # Check boundaries and if the current cell is 'O'
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != 'O':
                return

            # Mark the current cell as visited (temporary)
            board[r][c] = 'E'  # E for escaped

            # Recursively visit all adjacent cells
            dfs(r - 1, c)  # north
            dfs(r, c + 1)  # east
            dfs(r + 1, c)  # south
            dfs(r, c - 1)  # west

        # Start DFS from the border 'O's
        for r in range(len(board)):
            for c in range(len(board[0])):
                # Only start DFS from the border 'O's
                if (r in {0, len(board) - 1} or c in {0, len(board[0]) - 1}) and board[r][c] == 'O':
                    dfs(r, c)

        # Final pass to convert 'O's to 'X's and 'E's back to 'O's
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Capture surrounded 'O's
                elif board[r][c] == 'E':
                    board[r][c] = 'O'  # Restore escaped 'O's

board = [["O","O","O"],["O","O","O"],["O","O","O"]]
Solution().solve(board)
print(board)