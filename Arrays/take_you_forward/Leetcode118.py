from typing import List


class Solution:
    def nCr(self, n, r):
        if (r > n):
            return 0
        result = 1
        for i in range(r):
            result = result * (n - i) // (i + 1)
        return result

    def generate_brute(self, numRows: int):

        result = []
        for r in range(numRows):
            temp = []
            for c in range(r + 1):
                temp.append(self.nCr(r, c))
            result.append(temp)
        print(result)


Solution().generate_brute(5)
