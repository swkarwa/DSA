from importlib.util import source_hash


def find_first_and_last(l: list, k: int):
    low = 0
    high = len(l) - 1
    fi = -1;
    while (low <= high):
        mid = (low + high) // 2
        if (l[mid] == k):
            fi = mid
            high = mid - 1
        elif (l[mid] < k): low = mid + 1
        elif (l[mid] > k): high = mid - 1

    low = 0
    high = len(l) - 1
    while (low <= high):
        mid = (low + high) // 2
        if (l[mid] == k):
            li = mid
            low = mid + 1
        elif (l[mid] < k): low = mid + 1
        else: high = mid - 1
    print(fi, li)


nums = [5, 7, 7, 8, 8, 10]
find_first_and_last(nums, 8)
