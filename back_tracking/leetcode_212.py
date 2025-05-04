from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        for word in words:
            word_added = False
            for r in range(len(board)):
                for c in range(len(board[r])):
                    if (board[r][c] == word[0] and self.check_word(board, r, c, word, 0)):
                        word_added = True
                        result.add(word)
            if (not word_added):
                break

        return list(result)

    def check_word(self, board, r, c, word, i):
        if (i == len(word)):
            return True
        if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == '$'):
            return False

        if (board[r][c] != word[i]):
            return False

        temp = board[r][c]
        board[r][c] = '$'

        found = (
                self.check_word(board, r + 1, c, word, i + 1) or
                self.check_word(board, r - 1, c, word, i + 1) or
                self.check_word(board, r, c + 1, word, i + 1) or
                self.check_word(board, r, c - 1, word, i + 1)
        )

        board[r][c] = temp
        return found

board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
result = Solution().findWords(board , ["oa","oaa"])
print(result)