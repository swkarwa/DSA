class Solution:

    def __init__(self):
        self.count = 0

    def inversion_count(self, arr):
        self.merge_sort(arr, 0, len(arr) - 1)
        return self.count

    def merge_sort(self, arr, l, h):
        if (l == h):
            return [arr[l]]
        mid = (l + h) // 2
        fsh = self.merge_sort(arr, l, mid)
        ssh = self.merge_sort(arr, mid + 1, h)
        return self.merge(fsh, ssh)

    def merge(self, fsh, ssh):
        l = 0
        r = 0
        result = list()
        while (l < len(fsh) and r < len(ssh)):
            if (fsh[l] <= ssh[r]):
                result.append(fsh[l])
                l += 1
            else:
                self.count += len(fsh) - l
                result.append(ssh[r])
                r += 1
        while (l < len(fsh)):
            result.append(fsh[l])
            l += 1
        while (r < len(ssh)):
            result.append(ssh[r])
            r += 1
        return result

count = Solution().inversion_count([2,4,1,3,5])
print(count)