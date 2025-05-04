from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1

        # check if array is already sorted
        if (nums[l] < nums[h]):
            return nums[l]

        while (l <= h):
            mid = (l + h) // 2
            if(nums[l] > nums[mid] and nums[h] > nums[mid]):
                l+=1
                h-=1
            if (nums[mid] > nums[mid + 1]):
                return nums[mid + 1]
            elif (nums[mid] < nums[mid - 1]):
                return nums[mid]

            # if left half is sorted
            if (nums[l] <= nums[mid]):
                l = mid + 1  # discard left, as left is sorted and roateted point is not in left
            # if right half is sorted
            if (nums[mid] <= nums[h]):
                h = mid - 1  # discard right, as right is sorted and rotated point is not in right
        return -1


result = Solution().findMin([3,1,3])
print(result)