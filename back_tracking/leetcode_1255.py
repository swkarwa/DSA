from typing import List

from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_f = Counter(letters)
        return self.find_max_score(0, words, letter_f, score)

    def find_max_score(self, idx, words, letter_f, score):
        if (idx == len(words)):
            return 0

        score_no = self.find_max_score(idx + 1, words, letter_f, score)

        word = words[idx]
        can_use_word = True
        score_of_current_word = 0

        temp_f = letter_f.copy()
        for c in word:
            if temp_f[c] > 0:
                temp_f[c] -= 1
                score_of_current_word += score[ord(c) - ord('a')]
            else:
                can_use_word = False
                break
        score_yes = 0
        if can_use_word:
            score_yes = score_of_current_word + self.find_max_score(idx + 1, words, temp_f, score)

        return max(score_yes, score_no)


words = ["dog", "cat", "dad", "good"]
letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

scores_of_each_word = []
for word in words:
    score_of_current_word = 0
    for c in word:
        score_of_current_word+= score[ord(c) - ord('a')]
    scores_of_each_word.append(score_of_current_word)

print(scores_of_each_word)
s = Solution()
result = s.maxScoreWords(words, letters, score)
print(result)
