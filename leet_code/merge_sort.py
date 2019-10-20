def merge_sort(arr):
    if len(arr) <= 1: return arr
    m = len(arr) // 2
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])

    l, r =  0, 0
    result = []
    while(l < len(left) and r < len(right)):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    while l < len(left):
        result.append(left[l])
        l += 1

    while r < len(right):
        result.append(right[r])
        r += 1

    return result


sorted_arr = (merge_sort([1, 5, 3, 7, 4, 6, 2]))


def binary_search(arr, x):
    l, r = 0, len(arr)
    
    while l < r:
        m = (l + ((r-l) // 2))
        print(arr[l:r], arr[m])
        if arr[m] > x: r = m
        elif arr[m] < x: l = m+1
        else: return m

    return None

print(binary_search(sorted_arr, 1))
print(binary_search(sorted_arr, 6))
print(binary_search(sorted_arr, 9))


