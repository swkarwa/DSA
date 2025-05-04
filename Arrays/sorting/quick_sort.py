def quick_sort(l: list, low: int, high: int) -> list:
    if (low >= high):
        return
    pi = partation(l, low, high)
    quick_sort(l, low, pi - 1)
    quick_sort(l, pi + 1, high)


def partation(l: list, low: int, high: int):
    i = low
    j = low
    pivot = l[high]
    while (i <= high):
        if (l[i] <= pivot):
            l[i], l[j] = l[j], l[i]
            j += 1
        i += 1
    return j - 1;


nums = [10, 15, 20, 17, 30]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
