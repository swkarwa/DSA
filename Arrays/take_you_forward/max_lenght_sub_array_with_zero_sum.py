class Solution:
    def maxLen(self, n, arr):
        #Code here
        map = dict()
        map[0] = -1
        _sum = 0
        length = 0
        for i in range(len(arr)):
            _sum+=arr[i]
            if(_sum in map):
                length = max(length , i - map[_sum])
            else:
                map[_sum] = i
        return length

Solution().maxLen([15, -2, 2, -8, 1 ,7 ,10, 23])