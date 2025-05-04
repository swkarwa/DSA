from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        i = j = -1
        ans = 0
        while (True):
            f1 = f2 = False
            while (i < len(nums) - 1 and odd_count <= k):
                f1 = False
                i += 1
                num = nums[i]
                if (num % 2 == 1):
                    odd_count+=1
                if(odd_count == k):
                    ans+=1

            while (j < i and odd_count > k):
                f2 = False
                j += 1
                num = nums[j]
                if (num % 2 == 1):
                    odd_count-=1
                if(odd_count == k):
                    ans+=1
                    break
            if (not f1 and not f2):
                break
        return ans

    def numberOfSubarrays_self(self, nums: List[int], k: int) -> int:
        odd_count = 0
        i = j = -1
        ans = 0
        while (True):

            f1 = f2 = False
            while (i < len(nums) - 1 and odd_count <= k):
                f1 = True
                i += 1
                num = nums[i]
                if (num % 2 == 1):
                    odd_count += 1
                if (odd_count == k):
                    ans +=(i-j)

            while (j < i and odd_count > k):
                f2 = True
                j += 1
                num = nums[j]
                if (num % 2 == 1):
                    odd_count -= 1
                if (odd_count == k):
                    ans +=(i-j)

            if (not f1 and not f2):
                break
        return ans

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
s = Solution()
result = s.numberOfSubarrays_self(nums , k) + s.numberOfSubarrays_self(nums , k-1)
print(result)
