class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0;
        j = 0;
        stack = list()
        for push in pushed:
            stack.append(push)
            while (stack and stack[-1] == popped[j]):
                stack.pop()
                j += 1
        return j == len(popped)



Solution().validateStackSequences([1,2,3,4,5] , [4,3,5,1,2])