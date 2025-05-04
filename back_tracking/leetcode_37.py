from typing import List


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve_sudoku(0, 0, board)
        return board

    def solve_sudoku(self, r, c, board):

        # base case
        if (r == len(board)):
            return True

        # decide index next cells to call
        nr = nc = -1
        if (c == len(board[0]) - 1):
            nr = r + 1
            nc = 0
        else:
            nr = r
            nc = c + 1

        if (board[r][c] == "."):
            for option in range(1, 10):  # values from 1-9
                if (self.is_valid(board, r, c, option)):  # check if option can be placed on current cell
                    board[r][c] = str(option)
                    if (self.solve_sudoku(nr, nc, board)): return True
                    board[r][c] = "."
        else:
            return self.solve_sudoku(nr, nc, board)

        return False

    def is_valid(self, board, r, c, option):
        # check in col
        for row in range(len(board)):
            if (board[row][c] == str(option)):
                return False

        # check in row
        for col in range(len(board[0])):
            if (board[r][col] == str(option)):
                return False

        # check in sub_matrix
        sr = 3 * (r // 3)
        sc = 3 * (c // 3)
        for row in range(0, 3):
            for col in range(0, 3):
                if (board[sr + row][sc + col] == str(option)):
                    return False
        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

resullt = Solution().solveSudoku(board)
for row in resullt:
    print(row)
