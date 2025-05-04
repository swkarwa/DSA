class Solution:
    def next_greater(self, nums):
        left = [0]*len(nums)
        right= [0]*len(nums)
        stack = list()
        for i in range(len(nums)):
            while(stack and nums[stack[-1]]<= nums[i]):
                right[stack[-1]] = nums[i]
                stack.pop()
            if(not stack):
                left[i] = -1
            else:
                left[i] = nums[stack[-1]]
            stack.append(i)
        while(stack):
            right[stack.pop()] = len(nums)
        print(left)
        print(right)

    def next_greater_index(self,nums):
        left = [0] * len(nums)
        right = [0] * len(nums)
        stack = list()
        for i in range(len(nums)):
            while(stack and nums[stack[-1]] <= nums[i]):
                right[stack[-1]] = i
                stack.pop()
            if(not stack):
                left[i] = -1
            else:
                left[i] = stack[-1]
            stack.append(i)
        while(stack):
            right[stack.pop()] = len(nums)
        print(left)
        print(right)



Solution().next_greater_index([10 ,4 ,5 ,90, 120, 80])