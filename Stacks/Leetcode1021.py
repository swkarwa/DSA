class Solution():
    def removeOuterParentheses(self, s):
        stack = list()
        result = list()
        for c in s:
            if(c == '('):
                # if stack is empty not considered for ans as it is outermost element
                if(stack):
                    result.append(c)
                stack.append(c)
            else:
                stack.pop()
                # if stack is empty not considered for ans as it is outermost element
                if(stack):
                    result.append(c)

        return "".join(result)


result = Solution().removeOuterParentheses("(()())(())")
print(result)