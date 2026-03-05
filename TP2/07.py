def insertion_sort(arr):
    comparacoes = 0
    deslocamentos = 0
    n = len(arr)
    arr = arr.copy()  
    
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        
        while j >= 0:
            comparacoes += 1
            if arr[j] > chave:
                arr[j + 1] = arr[j]
                deslocamentos += 1
                j -= 1
            else:
                break
        
        arr[j + 1] = chave
    
    print(f"Comparações: {comparacoes:6d}  Deslocamentos: {deslocamentos:5d}")
    return arr


if __name__ == "__main__":
    print("=== 07 - Insertion Sort ===\n")
    
    quase_ordenado = list(range(1, 51)) + [45] + list(range(46, 50))
    
    invertido = list(range(50, 0, -1))
    
    aleatorio = [42, 17, 88, 5, 31, 99, 12, 64, 23, 77]
    
    casos = [
        ("Quase ordenado", quase_ordenado),
        ("Invertido", invertido),
        ("Aleatório pequeno", aleatorio)
    ]
    
    for nome, lista in casos:
        print(f"{nome} ({len(lista)} elementos)")
        print(f"Antes:  {lista[:15]}{'...' if len(lista)>15 else ''}")
        ordenado = insertion_sort(lista)
        print(f"Depois: {ordenado[:15]}{'...' if len(ordenado)>15 else ''}")
        print()