class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = dict()
        i, j = -1, -1
        ans = 0
        while True:
            f1 = False
            f2 = False
            # aquire till chars in string is unique
            while (i < len(s) - 1):
                f1 = True
                i += 1
                ch = s[i]
                map[ch] = map.get(ch, 0) + 1
                if (map.get(ch) == 2):
                    break
                else:
                    length = (i - j)
                    if (length > ans):
                        ans = length

            # release loop till ch freq == 1
            while (j < i):
                f2 = True
                j += 1
                ch = s[j]
                map[ch] = map.get(ch, 0) - 1
                if (map[ch] == 1):
                    break

            if (not f1 and not f2):
                break
        return ans

    def lengthOfLongestSubstring_0(self, s: str) -> int:
        table = dict()
        left, ans = 0, 0
        # aquire loop
        for right in range(len(s)):
            ch = s[right]
            table[ch] = table.get(ch, 0) + 1
            # release loop
            while left <= right and table.get(ch, 0) > 1:
                left_ch = s[left]
                table[left_ch] = table.get(left_ch, 0) - 1
                if (table.get(left_ch, 0) == 0):
                    table.pop(left_ch)
                left += 1

            ans = max(ans, right - left + 1)
        return ans


result = Solution().lengthOfLongestSubstring_0("pwwkew")
print(result)
