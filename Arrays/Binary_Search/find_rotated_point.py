class Solution:
    def findKRotation(self, nums):
        # code here
        l = 0
        h = len(nums) - 1
        ans = -1
        if (nums[l] <= nums[h]):
            return 0

        while (l <= h):
            mid = (l + h) // 2

            if (nums[mid] > nums[mid + 1]):
                ans = (mid + 1)
            elif (nums[mid] < nums[mid - 1]):
                ans = mid

            # left part is sorted
            if (nums[l] <= nums[mid]):
                l = mid + 1
            # right_part is sorted
            if (nums[mid] <= nums[h]):
                h = mid - 1

        return ans


Solution().findKRotation([14, 17, 22, 41, 10])
