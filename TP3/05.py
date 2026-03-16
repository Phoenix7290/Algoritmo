def teams(candidates, k, atual="", start=0, resultado=None):
    if resultado is None:
        resultado = []
    
    if k == 0:
        resultado.append(atual)
        return
    
    for i in range(start, len(candidates)):
        teams(candidates, k-1, atual + candidates[i], i+1, resultado)
    
    return resultado


pessoas = "ABCDE"
print(teams(pessoas, 3))
