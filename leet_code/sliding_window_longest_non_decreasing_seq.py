def longest_non_dec_seq(nums):
    start, end = 0, 1  # end is non-inclusive
    best_start, best_end = 0, 1
    for i in range(1, len(nums)):
        # we can safely use this check because we know every element 
        # before this group must be smaller
        if nums[i] < nums[i-1]: 
            print(end - start)
            if end - start > best_end - best_start:
                best_start = start
                best_end = end + 1
            start = end
        end += 1
        if end - start > best_end - best_start:
            best_start = start
            best_end = end
        

    return nums[best_start:best_end]

print(longest_non_dec_seq([1, 2, 3, 5, 4, 2, 7, 8, 9, 10, 11]))

