from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        if (nums[0] != nums[1]):
            return nums[0]
        if (nums[-1] != nums[-2]):
            return nums[-1]

        l = 1;
        h = len(nums) - 2
        while (l <= h):
            mid = (l + h) // 2
            if (nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]):
                return nums[mid]

            # ditermine which halves is odd
            elif (nums[mid] == nums[mid - 1]):
                left_count = (mid - l + 1)
                if (left_count % 2 == 0):
                    l = mid + 1
                else:
                    h = mid - 2
            elif (nums[mid] == nums[mid + 1]):
                right_count = (h - mid) + 1
                if (right_count % 2 == 0):
                    h = mid - 1
                else:
                    l = mid + 2
        return -1

result = Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print(result)