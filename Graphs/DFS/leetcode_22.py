from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(n, cn, on, ans):
            if (cn == on == n):
                result.append(ans)
                return

            if (on > n or cn > on):
                return

            dfs(n, cn, on + 1, ans + "(")
            dfs(n, cn + 1, on, ans + ")")

        result = []
        dfs(n, 0, 0, "")
        return result


s = Solution()
result = s.generateParenthesis(3)
print(result)
