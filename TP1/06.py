def quadratic_grains(grains):
    """
    Retorna o número do quadrado onde exatamente 'grains' grãos são colocados.
    Retorna None se a quantidade não for uma potência exata de 2.
    """
    if grains <= 0:
        return None
    
    square = 1
    current = 1
    
    while current < grains:
        square += 1
        current *= 2
        if current == grains:
            return square
    
    return None


test = [1, 2, 4, 8, 16, 32, 64, 3, 100, 0]
for qtd in test:
    res = quadratic_grains(qtd)
    print(f"{qtd:4} grãos → quadrado {res}")
    