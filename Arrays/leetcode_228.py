from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        right = 0
        left = 0
        result = []
        while right < len(nums) - 1:
            diff = nums[right + 1] - nums[right]
            if (diff == 1):
                right += 1
            elif (diff != 1):
                if (left == right):
                    result.append(str(nums[right]))
                else:
                    s = str(nums[left]) + "->" + str(nums[right])
                    result.append(s)
                right += 1
                left = right

        if (left == right):
            result.append(str(nums[right]))
        else:
            s = str(nums[left]) + "->" + str(nums[right])
            result.append(s)
        return result

result = Solution().summaryRanges([0,2,3,4,6,8,9])
print(result)