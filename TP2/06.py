def selection_sort(arr):
    comparacoes = 0
    trocas = 0
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1
    
    print(f"Comparações: {comparacoes:6d}  Trocas: {trocas:4d}")
    return arr


if __name__ == "__main__":
    print("=== Teste 06.py ===\n")
    for caso in [
        list(range(20,0,-1)),
        list(range(1,21)),
        [3,1,4,1,5,9,2,6,5,3,5]
    ]:
        print(f"Antes : {caso}")
        ordenado = selection_sort(caso)
        print(f"Depois: {ordenado}\n")