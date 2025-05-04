from typing import List
# optimized approach
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # decides if first col should be zero
        col0 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == 0):
                    matrix[i][0] = 0

                    if (j != 0):
                        matrix[0][j] = 0
                    else:
                        col0 = 0  # if 0th column, then col0 = 0

        # step-2 : if any of row and col are zero then it is 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if (matrix[i][j] != 0):
                    if (matrix[i][0] == 0 or matrix[0][j] == 0):
                        matrix[i][j] = 0

        # step3: solve 0th row first as right corneer element is dependent on 1st element of 1st row
        if (matrix[0][0] == 0):
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        # finally first col
        if (col0 == 0):
            for i in range(len(matrix)):
                matrix[i][0] = 0