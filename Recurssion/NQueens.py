from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(r):
            if (r == n):
                result.append(["".join(row) for row in board])
                return
            for c in range(n):
                di = (r+c)
                rdi = (r-c)+(n - 1)
                if (cols[c] == 0 and diag[di] == 0 and rdiag[rdi] == 0):
                    cols[c] = diag[di] = rdiag[rdi] = 1
                    board[r][c] = "Q"
                    solve(r + 1)
                    cols[c] = diag[di] = rdiag[rdi] = 0
                    board[r][c] = "."

        board = [["."] * n for _ in range(n)]
        cols = [0] * n  # keep track of cols
        diag = [0] * (2 * n - 1)  # keep track for diagnals topL->bottomR
        rdiag = [0] * (2 * n - 1)  # keep track of digonals bottomL->topR
        result = []
        solve(0)
        print(result)
        return result

Solution().solveNQueens(4)