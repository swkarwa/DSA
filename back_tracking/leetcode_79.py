from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        grid = [[False for _ in b] for b in board]
        i = 0  # pointer to keep a track on word
        for r in range(len(board)):

            for c in range(len(board[r])):
                if (board[r][c] == word[0] and self.back_track(board, word, r, c, 0)):
                    return True
        return False

    def back_track(self, board, word, r, c, i):

        if (i == len(word)):
            return True

        if (r <= 0 or r >= len(board) or c <= 0 and c >= len(board[0]) or board[r][c] == '$'):
            return False

        if (board[r][c] != word[i]):
            return False

        val = board[r][c]
        board[r][c] = '$'

        found = (
                self.back_track(board, word, r + 1, c, i + 1) or
                self.back_track(board, word, r - 1, c, i + 1) or
                self.back_track(board, word, r, c + 1, i + 1) or
                self.back_track(board, word, r, c - 1, i + 1)
        )
        board[r][c] = val
        return found

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
result = Solution().exist(board, "ABCB")
print(result)
