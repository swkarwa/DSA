import string
from collections import deque
from typing import List

from collections import deque
from typing import List
import string

class Solution:
    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        word_list = set(word_list)  # Convert to set for O(1) lookup
        if end_word not in word_list:
            return []

        valid_chars = list(string.ascii_lowercase)
        seen = set([begin_word])  # Start with the whole word
        q = deque([[begin_word]])  # Initialize queue with path lists
        result = []
        found = False  # Indicates if any path reaches `end_word`
        level = 0

        while q and not found:
            size = len(q)
            current_level_seen = set()  # To add to `seen` after processing current level

            for _ in range(size):
                path = q.popleft()
                current_word = path[-1]

                # Check if we reached `end_word`
                if current_word == end_word:
                    result.append(path)
                    found = True

                # Try transforming `current_word`
                for idx in range(len(current_word)):
                    for c in valid_chars:
                        next_word = current_word[:idx] + c + current_word[idx+1:]
                        if next_word in word_list and next_word not in seen:
                            q.append(path + [next_word])  # Extend path with next_word
                            current_level_seen.add(next_word)

            seen.update(current_level_seen)  # Update seen only after processing the level
            level += 1  # Move to the next level after completing current level

        return result

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Solution().findLadders(beginWord , endWord , wordList)

