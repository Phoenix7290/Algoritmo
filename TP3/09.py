def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = []
    right = []
    
    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    
    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([3, 6, 8, 10, 1, 2, 1]))
print(quicksort([1, 2, 3, 4, 5, 6, 7]))
print(quicksort([7, 6, 5, 4, 3, 2, 1]))