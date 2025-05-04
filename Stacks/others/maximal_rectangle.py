import sys


class Solution:
    def maximalRectangle(self, matrix) -> int:

        heights = [int(_) for _ in matrix[0]]
        print(heights)
        _max = self.get_largest_area(heights)

        for i in range(1, len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == "1"):
                    heights[j] += 1
                else:
                    heights[j] = 0
            print(heights)
            area = self.get_largest_area(heights)
            if (area >= _max):
                _max = area
        return _max

    def get_largest_area(self, heights):
        left = [0] * len(heights)
        right = [0] * len(heights)
        stack = list()
        for i in range(len(heights)):
            while (stack and heights[stack[-1]] >= heights[i]):
                right[stack[-1]] = i
                stack.pop()
            if (not stack):
                left[i] = -1
            else:
                left[i] = stack[-1]
            stack.append(i)
        while (stack):
            right[stack.pop()] = len(heights)

        _max_area = -1 * sys.maxsize
        for i in range(len(heights)):
            width = right[i] - left[i] - 1;
            height = heights[i]
            area = height * width
            if (area > _max_area):
                _max_area = area
        return _max_area


matrix = [["1", "0", "1", "0", "0"],
 ["1", "0", "1", "1", "1"],
 ["1", "1", "1", "1", "1"],
 ["1", "0", "0", "1", "0"]]

Solution().maximalRectangle(matrix)
