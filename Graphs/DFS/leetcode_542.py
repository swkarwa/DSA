from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        # Initialize distance matrix
        distance = [[0 if mat[r][c] == 0 else float('inf') for c in range(cols)] for r in range(rows)]
        q = deque()

        # Enqueue all cells with 0s
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    distance[r][c] = float('inf')

        # Directions for moving in 4 possible ways
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS to find the minimum distance for all cells
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                # Check bounds and whether we found a shorter distance
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if distance[new_r][new_c] > distance[r][c] + 1:
                        distance[new_r][new_c] = distance[r][c] + 1
                        q.append((new_r, new_c))

        return distance


mat = [[0,0,0],[0,1,0],[1,1,1]]
Solution().updateMatrix(mat)