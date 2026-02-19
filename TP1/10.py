def bubble_sort_strings(list):
    """
    Bubble Sort adaptado para ordenar strings em ordem alfabética (crescente).
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

def test_bubble_sort_strings():
    casos = [
        ["banana", "apple", "cherry", "date", "blueberry"],     
        ["Zebra", "apple", "Banana", "zebra", "Apple"],  
        ["python", "java", "c++", "javascript", "ruby"],
        ["ana", "ana", "ana"], 
        ["zebra"], 
        [], 
        ["manga", "maçã", "melancia", "morango", "abacaxi"],
        ["João", "Maria", "José", "Ana", "Pedro"]
    ]
    
    for i, list in enumerate(casos, 1):
        original = list.copy()
        result = bubble_sort_strings(list)
        
        print(f"\nTeste {i}:")
        print(f"  Antes:  {original}")
        print(f"  Depois: {result}")
        
        if result == sorted(original):
            print("  → Ordenado corretamente!")
        else:
            print("  → ERRO na ordenação!")


if __name__ == "__main__":
    test_bubble_sort_strings()