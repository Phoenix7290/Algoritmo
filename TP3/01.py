def mult(x, y, depth=0):
    indent = "  " * depth
    print(f"{indent}mult({x}, {y}) chamada")
    
    if y == 0:
        print(f"{indent}→ retorno 0 (caso base y=0)")
        return 0
    
    resultado = x + mult(x, y - 1, depth + 1)
    
    print(f"{indent}→ retorno {resultado}  (depois de somar {x})")
    return resultado


print(" mult(3,4):")
print("Resultado final:", mult(3, 4))
print("\n mult(5,0):")
print("Resultado final:", mult(5, 0))