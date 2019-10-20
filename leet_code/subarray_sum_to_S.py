def subarray_sum_to_S(arr, S):
    l, r = 0, 1
    total = arr[l]
    while True:
        if total < S:
            # expand window to the right
            total += arr[r]
            r += 1
            if r >= len(arr): return None

        elif total > S:
            # shrink window from left
            total -= arr[l]
            l += 1
            if l >= len(arr): return None
        else: return arr[l:r]

    return None

print(subarray_sum_to_S([1, 4, 20, 3, 10, 5], 33))