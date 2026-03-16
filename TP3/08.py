def fib_memo(n, memo=None, calls=0):
    if memo is None:
        memo = {}
    calls += 1
    
    if n in memo:
        return memo[n], calls
    
    if n <= 1:
        memo[n] = n
        return n, calls
    
    a, c1 = fib_memo(n-1, memo, calls)
    b, c2 = fib_memo(n-2, memo, calls)
    calls += c1 + c2 - calls
    
    memo[n] = a + b
    return memo[n], calls