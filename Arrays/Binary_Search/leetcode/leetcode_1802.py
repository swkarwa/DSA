from typing import List
class Solution:
    def is_possible(self, n, index, max_sum, max_value):
        result = [0 for _ in range(n)]
        result[index] = max_value
        # compute left values
        value = max_value
        left_sum = 0
        for i in range(index - 1, -1, -1):
            if (value > 1):
                value -= 1
            left_sum+=value
            result[i] = value
        # compute right values
        value = max_value
        right_sum = 0
        for i in range((index + 1), n):
            if (value > 1):
                value -= 1
            right_sum += value
            result[i] = value

        print(result)
        return (left_sum + max_value + right_sum) <= max_sum

    def maxValue(self, n: int, index: int, max_sum: int) -> int:
        l, h = 1, max_sum
        ans = 0
        while (l <= h):
            m_value = l + (h - l) // 2
            if (self.is_possible(n, index, max_sum, m_value)):
                ans = m_value
                l = m_value + 1
            else:
                h = m_value - 1
        return ans

result = Solution().maxValue(7,5,10)
print(result)