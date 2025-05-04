class Solution:
    def knight_tour(self, n, m):
        """
        create a chess board
        :param n: rows
        :param m: cols
        :return: True
        """
        board = [["."] * m for _ in range(n)]
        for start_row in range(n):
            for start_col in range(m):
                print(f"Trying starting position: ({start_row}, {start_col})")
                if self.dfs(board, start_row, start_col, 1):
                    print("Found a valid Knight's Tour!")
                    return  # Stop after finding the first solution
                else:
                    print("No valid Knight's Tour from this position.\n")

    def dfs(self, board, r, c, move_number):
        if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == "K"):
            return False

        if (move_number == len(board) * len(board[0])):
            board[r][c] = "K"  # make a final move
            for row in board:
                print(row)
            board[r][c] = "."
            return True

        board[r][c] = "K"
        # All possible knight moves
        moves = [
            (-2, 1), (-1, 2), (1, 2), (2, 1),  # move right side of the board
            (2, -1), (1, -2), (-1, -2), (-2, -1)  # move left side of the board
        ]

        # Try all moves
        for dr, dc in moves:
            if self.dfs(board, r + dr, c + dc, move_number + 1):
                return True
        board[r][c] = "."
        return False


s = Solution()
s.knight_tour(8, 8)
