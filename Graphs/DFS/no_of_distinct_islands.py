# User function Template for python3

import sys
from typing import List

sys.setrecursionlimit(10 ** 8)

"""
u -> up
d -> down
l -> left
r -> right
z -> backtrack

"""


class Solution:
    def __init__(self):

        self.path = ""

    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        # code here
        result = set()

        def dfs(r, c):

            grid[r][c] = 0

            # go up
            if (r - 1 >= 0 and grid[r - 1][c] == 1):
                self.path = self.path + "u"
                dfs(r - 1, c)

            # go down
            if (r + 1 < len(grid) and grid[r + 1][c] == 1):
                self.path = self.path + "d"
                dfs(r + 1, c)

            # go left
            if (c - 1 >= 0 and grid[r][c - 1] == 1):
                self.path = self.path + "l"
                dfs(r, c - 1)

            # go right
            if (c + 1 < len(grid[0]) and grid[r][c + 1] == 1):
                self.path = self.path + "r"
                dfs(r, c + 1)

            self.path += "z"

        for r in range(len(grid)):
            for c in range(len([r])):
                if (grid[r][c] == 1):
                    self.path = ""
                    dfs(r, c)
                    result.add(self.path)

        print(result)
        return len(result)


grid = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1]
]
Solution().countDistinctIslands(grid)
