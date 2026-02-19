def bubble_sort(list):
    """
    Implementa o Bubble Sort para ordenar uma lista em ordem crescente.
    Modifica a lista original (in-place).
    """
    n = len(list)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        
        if not swapped:
            break
    
    return list 

def test_bubble_sort():
    casos_teste = [
        [64, 34, 25, 12, 22, 11, 90],           
        [5, 1, 4, 2, 8],                        
        [1, 2, 3, 4, 5],                        
        [5, 4, 3, 2, 1],                        
        [42],                                   
        [],                                     
        [7, 7, 7, 7],                           
        [10, -5, 0, 3, -8, 12, -1]            
    ]
    
    for i, list in enumerate(casos_teste, 1):
        original = list.copy()  
        result = bubble_sort(list)
        
        print(f"\nTeste {i}:")
        print(f"  Antes:  {original}")
        print(f"  Depois: {result}")
        
        if result == sorted(original):
            print("  → Ordenado corretamente!")
        else:
            print("  → ERRO na ordenação!")


if __name__ == "__main__":
    test_bubble_sort()