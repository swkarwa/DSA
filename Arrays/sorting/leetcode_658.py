import heapq as heap


class Solution:

    def find_k_closest(self, arr, k, x):
        _list = []
        for e in arr:
            heap.heappush(_list, (abs(e - x), e))
        result = []
        for _ in range(k):
            result.append(heap.heappop(_list)[1])
        return sorted(result)


result = Solution().find_k_closest([1, 2, 3, 4, 5], 4, 3)
print(result)
