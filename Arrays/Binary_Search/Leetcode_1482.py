from typing import List

class Solution:
    def is_possible(self, bloom_day: List['int'], m_bouquetes: int, k_adj_flowers: int, current_day: int) -> bool:
        count = 0
        formed_bouqutes = 0
        for flower in bloom_day:
            if (flower <= current_day):
                count += 1
            else:
                formed_bouqutes += count // k_adj_flowers
                count = 0

        formed_bouqutes += count // k_adj_flowers

        if (formed_bouqutes >= m_bouquetes):
            return True
        return False

    def minDays(self, bloom_day: List[int], m_bouquets: int, k_adj_flowers: int) -> int:
        if ((m_bouquets * k_adj_flowers) > len(bloom_day)):
            return -1
        l, h = min(bloom_day), max(bloom_day)
        ans = 0
        while (l <= h):
            current_day = (l + h) // 2
            if (self.is_possible(bloom_day, m_bouquets, k_adj_flowers, current_day)):
                ans = current_day
                h = current_day - 1
            else:
                l = current_day + 1
        return ans


result = Solution().minDays([1,10,3,10,2] , 3 , 1)
print(result)
