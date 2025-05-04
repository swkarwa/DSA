class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        big_map, small_map = dict(), dict()
        for _ in t:
            small_map[_] = small_map.get(_, 0) + 1
        match_count = 0
        i = j = 0
        while (True):
            f1 = False
            f2 = False
            # aquiring window here
            while (i < len(s) and match_count < len(t)):
                f1 = True
                ch = s[i]

                big_map[ch] = big_map.get(ch, 0) + 1

                if (big_map.get(ch, 0) <= small_map.get(ch, 0)):
                    match_count += 1
                i += 1

            # start releasing here
            while (j < i and match_count == len(t)):
                f2 = True
                pans = s[j:i]
                if (not ans or len(pans) < len(ans)):
                    ans = pans
                ch = s[j]
                if (big_map.get(ch, 0) == 1):
                    big_map.pop(ch)
                else:
                    big_map[ch] = big_map.get(ch, 0) - 1

                if (big_map.get(ch, 0) < small_map.get(ch, 0)):
                    match_count -= 1
                j += 1

            if (not f1 and not f2):
                break
        return ans

    def minWindow_0(self, s: str, t: str) -> str:
        small_map, big_map = dict(), dict()
        left,right ,match_count = 0, 0 , 0
        ans = ""
        for c in t:
            small_map[c] = small_map.get(c, 0) + 1
        # expand right_corner of window

        for right in range(len(s)):
            ch = s[right]
            big_map[ch] = big_map.get(ch, 0) + 1

            if (big_map.get(ch, 0) <= small_map.get(ch, 0)):
                match_count += 1

            # release loop from left corner of window
            while (left <= right and match_count == len(t)):
                pans = s[left:right + 1]
                if (not ans or len(pans) < len(ans)):
                    ans = pans
                ch = s[left]
                big_map[ch] = big_map.get(ch, 0) - 1
                if (big_map.get(ch) == 0):
                    big_map.pop(ch)
                if (big_map.get(ch, 0) < small_map.get(ch, 0)):
                    match_count -= 1
                left += 1
            right+=1

        return ans


result = Solution().minWindow_0("ADOBECODEBANC", "ABC")
print(result)
