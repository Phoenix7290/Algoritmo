def knapsack(target, weights, index=None, caminho=None, todas=None):
    if todas is None:
        todas = []
    if caminho is None:
        caminho = []
    if index is None:
        index = len(weights)-1
    
    if target == 0:
        todas.append(caminho[:])
        return
    
    if target < 0 or index < 0:
        return
    
    knapsack(target, weights, index-1, caminho, todas)
    
    caminho.append(weights[index])
    knapsack(target - weights[index], weights, index-1, caminho, todas)
    caminho.pop()
    
    return todas


pesos = [2, 3, 4, 7, 8, 10]
print(knapsack(11, pesos))