def is_valid(s:str)->bool:
    stack = list()
    for c in s:
        if(c == ')'):
            if not stack:
                return False
            if(stack[-1] == '('):
                return True
            else:
                while(stack[-1] != '('):
                    stack.pop()
                stack.pop()
        else:
            stack.append(c)
    return False

print(is_valid("(1)+((2))+(((3)))")) # positive case
print(is_valid(")")) # negative case