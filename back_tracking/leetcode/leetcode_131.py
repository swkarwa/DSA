from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(substr):
            return substr == substr[::-1]  # check if palindome

        def back_track(start:int, current:List[int]):
            if (start == len(s)):
                result.append(current[:])
                return

            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if(is_palindrome(substr)):
                    current.append(substr)
                    back_track(end , current)
                    current.pop()

        result = list()
        back_track(0 , [])
        print(result)
        return result


s = "aab"
Solution().partition(s)