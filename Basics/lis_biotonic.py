def lis_biotonic(nums: list):
    lis = [0] * len(nums)
    lds = [0] * len(nums)
    lis[0] = 1
    lds[-1] = 1

    # lis
    for i in range(1, len(nums)):
        _max = 0
        for j in range(i):
            if (nums[i] > nums[j]):
                _max = max(_max, lis[j])
        lis[i] = 1 + _max
    # lds
    for i in range(len(nums) - 2, -1, -1):
        _max = 0
        for j in range(len(nums) - 1, i - 1, -1):
            if (nums[i] > nums[j]):
                _max = max(_max, lds[j])
        lds[i] = 1 + _max

    
    print(
        max(
            [lis[i] + lds[i] - 1 for i in range(len(lis))]
        )
    )


lis_biotonic([10, 22, 9, 33, 21, 50, 41, 60, 80, 3])
