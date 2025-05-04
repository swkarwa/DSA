class Solution:
    def merge_sort(self, nums, low, high):
        if (low >= high):
            return
        mid = (low + high) // 2
        self.merge_sort(nums, low, mid)
        self.merge_sort(nums, mid + 1, high)
        self.merge(nums, low, mid, high)

    def merge(self, nums, low, mid, high):
        left = nums[low: mid + 1]
        right = nums[mid + 1: high + 1]
        l = r = 0
        k = low
        while (l < len(left) and r < len(right)):
            if (left[l] <= right[r]):
                nums[k] = left[l]
                l += 1
            else:
                nums[k] = right[r]
                r += 1
            k += 1

        while (l < len(left)):
            nums[k] = left[l]
            l += 1
            k += 1

        while (r < len(right)):
            nums[k] = right[r]
            r += 1
            k += 1


nums = [1, 3, 2, 3, 1]
Solution().merge_sort(nums, 0, len(nums) - 1)
print(nums)
