from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        memo = {}

        def get_total(r, c):

            if (r, c) in memo:
                return memo[(r, c)]

            if (r >= len(dungeon) or c >= len(dungeon[0])):
                return float('inf')

            # queen found
            if (r == len(dungeon) - 1 and c == len(dungeon[0]) - 1):
                return max(1, 1 - dungeon[r][c])

            from_down = get_total(r + 1, c)
            from_right = get_total(r, c + 1)

            min_health = min(from_down, from_right)

            survival_health = max(1, min_health - dungeon[r][c])
            memo[(r, c)] = survival_health

            return survival_health

        return get_total(0, 0)


dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
result = Solution().calculateMinimumHP(dungeon)
print(result)
