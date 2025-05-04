"""
    for a string "a1b1c1a12c15 -> add up digitis of repeated frequencies and print in ascending order of charachters
    output -> a13b1c16

"""
from collections import defaultdict


class Solution:
    def compress(self, s: str):
        map = defaultdict(int)
        i = 0
        while i < len(s):
            char = s[i]
            num_i = i + 1
            while num_i < len(s) and s[num_i].isdigit():
                num_i += 1
            freq = int(s[i+1: num_i])
            map[char] += freq
            i = num_i
        sorted_items = sorted(map.items())
        result = "".join(f"{char}{freq}" for char, freq in sorted_items)
        return result

result = Solution().compress("a1b1c1a12c15")
print(result)
