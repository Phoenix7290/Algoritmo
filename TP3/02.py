import math

def factor(x, lowest=2):
    if x <= 1:
        return [] if x == 1 else ["invalid" if x == 0 else "negative"]
    
    if x < 0:
        return ["-"] + factor(-x, lowest)
    
    fatores = []
    
    while lowest * lowest <= x:
        if x % lowest == 0:
            fatores.append(lowest)
            return fatores + factor(x // lowest, lowest)
        lowest += 1 if lowest == 2 else 2
    
    if x > 1:
        fatores.append(x)
    
    return fatores


print(factor(1))
print(factor(13))
print(factor(100))
print(factor(315))
print(factor(-60))