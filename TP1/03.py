array = [2, 4, 6, 8, 10, 12, 13]
target = 8
steps = 0

for num in array:
    steps += 1
    if num == target:
        print(f"Encontrou {target} em {steps} passos")
        break
else:
    print(f"Não encontrou {target}")
