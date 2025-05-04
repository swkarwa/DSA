from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def back_track(start, combinations):

            if len(combinations) == k:
                result.append(combinations[:])

            for i in range(start, n + 1):
                combinations.append(i)
                back_track(i + 1, combinations)
                combinations.pop()

        back_track(1, [])
        return result
n = 4
k = 2
Solution().combine(n , k)