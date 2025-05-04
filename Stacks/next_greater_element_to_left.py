def next_greater(nums: list) -> list:
    stack = list()
    stack.insert(0, -1)
    result = list()
    result.insert(0,-1)
    for i in range(1 , len(nums)):
        while(stack and stack[-1] < nums[i]):
            stack.pop()
        if(not stack):
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(nums[i])
    print(result)

def next_greater_index(nums: list) -> list:
    stack = list()
    result = list()
    for i in range(len(nums)):
        while(stack and nums[stack[-1]] <= nums[i]):
            stack.pop()
        if(not stack):
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(i)
    print(result)


next_greater_index([10 ,4 ,5 ,90, 120, 80])