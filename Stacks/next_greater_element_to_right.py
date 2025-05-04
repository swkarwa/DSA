def next_greater(nums: list) -> list:
    result = list()
    stack = list()
    for j in range(len(nums) - 1, -1, -1):
        while (stack and stack[-1] <= nums[j]):
            stack.pop()
        if (not stack):
            result.insert(0, -1)
        else:
            result.insert(0, stack[-1])
        stack.append(nums[j])
    print(result)

def next_greater_index(nums: list) -> list:
    result = list()
    stack = list()
    for j in range(len(nums) - 1, -1, -1):
        while (stack and nums[stack[-1]] <= nums[j]):
            stack.pop()
        if (not stack):
            result.insert(0, -1)
        else:
            result.insert(0, stack[-1])
        stack.append(j)
    print(result)


next_greater([1, 3, 4, 2])
