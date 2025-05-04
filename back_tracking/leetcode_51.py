from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(r):
            # base case
            if (r == n):
                result.append(["".join(row) for row in board])
                return

            for c in range(n):
                di = (r + c)
                rdi = (r - c) + (n - 1)
                if (cols[c] == 0 and diag[di] == 0 and rdiag[rdi] == 0):
                    board[r][c] = "Q"
                    diag[di] = rdiag[rdi] = cols[c] = 1

                    solve(r + 1)

                    diag[di] = rdiag[rdi] = cols[c] = 0
                    board[r][c] = "."

        board = [["."] * n for r in range(n)]
        cols = [0] * n
        diag = [0] * (2 * n - 1)
        rdiag = [0] * (2 * n - 1)
        result = []
        solve(0)
        print(result)
        return result
Solution().solveNQueens(4)