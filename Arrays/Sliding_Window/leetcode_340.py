class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        map = dict()
        i = j = -1
        max_len = 0
        while (True):
            f1 = f2 = False

            while (i < len(s) - 1):
                f1 = True
                i += 1
                ch = s[i]
                map[ch] = map.get(ch, 0) + 1
                if (len(map) <= k):
                    max_len = max(max_len, (i - j))
                else:
                    break

            while (j < i):
                f2 = True
                j += 1
                ch = s[j]
                map[ch] -= 1
                if (map[ch] == 0):
                    map.pop(ch)
                if (len(map) <= k):
                    max_len = max(max_len, (i - j))
                    break

            if (not f1 and not f2):
                break
        return max_len

    def lengthOfLongestSubstringKDistinct_o(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        table = dict()
        for right in range(len(s)):
            ch = s[right]
            table[ch] = table.get(ch, 0) + 1
            while (len(table) > k):
                ch = s[left]
                table[ch] = table.get(ch, 0) - 1
                if (table.get(ch) == 0):
                    table.pop(ch)
                left += 1
            if (len(table) <= k):
                ans = max(ans, right - left + 1)
        return ans


result = Solution().lengthOfLongestSubstringKDistinct_o("ab", 1)
print(result)
