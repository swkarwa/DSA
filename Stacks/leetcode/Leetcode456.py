class Solution:
    def find132pattern(self, nums) -> bool:
        if(len(nums) < 3):
            return False
        s3 = float('-inf')
        stack = list()
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            if num < s3:
                return True
            while stack and num > stack[-1]:
                s3 = stack.pop()
            stack.append(num)
        return False


result = Solution().find132pattern([3,1,4,2])
print(result)