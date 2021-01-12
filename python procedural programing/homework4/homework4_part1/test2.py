numbers = input("Input format: num1 num2 step ")

def print_num(n):
    n = n.split(" ")
    a=int(n[0])
    b=int(n[1])
    step=int(n[2])
    res = []
    while a<=b:
        res.append(a)
        a +=step
    return res

print(print_num(numbers))