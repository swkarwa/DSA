from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        for r in range(len(image)):
            for c in range(len(image[r])):
                if (r == sr and c == sc):
                    self.back_track(image, r, c, image[r][c], color)
                    return image

    def back_track(self, image, r, c, pixel_value, color):
        if (r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != pixel_value):
            return

        if(image[r][c] == pixel_value):
            image[r][c] = color

        self.back_track(image, r - 1, c, pixel_value, color)
        self.back_track(image, r + 1, c, pixel_value, color)
        self.back_track(image, r, c - 1, pixel_value, color)
        self.back_track(image, r, c + 1, pixel_value, color)


image = [

    [1, 1, 1], [1, 1, 0], [1, 0, 1]
]
result = Solution().floodFill(image, 1, 1, 2)
print(result)
