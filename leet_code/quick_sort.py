def quick_sort(nums, low, high):
    if high - low <= 1: return
    pi = partition(nums, low, high)
    quick_sort(nums, low, pi-1)
    quick_sort(nums, pi+1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low  # keeps track of the smaller element index
    for j in range(low, high):
        if nums[j] < pivot: 
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i


a = [1, 5, 2, 8, 4, 6]
quick_sort(a, 0, len(a)-1)
print(a)