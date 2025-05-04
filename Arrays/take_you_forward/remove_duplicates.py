from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        u = 1
        for i in range(1, len(nums)):
            if(nums[i] != nums[u-1]):
                nums[u] = nums[i]
                u+=1
        print(nums[:u])
        return 0

Solution().removeDuplicates([0,1,1,1,2,2,3,3,4])