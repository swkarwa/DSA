from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        big_map, small_map = dict(), dict()
        ans, left, match_count = list(), 0, 0
        # compute small map

        for _ in p:
            small_map[_] = small_map.get(_, 0) + 1

        for right in range(len(s)):
            ch = s[right]
            big_map[ch] = big_map.get(ch, 0) + 1

            if (big_map.get(ch, 0) <= small_map.get(ch, 0)):
                match_count += 1

            while (left <= right and match_count == len(p)):
                if (big_map == small_map):
                    ans.append(left)
                left_ch = s[left]
                big_map[left_ch] = big_map.get(left_ch, 0) - 1
                if (big_map.get(left_ch, 0) == 0):
                    big_map.pop(left_ch)
                if(big_map.get(left_ch,0) < small_map.get(left_ch,0)):
                    match_count-=1
                left += 1
            if (big_map == small_map):
                ans.append(left)
        return ans


result = Solution().findAnagrams("cbaebabacd" , "abc")
print(result)