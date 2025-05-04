class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = [_ for _ in s]
        stack = list()
        for i in range(len(s)):
            c = s[i]
            if (c == ')'):
                if (stack and s[stack[-1]] == '('):
                    stack.pop()
                else:
                    stack.append(i)
            elif (c == '('):
                stack.append(i)

        while (stack):
            s[stack.pop()] = "."

        return "".join(s).replace(".", "")

Solution().minRemoveToMakeValid("lee(t(c)o)de)")