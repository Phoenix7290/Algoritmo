def partition(arr, low, high, stats):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        stats["comparisons"] += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            stats["swaps"] += 1
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    stats["swaps"] += 1
    return i + 1


def quicksort_inplace(arr, low=0, high=None, stats=None):
    if stats is None:
        stats = {"comparisons": 0, "swaps": 0}
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high, stats)
        quicksort_inplace(arr, low, pi-1, stats)
        quicksort_inplace(arr, pi+1, high, stats)
    
    return stats


vetor = [10, 80, 30, 90, 40, 50, 70]
stats = quicksort_inplace(vetor)
print("Ordenado:", vetor)
print(stats)