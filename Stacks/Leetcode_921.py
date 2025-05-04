class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = list()
        for c in s:
            if(c ==')'):
                if(stack and stack[-1] == '('):
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        print(stack)
        return len(stack)

Solution().minAddToMakeValid("())")