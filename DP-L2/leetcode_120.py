from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second-last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update the current cell by adding the minimum of the two adjacent cells from the row below
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        # The top element will contain the minimum path sum
        print(triangle)
        return triangle[0][0]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Solution().minimumTotal(triangle)