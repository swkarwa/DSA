import heapq

max_heap =[]
heapq.heappush(max_heap , -5)
heapq.heappush(max_heap , -3)
heapq.heappush(max_heap , -4)
print(heapq.heappop(max_heap))
print(max_heap)