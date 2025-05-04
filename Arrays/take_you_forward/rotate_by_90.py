from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # convert rows to cols
        for i in range(len(matrix)):
            for j in range(i,len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse order of each row
        for arr in matrix:
            i = 0
            j = len(arr) - 1
            while (i < j):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return matrix

Solution().rotate(
[[1,2,3],[4,5,6],[7,8,9]]
)
