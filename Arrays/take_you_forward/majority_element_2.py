from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        el1, count1 = None, 0
        el2, count2 = None, 0
        for num in nums:
            if (num == el1):
                count1 += 1
            elif (num == el2):
                count2 += 1
            elif (count1 == 0):
                el1, count1 = num, 1
            elif (count2 == 0):
                el2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        count1,count2 = 0,0
        for num in nums:
            if(num == el1):
                count1+=1
            elif(num == el2):
                count2+=1
        if(count1 > len(nums)//3):
            result.append(el1)
        if(el1 != el2 and count2 > len(nums)//3):
            result.append(el2)
        return result



result = Solution().majorityElement([2, 1, 1, 3, 1, 4, 5, 6])
print(result)
