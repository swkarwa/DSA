def is_balanced(s: str):
    stack = list()
    for c in s:
        if (c == ')'):
            if (stack and stack[-1] == '('):
                stack.pop()
            else:
                return False
        if (c == '}'):
            if (stack and stack[-1] == '{'):
                stack.pop()
            else:
                return False
        if (c == ']'):
            if (stack and stack[-1] == '['):
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    if (stack):
        return False
    return True


is_balanced("()[]{}")
