from collections import Counter

def primeiro_nao_repetido(s):
    if not s:
        return None
    
    freq = Counter(s)
    for c in s:
        if freq[c] == 1:
            return c
    return None


if __name__ == "__main__":
    print("=== Teste 05.py ===\n")
    
    for palavra in ["aabbc", "leetcode", "loveleetcode", "a", "aa", "abcabc"]:
        print(f"{palavra:15} → {primeiro_nao_repetido(palavra)}")