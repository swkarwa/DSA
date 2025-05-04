import sys

sys.setrecursionlimit(10 ** 6)


def quick_sort(l: list, low: int, high: int):
    if (low >= high):
        return
    pi = partation(l , low , high)
    quick_sort(l , low , pi-1)
    quick_sort(l, pi+1, high)

def quick_select(l: list, k: int, low: int, high: int):
    if (low <= high):
        pi = partation(l, low, high)
        if (k > pi):
            return quick_select(l, k, pi + 1, high)
        elif (k < pi):
            return quick_select(l, k, low, pi - 1)
        else:
            return l[pi]
    raise ValueError("k is not in valid range")


def partation(l: list, low: int, high: int):
    pivot = l[high]
    i = low;
    for j in range(low, high):
        if (l[j] <= pivot):
            l[i], l[j] = l[j], l[i]
            i += 1
    l[i], l[high] = l[high], l[i]
    return i


nums = [10, 15, 20, 17, 30]
result = quick_sort(nums,  0, len(nums) - 1)
print(nums)
