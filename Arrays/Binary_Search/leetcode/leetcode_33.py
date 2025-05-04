from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , h = 0 , len(nums)-1
        while(l<=h):
            m = l+(h-l)//2
            if(nums[m] == target):
                return m
            elif(nums[m] >= nums[l]): # left half is sorted
                if(nums[l] <= target and  target <= nums[m]):
                    h = m-1
                else:
                    l = m+1
            elif(nums[m] <= nums[h]): # right hald is sorted
                if(nums[m] <= target and target <= nums[h]):
                    l = m+1
                else:
                    h = m-1
        return -1

result = Solution().search([4,5,6,7,0,1,2] , 3)
print(result)