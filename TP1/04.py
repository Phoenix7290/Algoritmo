def busca_binaria_detalhada(arr, alvo):
    passos = 0
    esquerda = 0
    direita = len(arr) - 1
    
    print("Busca binária passo a passo:")
    while esquerda <= direita:
        passos += 1
        meio = (esquerda + direita) // 2
        print(f"Passo {passos}: intervalo [{esquerda}..{direita}] → meio = {meio} (valor = {arr[meio]})")
        
        if arr[meio] == alvo:
            print(f"→ Encontrou {alvo} na posição {meio} em {passos} passo(s)!")
            return passos, True
        elif arr[meio] < alvo:
            print(f"→ {arr[meio]} < {alvo} → procura na metade direita")
            esquerda = meio + 1
        else:
            print(f"→ {arr[meio]} > {alvo} → procura na metade esquerda")
            direita = meio - 1
    
    print(f"Não encontrou {alvo}")
    return passos, False


array = [2, 4, 6, 8, 10, 12, 13]
busca_binaria_detalhada(array, 8)
