def fib(n):
    if n <= 1:
        return n
        
    return fib(n-1)+fib(n-2)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(21))
