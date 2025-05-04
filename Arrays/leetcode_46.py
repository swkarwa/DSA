from typing import List


class Solution:
    def permute(self, nums):
        result = []
        def p(rest:List[int], current:List[int]):
            if not rest:
                result.append(current[:])
            for i in range(len(rest)):
                new_current = current + [rest[i]]
                new_rest = rest[:i] + rest[i+1:]
                p(new_rest , new_current)
        p(nums , [])
        return result


result = Solution().permute([1, 2, 3])
print(result)
