def p_factorial(n):
    def factorial(n):
        if n == 1:
            return n
        return n*factorial(n-1)

    return("{}! = {}".format(n,(factorial(n))))

print(p_factorial(5))