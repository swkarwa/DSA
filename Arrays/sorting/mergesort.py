from heapq import merge


def merge_sort(l: list, low: int, high: int) -> list:
    if (low == high):
        return [l[low]]
    mid = (low + high) // 2
    fsh = merge_sort(l, low, mid)
    ssh = merge_sort(l, mid + 1, high)
    return merge_sorted_arrays(fsh, ssh)


def merge_sorted_arrays(l1: list, l2: list) -> list:
    i = 0
    j = 0

    result = [];
    while (i < len(l1) and j < len(l2)):
        if (l1[i] <= l2[j]):
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    while (i < len(l1)):
        result.append(l1[i])
        i += 1
    while (j < len(l2)):
        result.append(l2[j])
        j += 1
    return result


nums = [10, 5, 7, 3, 6]
result = merge_sort(nums, 0, len(nums) - 1)
print(result)
