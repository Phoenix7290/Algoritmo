# Após analisar na internet, possuí diversos nomes como cocktailSort ou Shaker Sort

def cocktailSort(self):
    """
    Bubble Sort bidirecional (Cocktail Shaker Sort)
    Alterna direção: esquerda→direita (sobe maior) e direita→esquerda (desce menor)
    """
    left = 0
    right = self.__nItems - 1
    swapped = True  

    while left < right and swapped:
        swapped = False

        for i in range(left, right):
            if self.__a[i] > self.__a[i + 1]:
                self.swap(i, i + 1)
                swapped = True

        right -= 1  

        for i in range(right, left, -1):
            if self.__a[i] < self.__a[i - 1]:
                self.swap(i, i - 1)
                swapped = True

        left += 1  
