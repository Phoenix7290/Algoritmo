# 01.py - Maior número único - quadrático vs hash

def maior_unico_quadratico(nums):
    """O(n²) - dois laços"""
    comparacoes = [0]
    
    def conta_comp():
        comparacoes[0] += 1
    
    maior = float('-inf')
    for i in range(len(nums)):
        unico = True
        for j in range(len(nums)):
            conta_comp()
            if i != j and nums[i] == nums[j]:
                unico = False
                break
        if unico:
            maior = max(maior, nums[i])
    
    print(f"Quadrático → comparações: {comparacoes[0]}")
    return maior if maior != float('-inf') else None


def maior_unico_hash(nums):
    """O(n) usando hash"""
    contagem = {}
    acessos = 0
    
    for num in nums:
        acessos += 1
        contagem[num] = contagem.get(num, 0) + 1
    
    maior = float('-inf')
    for num in nums:           # mantém a primeira ocorrência na ordem
        acessos += 1
        if contagem[num] == 1:
            maior = max(maior, num)
    
    print(f"Hash → acessos: {acessos}")
    return maior if maior != float('-inf') else None


# Testes comparativos
if __name__ == "__main__":
    print("=== Teste 01.py ===\n")
    
    casos = [
        [4, 2, 5, 2, 4, 7, 3],
        list(range(2000)) + [42] + list(range(1999, -1, -1)),
        [1] * 100 + [777]
    ]
    
    for i, lst in enumerate(casos, 1):
        print(f"Caso {i}  (tamanho = {len(lst)})")
        print("  Quadrático:", maior_unico_quadratico(lst[:]))
        print("  Hash      :", maior_unico_hash(lst[:]))
        print()