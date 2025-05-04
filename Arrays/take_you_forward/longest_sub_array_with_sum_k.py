class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        # Complete the function
        map = dict()
        map[0] = -1
        sum = 0
        length = 0

        for i in range(n):
            sum += arr[i]
            if (sum == k):
                length = max(length, i + 1)
            elif ((sum - k) in map):
                rem = sum - k
                length = max(length, (i - map[rem]))
            if (sum not in map):
                map[sum] = i
        return length
