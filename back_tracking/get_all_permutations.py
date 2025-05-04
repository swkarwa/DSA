from typing import List


def solution(nums: List[int]):
    def back_track(idx, current):
        if (len(current) >= 1):
            result.append(current[:])

        for i in range(idx, len(nums)):
            current.append(nums[i])
            back_track(i + 1, current)
            current.pop()

    result = list()
    back_track(0 , [])
    return result


print(solution([4, 6, 7, 7]))
