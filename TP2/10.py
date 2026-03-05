class Queue:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.itens = [None] * capacidade
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0
    
    def is_empty(self):
        return self.tamanho == 0
    
    def is_full(self):
        return self.tamanho == self.capacidade
    
    def enqueue(self, valor):
        if self.is_full():
            raise OverflowError("Fila cheia")
        
        self.itens[self.fim] = valor
        self.fim = (self.fim + 1) % self.capacidade
        self.tamanho += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Fila vazia")
        
        valor = self.itens[self.inicio]
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return valor
    
    def __str__(self):
        if self.is_empty():
            return "[ vazia ]"
        elementos = []
        i = self.inicio
        for _ in range(self.tamanho):
            elementos.append(str(self.itens[i]))
            i = (i + 1) % self.capacidade
        return f"[ {', '.join(elementos)} ]  (inicio={self.inicio}, fim={self.fim})"


if __name__ == "__main__":
    print("=== 10 - Fila circular ===\n")
    f = Queue(6)
    
    print("Enfileirando 1,2,3,4")
    for v in [1,2,3,4]:
        f.enqueue(v)
        print(f)
    
    print("\nDesenfileirando 2 elementos:")
    print("dequeue →", f.dequeue())
    print(f)
    print("dequeue →", f.dequeue())
    print(f)
    
    print("\nEnfileirando 5,6,7 (testando circularidade)")
    for v in [5,6,7]:
        f.enqueue(v)
        print(f)