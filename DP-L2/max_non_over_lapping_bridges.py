from typing import List


def max_non_over_lapping_bridges(bridges: List[List[int]]):
    bridges = sorted(bridges, key=lambda x: (x[0], x[1]))
    dp = [0] * len(bridges)
    dp[0] = 1
    for i in range(1,len(bridges)):
        _max = 0
        for j in range(i):
            if (bridges[i][1] > bridges[j][1]):
                _max = max(_max, dp[j])
        dp[i] = 1 + _max
    print(dp)
    print(max(dp))


bridges = [[10, 20], [2, 7], [8, 15], [17, 3], [21, 40], [50, 4], [41, 57], [60, 80], [80, 90], [1, 30]]
max_non_over_lapping_bridges(bridges)
