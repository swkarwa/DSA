def lis_max_sum(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        _max = -float('inf')
        for j in range(i):
            if (nums[i] > nums[j]):
                _max = max(_max, dp[j])
        if (_max == -float('inf')):
            dp[i] = nums[i]
        else:
            dp[i] = _max + nums[i]

    print(dp)


lis_max_sum([10, 22, 9, 33, 21, 50, 41, 60, 80, 3])
