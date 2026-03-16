def fib(n, calls=0):
    calls += 1
    if n <= 1:
        return n, calls
    a, c1 = fib(n-1)
    b, c2 = fib(n-2)
    return a+b, calls + c1 + c2