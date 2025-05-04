class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = [int(_) for _ in num]
        stack = list()
        for n in num:
            while (stack and k > 0 and stack[-1] > n):
                stack.pop()
                k -= 1
            stack.append(n)
        while (k > 0):
            stack.pop()
            k -= 1
        while (stack and stack[0] == "0"):
            stack.pop(0)
        if not stack:
            return "0"
        return "".join([str(_) for _ in stack])

Solution().removeKdigits("10200", 1)
