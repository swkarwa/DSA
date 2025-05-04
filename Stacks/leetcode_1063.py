class Solution:
    def validSubarrays(self, nums) -> int:
        stack = list()
        right = [0] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            while (stack and nums[stack[-1]] < nums[i]):
                stack.pop()
            if (not stack):
                right[i] = len(nums)
            else:
                right[i] = stack[-1]
            stack.append(i)
        print(right)
        return 0

Solution().validSubarrays([1,4,2,5,3])