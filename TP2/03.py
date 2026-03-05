def primeiro_duplicado(arr):
    visto = set()
    
    for i, valor in enumerate(arr):
        if valor in visto:
            return valor, i
        visto.add(valor)
    
    return None


if __name__ == "__main__":
    print("=== Teste 03.py ===\n")
    
    exemplos = [
        ["a", "b", "c", "d", "b", "e"],
        [1,2,3,4,5,3,6],
        ["x"]*10 + ["y"] + ["x"],
        list("algoritmo") + ["a"]
    ]
    
    for ex in exemplos:
        dup = primeiro_duplicado(ex)
        print(f"Lista: {ex}")
        print(f"Primeiro duplicado: {dup}")
        print()