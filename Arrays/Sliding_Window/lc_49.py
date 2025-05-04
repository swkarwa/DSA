from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using defaultdict to simplify the grouping
        anagrams = defaultdict(list)

        for s in strs:
            # Sort the string to generate a key
            key = tuple(sorted(s))
            # Append the original string to the appropriate group
            anagrams[key].append(s)

        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())

result = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)