def quickselect(arr, k, low=0, high=None, stats=None):
    if high is None:
        high = len(arr) - 1
    if stats is None:
        stats = {"comparisons": 0}
    
    if low == high:
        return arr[low]
    
    pivot_idx = partition(arr, low, high, stats)
    
    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return quickselect(arr, k, low, pivot_idx-1, stats)
    else:
        return quickselect(arr, k, pivot_idx+1, high, stats)


vetor = [10, 80, 30, 90, 40, 50, 70]
print(quickselect(vetor.copy(), len(vetor)//2))
