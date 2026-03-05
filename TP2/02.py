def intersecao_linear(a, b):
    if not a or not b:
        return []
    
    if len(a) > len(b):
        a, b = b, a
    
    seen = set()
    for x in a:
        seen.add(x)
    
    resultado = []
    for x in b:
        if x in seen:
            resultado.append(x)
            seen.remove(x)
    
    return resultado


if __name__ == "__main__":
    print("=== Teste 02.py ===\n")
    
    testes = [
        ([1,2,2,1], [2,2]),
        (list(range(1,10001,3)), list(range(0,10000,7))),
        ([], [5,6,7]),
        ([9,9,9], [9])
    ]
    
    for i, (a,b) in enumerate(testes,1):
        print(f"Teste {i}:")
        print(f"  A = {a[:15]}{'...' if len(a)>15 else ''}")
        print(f"  B = {b[:15]}{'...' if len(b)>15 else ''}")
        print(f"  Interseção = {intersecao_linear(a,b)}")
        print()