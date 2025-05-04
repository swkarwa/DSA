import heapq


def min_meeting_rooms(intervals) -> int:
    if not intervals:
        return 0;
    intervals = sorted(intervals, key=lambda x: x[0])
    min_heap = []
    heapq.heappush(min_heap, intervals[0][1])

    for i in range(1, len(intervals)):
        start_time = intervals[i][0]
        end_time = intervals[i][1]
        min_end_time = min_heap[0]

        if start_time < min_end_time:
            heapq.heappush(min_heap, end_time)
        else:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, end_time)
            heapq
    print(len(min_heap))
    return len(min_heap)

min_meeting_rooms([[0,30],[5,10],[15,20]])