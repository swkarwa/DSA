class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = list()
        for c in s:
            if (c == ')'):
                result = list()
                while (stack[-1] != '('):
                    result += stack.pop()
                stack.pop()
                stack.extend(result)
            else:
                stack.append(c)

        print(stack)
        return "".join(result)

Solution().reverseParentheses("(u(love)i)")