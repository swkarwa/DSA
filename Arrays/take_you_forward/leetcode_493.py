from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        stack = list()
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            while (stack and nums[i] < 2*nums[stack[-1]]):
                stack.pop()
            if(stack):
                count+=1
            stack.append(i)
        print(count)
        return count



Solution().reversePairs([1,3,2,3,1])