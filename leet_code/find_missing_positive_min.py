def find_pos_min(L):
    """Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
    
    Arguments:
        L {List} -- list of integers to search through
    """
    # First strategy: sort in O(NlogN), loop in O(N), but sorting already
    # exceeds O(N) restraint

    # Second strategy: form set from L, continuously increment min until no more
    # O(1) search, O(N) worse-case loop
    min_num = 1
    nums = set(L)
    while(True):
        if min_num in nums: min_num += 1
        else: return min_num
    

assert(find_pos_min([3, 4, -1, 1]) == 2)
assert(find_pos_min([1, 2, 0]) == 3)

