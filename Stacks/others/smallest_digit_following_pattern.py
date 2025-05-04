class Solution:
    def smallestNumber(self, pattern: str):
        stack = list()
        counter = 1;
        result = ""
        for s in pattern:
            if s == 'D':
                stack.append(counter)  # push and increase
                counter += 1
            else:
                stack.append(counter)  # push -> increase -> pop till len(stack) > 0
                counter += 1
                while (stack):
                    result += str(stack.pop())

        stack.append(counter)
        while (stack):
            result += str(stack.pop())
        return result


result = Solution().smallestNumber("IIIDIDDD")
print(result)
