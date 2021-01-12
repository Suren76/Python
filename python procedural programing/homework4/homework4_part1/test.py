numbers = [1, 12, 4] ,[-1, 0, 1, 2] ,[] ,[-1, 0.4] 

def sum_x(num):
    sum_x =0
    for x in num:
        sum_x +=x
    return sum_x

x=0
while x<len(numbers):
    print(sum_x(numbers[x]))
    x+=1