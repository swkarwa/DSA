# BFS
from collections import deque
from typing import List


class Color:
    def __init__(self, r, c, color):
        self.r = r
        self.c = c
        self.color = color


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        visited = [[False for _ in r] for r in image]
        q = deque()
        clr = Color(sr, sc, image[sr][sc])
        q.append(clr)
        image[sr][sc] = color
        visited[sr][sc] = True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while (q):
            top = q.popleft()
            r, c = top.r, top.c
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if (
                        0 <= new_r < len(image) and
                        0 <= new_c < len(image[0]) and
                        not visited[new_r][new_c] and
                        image[new_r][new_c] == top.color

                ):
                    clr = Color(new_r, new_c, image[new_r][new_c])  # store original color before changing
                    q.append(clr)
                    image[new_r][new_c] = color  # change color
                    visited[new_r][new_c] = True

        return image

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0
result = Solution().floodFill(image , sr , sc , color)
print(image)