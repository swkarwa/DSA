import sys
from typing import List

def largest_rectangle_area(self, heights: List[int]) -> int:
    # next smaller to right
    stack = list()
    nser = list()
    for i in range(len(heights) - 1, -1, -1):
        while (stack and heights[stack[-1]] >= heights[i]):
            stack.pop()
        if (not stack):
            nser.insert(0, len(heights))
        else:
            nser.insert(0, stack[-1])
        stack.append(i)

    stack.clear()
    nsel = list()
    for i in range(len(heights)):
        while (stack and heights[stack[-1]] >= heights[i]):
            stack.pop()
        if (not stack):
            nsel.append(-1)
        else:
            nsel.append(stack[-1])
        stack.append(i)

    _max = 0
    for i in range(len(heights)):
        width = nser[i] - nsel[i] - 1
        height = heights[i]
        area = width * height
        if (area > _max):
            _max = area
    return _max


largest_rectangle_area([2, 1, 5, 6, 2, 3])
