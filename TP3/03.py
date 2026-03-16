def power(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    
    if y < 0:
        return 1 / power(x, -y)
    
    if y % 2 == 0:
        half = power(x, y // 2)
        return half * half
    
    return x * power(x, y - 1)


print(power(2, 10))
print(power(3, 5))
print(power(2, -3))
print(power(5, 0))