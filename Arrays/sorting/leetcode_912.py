from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.count = [0] * len(nums)
        indexed_nums = list(enumerate(nums))  # Keep track of original indices
        self.merge_sort(indexed_nums, 0, len(nums) - 1)
        return self.count

    def merge_sort(self, indexed_nums, low, high):
        if low == high:
            return [indexed_nums[low]]

        mid = low + (high - low) // 2
        left_sorted = self.merge_sort(indexed_nums, low, mid)
        right_sorted = self.merge_sort(indexed_nums, mid + 1, high)
        return self.merge_sorted_arrays(left_sorted, right_sorted)

    def merge_sorted_arrays(self, left, right):
        merged = []
        i = 0
        j = 0
        right_count = 0

        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                self.count[left[i][0]] += right_count
                merged.append(left[i])
                i += 1
            else:
                right_count += 1
                merged.append(right[j])
                j += 1

        while i < len(left):
            self.count[left[i][0]] += right_count
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

result = Solution().countSmaller([5,2,6,1])
print(result)