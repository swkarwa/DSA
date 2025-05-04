class Solution:
    def mostCompetitive(self, nums, k: int):
        stack = []
        n = len(nums)

        for i in range(n):
            num = nums[i]
            while stack and stack[-1] > num and len(stack) + (n - i) > k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        print(stack)
        return stack

Solution().mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4)
