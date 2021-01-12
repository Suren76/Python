numbers = input("Input format: num1 num2 step ")
numbers = numbers.split(" ")
num_a=int(numbers[0])
num_b=int(numbers[1])
step=int(numbers[2])
def print_num(a,b,step):
    res = []
    while a<=b:
        res.append(a)
        a +=step
    return res

print(print_num(num_a,num_b,step))