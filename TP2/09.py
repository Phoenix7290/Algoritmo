class Stack:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.itens = [None] * capacidade
        self.topo = -1
    
    def is_empty(self):
        return self.topo == -1
    
    def is_full(self):
        return self.topo == self.capacidade - 1
    
    def push(self, valor):
        if self.is_full():
            raise OverflowError(f"Pilha cheia (capacidade = {self.capacidade})")
        self.topo += 1
        self.itens[self.topo] = valor
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Underflow: pilha vazia")
        valor = self.itens[self.topo]
        self.topo -= 1
        return valor
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Pilha vazia")
        return self.itens[self.topo]
    
    def __str__(self):
        if self.is_empty():
            return "[ vazia ]"
        return f"[ {', '.join(str(self.itens[i]) for i in range(self.topo+1))} ] <- topo"


if __name__ == "__main__":
    print("=== 09 - Pilha com controle de erros ===\n")
    p = Stack(5)
    
    try:
        for i in range(1, 7):
            print(f"push({i})")
            p.push(i)
            print(p)
    except OverflowError as e:
        print("→", e)
    
    print("\nDesempilhando:")
    while not p.is_empty():
        print(f"pop() → {p.pop():2d}   |  pilha: {p}")
    
    try:
        print("Tentando pop() em pilha vazia...")
        p.pop()
    except IndexError as e:
        print("→", e)