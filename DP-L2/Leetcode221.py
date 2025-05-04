class Solution:
    def maximalSquare(self, matrix):
        dp = [[0 for col in row] for row in matrix]

        for r in range(len(matrix) - 1, -1, -1):
            for c in range(len(matrix[r]) - 1, -1, -1):
                # last cell
                if (r == len(matrix) - 1 and c == len(matrix[r]) - 1):
                    dp[r][c] = int(matrix[r][c])
                elif (r == len(matrix) - 1 or c == len(matrix[r]) - 1):
                    dp[r][c] = int(matrix[r][c])
                else:
                    if(matrix[r][c] == "1"):
                        dp[r][c] = 1 + min(dp[r][c + 1], dp[r + 1][c], dp[r + 1][c + 1])
                    else:
                        dp[r][c] = 0
        _max = -1
        for d in dp:
            _max = max(_max , max(d))
        print(_max*_max)
        return max

matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]
Solution().maximalSquare(matrix)
