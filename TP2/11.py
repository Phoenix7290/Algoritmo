class Stack:
    def __init__(self):
        self.itens = []
    
    def push(self, item):
        self.itens.append(item)
    
    def pop(self):
        if not self.itens:
            raise IndexError("Pilha vazia")
        return self.itens.pop()
    
    def is_empty(self):
        return len(self.itens) == 0


def inverte_string(s):
    pilha = Stack()
    for char in s:
        pilha.push(char)
    
    resultado = []
    while not pilha.is_empty():
        resultado.append(pilha.pop())
    
    return ''.join(resultado)


if __name__ == "__main__":
    print("=== 11 - Inversão com pilha ===\n")
    testes = [
        "Python",
        "Estrutura de Dados",
        "1234567890",
        "A man a plan a canal Panama",
        ""
    ]
    
    for t in testes:
        print(f"Original : {t}")
        print(f"Invertida: {inverte_string(t)}")
        print()