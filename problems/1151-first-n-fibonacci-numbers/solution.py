def first_n_fibonacci(n):
    # Return a list of the first n Fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
    fib = [0,1]
    if n == 2:
        return fib
    for n in range(2,n):
        fib.append(fib[n-1] + fib[n-2])
    return fib