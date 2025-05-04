class Solution:
    def nextGreaterElements(self, nums):
        stack = list()
        result = list()
        for i in range(len(nums) - 2, -1, -1):
            while (stack and stack[-1] <= nums[i]):
                stack.pop()
            stack.append(nums[i])

        for i in range(len(nums) - 1, -1, -1):
            while (stack and stack[-1] <= nums[i]):
                stack.pop()
            if (not stack):
                result.insert(0, -1)
            else:
                result.insert(0, stack[-1])
            stack.append(nums[i])
        return result

print(Solution().nextGreaterElements([1,2,3,4,3]))
