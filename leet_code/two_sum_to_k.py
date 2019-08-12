def two_sum(nums, k):
    res = set()
    set_nums = set(nums)
    for n in nums:
        if (k - n in set_nums and 
            (n, k-n) not in res and 
            (k-n, n) not in res): 
            res.add((n, k-n))
    return list(res)


nums = [10, 15, 3, 7, 14, 2]
k = 17
print(two_sum(nums, k))