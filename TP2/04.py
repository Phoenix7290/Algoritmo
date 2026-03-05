# 04.py - Letra que falta (a-z)

import string

def letra_ausente(s):
    alfabeto = set(string.ascii_lowercase)
    presente = set()
    
    for c in s.lower():
        if c.isalpha():
            presente.add(c)
    
    faltam = sorted(alfabeto - presente)
    if not faltam:
        return None
    return faltam[0]   # retorna a primeira em ordem alfabética


if __name__ == "__main__":
    print("=== Teste 04.py ===\n")
    frases = [
        "The quick brown fox jumps over the lazy dog",
        "hello world",
        "a b c d e f g h i j k l m n o p q r s t u v w x y",
        "Sphinx of black quartz, judge my vow."
    ]
    
    for f in frases:
        print(f"Frase: {f}")
        print(f"Letra faltante: {letra_ausente(f)}")
        print()